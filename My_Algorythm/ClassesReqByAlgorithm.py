import math
from typing import List
import copy


class Pv:
    # photo-voltaic panel

    def __init__(self, id, price, power, efficiency, area, quantity=0):
        self.id = id
        self.price = price  # PLN
        self.power = power  # W
        self.efficiency = efficiency  # %
        self.area = area  # m^2
        self.quantity = quantity

    def __str__(self):
        return str(self.id) + " " + str(self.quantity)

    def cost(self):
        return self.price * self.quantity

    def total_power(self):
        return self.power * self.quantity * self.efficiency

    def total_area(self):
        return self.quantity * self.area

    @staticmethod
    def get_name(elem_id: int):
        return {
            11: "Panel polikrystaliczny",
            12: "Panel monokrystaliczny",
            13: "Panel z krzemu amorficznego",
            14: "Panel cieńkowarstwowy"
        }.get(elem_id, "Panel niezidentyfikowany")


class Battery:

    def __init__(self, id, price, capacity, efficiency, area, quantity=0):
        self.id = id  # identyfikator panelu
        self.price = price  # PLN
        self.capacity = capacity  # Wh
        self.efficiency = efficiency  # %
        self.area = area  # m^2
        self.quantity = quantity

    def __str__(self):
        return str(self.id) + " " + str(self.quantity)

    def cost(self):
        return self.price * self.quantity

    def total_capacity(self):
        return self.capacity * self.quantity

    def total_area(self):
        return self.area * self.quantity

    @staticmethod
    def get_name(elem_id: int):
        return {
            21: "Tesla PowerPack",
            22: "StornEn PowerPack",
            23: "Tesla MegaPack ",
        }.get(elem_id, "Bareria niezidentyfikowany")


class Taboo:
    def __init__(self, pvs: List[Pv], batteries: List[Battery], limit: int, internal_budget: int):
        self.internal_budget = internal_budget
        self.taboo_list = {}
        self.limit = limit  # ile razy może się pojawić gorsze rozwiązanie
        for panel in pvs:
            self.taboo_list[panel.id] = {}
            while panel.cost() <= internal_budget:
                self.taboo_list[panel.id][panel.quantity] = 0
                panel.quantity += 1
            self.taboo_list[panel.id][panel.quantity] = 0
            panel.quantity = 0

        for battery in batteries:
            self.taboo_list[battery.id] = {}
            while battery.cost() <= internal_budget:
                self.taboo_list[battery.id][battery.quantity] = 0
                battery.quantity += 1
            self.taboo_list[battery.id][battery.quantity] = 0
            battery.quantity = 0

    def update(self, pvs: List[Pv], batteries: List[Battery]):

        for panel in pvs:
            try:
                if panel.quantity != 0:
                    self.taboo_list[panel.id][panel.quantity] += 1
            except KeyError:
                print("\n\n!!!!!")
                print("budget = ", self.internal_budget)
                print("Panel\nid = ", panel.id, ", quantity = ", panel.quantity, "\nTaboo list value",
                      self.taboo_list[panel.id])
                print("\n\n!!!!!")

        for battery in batteries:
            try:
                if battery.quantity != 0:
                    self.taboo_list[battery.id][battery.quantity] += 1
            except KeyError:
                print("\n\n!!!!!")
                print("budget = ", self.internal_budget)
                print("battery\nid = ", battery.id, ", quantity = ", battery.quantity, "\nTaboo list value",
                      )
                print("\n\n!!!!!")

    def check(self, element):
        value = True
        try:
            value = self.taboo_list[element.id][element.quantity] > self.limit
        except KeyError:
            print("Error:\n", "element id ->", element.id, "\nelement quantity -> ", element.quantity, " budget = ",
                  self.internal_budget)
            print("Taboo\n:", self.taboo_list[element.id])

        return value


class ForbiddenAlgorithm:
    def __init__(self, pvs: List[Pv], batteries: List[Battery], budget: int, batteries_area_limit: int,
                 pvs_area_limit: int):
        self.budget = budget
        self.batteries_area_limit = batteries_area_limit
        self.pvs_area_limit = pvs_area_limit
        self.Taboo = Taboo(pvs, batteries, 2, budget)

        self.pvs = pvs
        self.batteries = batteries

        self.current_max_value = - math.inf
        self.pvs_max_value_comb = []
        self.batteries_max_value_comb = []

        self.Zd= 120000 + 100000  # Wh (serwerownia + biuro)
        self.Zn = 120000 + 60000  # Wh (serwerownia + biuro)
        self.cp = 0.00065  # PLN/Wh

    def total_cost(self):
        t_cost = 0
        for p in self.pvs:
            t_cost += p.cost()
        for b in self.batteries:
            t_cost += b.cost()

        return t_cost

    def all_batteries_capacity(self):
        bmax = 0
        for b in self.batteries:
            bmax += b.total_capacity()
        return bmax

    def all_batteries_area(self):
        area = 0
        for b in self.batteries:
            area += b.total_area()
        return area

    def daily_energy_production(self, season):
        sun_power_arg = 1000  # (zima-jesien) 1000
        energy = 0
        i = 0
        for p in self.pvs:
            energy += p.quantity * min(p.power,
                                       p.efficiency * season * sun_power_arg) * 12  # 12 bo przewidujemy że tyle godzin będzie pracował panel
        return energy

    def all_panels_area(self):
        area = 0
        for p in self.pvs:
            area += p.total_area()
        return area

    def still_have_area(self):
        return self.all_batteries_area() <= self.batteries_area_limit and self.all_panels_area() <= self.pvs_area_limit

    def objective_f(self):  # funkcja celu
        # lista stalych parametrow

        etas = 0.7  # % (sprawnosc sprzedazy)
        wcp = 1.05  # Wspolczynnik wzrostu cenny pradu
        season = [0.85, 0.95, 0.85, 0.8]
        Bmax = self.all_batteries_capacity()
        # Wyliczam srednia wazona sprawnosci baterii
        etab = 0
        for b in self.batteries:
            etab += b.total_capacity() * b.efficiency
        try:
            etab /= self.all_batteries_capacity()
        except ZeroDivisionError:
            etab = 1

        daily_income = 0
        for season_eff in season:
            Pt = self.daily_energy_production(season_eff)

            if Pt <= self.Zd:
                daily_income += (Pt - self.Zd) * self.cp - self.Zn * self.cp

            if self.Zd < Pt <= (Bmax + self.Zd):
                daily_income += ((Pt - self.Zd) * etab - self.Zn) * self.cp

            if (self.Zd + Bmax) < Pt:
                daily_income += (Bmax * etab - self.Zn) * self.cp + (Pt - self.Zd - Bmax) * etas * self.cp

        yearly_income = daily_income * (365 / 4)

        # return 20 * yearly_income - self.total_cost()
        return yearly_income * (1 - pow(wcp, 20)) / (1 - wcp) - self.total_cost()

    def find_min(self):
        self.preliminary_opt()
        # print("pvs 1:\n", self.pvs[0].quantity, " z ", len(self.Taboo.taboo_list[self.pvs[0].id].values()))
        # print("pvs 2:\n", self.pvs[1].quantity, " z ", len(self.Taboo.taboo_list[self.pvs[1].id].values()))
        # print("pvs 3:\n", self.pvs[2].quantity, " z ", len(self.Taboo.taboo_list[self.pvs[2].id].values()))
        # print("pvs 4:\n", self.pvs[3].quantity, " z ", len(self.Taboo.taboo_list[self.pvs[3].id].values()))
        while self.pvs[0].cost() <= self.budget and self.still_have_area():
            # print("pvs 1:\n", self.pvs[0].quantity, " z ", len(self.Taboo.taboo_list[self.pvs[0].id].values()))
            while self.total_cost() <= self.budget and self.still_have_area():
                # print("pvs 2:\n", self.pvs[1].quantity, " z ", len(self.Taboo.taboo_list[self.pvs[1].id].values()))

                if self.Taboo.check(self.pvs[1]):
                    self.pvs[1].quantity += 1
                    continue

                while self.total_cost() <= self.budget and self.still_have_area():
                    # print("pvs 2:\n", self.pvs[2].quantity, " z ", len(self.Taboo.taboo_list[self.pvs[2].id].values()))
                    if self.Taboo.check(self.pvs[2]):
                        self.pvs[2].quantity += 1
                        continue

                    while self.total_cost() <= self.budget and self.still_have_area():
                        # print("pvs 3:\n", self.pvs[3].quantity, " z ",
                        #       len(self.Taboo.taboo_list[self.pvs[3].id].values()))
                        if self.Taboo.check(self.pvs[3]):
                            self.pvs[3].quantity += 1
                            continue

                        while self.total_cost() <= self.budget and self.still_have_area():
                            # print("bat 1:\n", self.batteries[0].quantity, " z ",
                            #     len(self.Taboo.taboo_list[self.batteries[0].id].values()))

                            if self.Taboo.check(self.batteries[0]):
                                self.batteries[0].quantity += 1
                                continue

                            while self.total_cost() <= self.budget and self.still_have_area():
                                # print("bat 2:\n", self.batteries[1].quantity, " z ",
                                #      len(self.Taboo.taboo_list[self.batteries[1].id].values()))
                                if self.Taboo.check(self.batteries[1]):
                                    self.batteries[1].quantity += 1
                                    continue

                                while self.total_cost() <= self.budget and self.still_have_area():
                                    # print("bat 3:\n", self.batteries[2].quantity, " z ",
                                    # len(self.Taboo.taboo_list[self.batteries[2].id].values()))
                                    if self.Taboo.check(self.batteries[2]):
                                        self.batteries[2].quantity += 1
                                        continue

                                    curr_value = self.objective_f()
                                    if curr_value > self.current_max_value:
                                        self.current_max_value = copy.deepcopy(curr_value)
                                        self.pvs_max_value_comb = copy.deepcopy(self.pvs)
                                        self.batteries_max_value_comb = copy.deepcopy(self.batteries)
                                    else:
                                        if curr_value < 0.8 * self.current_max_value:
                                            self.Taboo.update(self.pvs, self.batteries)
                                    # print("I was invoke")
                                    self.batteries[2].quantity += 1

                                self.batteries[1].quantity += 1
                                self.batteries[2].quantity = 0

                            self.batteries[0].quantity += 1
                            self.batteries[1].quantity = 0

                        self.pvs[3].quantity += 1
                        self.batteries[0].quantity = 0

                    self.pvs[2].quantity += 1
                    self.pvs[3].quantity = 0

                self.pvs[1].quantity += 1
                self.pvs[2].quantity = 0

            self.pvs[0].quantity += 1
            self.pvs[1].quantity = 0

        self.pvs[0].quantity = 0
        return self.current_max_value, self.pvs_max_value_comb, self.batteries_max_value_comb

    def inspect_pvs(self, pv_n=0):

        if pv_n > (len(self.pvs) - 1):
            # print("Inspect battery run")
            self.inspect_battery()
            self.batteries[0].quantity = 0
            # if pv_n < (len(self.pvs) - 1):
            #     self.pvs[pv_n + 1].quantity = 0
        else:
            while self.total_cost() <= self.budget and self.still_have_area():
                # print("In loop pv_n = ", pv_n, "\n\n")
                self.inspect_pvs(pv_n + 1)
                self.pvs[pv_n].quantity += 1
                if pv_n < (len(self.pvs) - 1):
                    self.pvs[pv_n + 1].quantity = 0

                while self.total_cost() <= self.budget and self.Taboo.check(self.pvs[pv_n]):
                    self.pvs[pv_n].quantity += 1

        return True

    def inspect_battery(self, bat_n=0):

        if bat_n > (len(self.batteries) - 1):
            # print("Max counted")
            curr_value = self.objective_f()
            if curr_value > self.current_max_value:
                self.current_max_value = curr_value
                self.pvs_max_value_comb = copy.deepcopy(self.pvs)
                self.batteries_max_value_comb = copy.deepcopy(self.batteries)
            else:
                if curr_value < 0.8 * self.current_max_value:
                    self.Taboo.update(self.pvs, self.batteries)
            return True
        else:
            # print(" Before loop batteries\nbatn = ", bat_n, "  batn quantity = ", self.batteries[bat_n].quantity,"\n\n")

            while self.total_cost() <= self.budget and self.still_have_area():
                # print(" In loop batteries\nbatn = ", bat_n, "  batn quantity = ", self.batteries[bat_n].quantity)
                self.inspect_battery(bat_n + 1)
                self.batteries[bat_n].quantity += 1
                if bat_n < (len(self.batteries) - 1):
                    self.batteries[bat_n + 1].quantity = 0

                if self.Taboo.check(self.batteries[bat_n]):
                    self.batteries[bat_n].quantity = 0  # niekoniecznie potrzebne
                    if bat_n < (len(self.batteries) - 1):
                        self.batteries[bat_n + 1].quantity = 0
                    return False

    def find_min_v2(self):
        self.preliminary_opt()
        self.inspect_pvs()
        # program działa na referencjach obiektów, by uniknąć problemów przy działaniu w pętli musimy przywrócić obiekty do stanu początkowego
        self.pvs[0].quantity = 0
        return self.current_max_value, self.pvs_max_value_comb, self.batteries_max_value_comb

    # noinspection DuplicatedCode
    def preliminary_opt(self):
        for pv_checked in self.pvs:
            for pv_compared in self.pvs:
                if pv_checked.price > pv_compared.price and pv_checked.power <= pv_compared.power \
                        and pv_checked.efficiency <= pv_compared.efficiency and pv_checked.area <= pv_compared.area:
                    for key, value in self.Taboo.taboo_list[pv_checked.id].items():
                        if key != 0:
                            self.Taboo.taboo_list[pv_checked.id][key] = math.inf

        for bat_checked in self.batteries:
            for bat_compared in self.batteries:
                if bat_checked.price > bat_compared.price and bat_checked.capacity <= bat_compared.capacity \
                        and bat_checked.efficiency <= bat_checked.efficiency and bat_checked.area <= bat_compared.area:
                    for key, value in self.Taboo.taboo_list[bat_checked.id].items():
                        if key != 0:
                            self.Taboo.taboo_list[bat_checked.id][key] = math.inf



