from ClassesReqByAlgorithm import Pv, Battery
from random import randint


# generator zadań testowych

class Scenarios:
    def __init__(self):
        # all panels are viable
        pv1 = Pv(11, 5100, 3100, 0.22, 1.5)  # cena jest druga
        pv2 = Pv(12, 6530, 4000, 0.27, 1.5)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
        pv3 = Pv(13, 7800, 4500, 0.11, 1.5)
        pv4 = Pv(14, 9000, 4600, 0.16, 1.5)
        self.p_worst_case = [pv1, pv2, pv3, pv4]

        # all batteries are viable
        # def __init__(self, id, price, capacity, efficiency, area, quantity=0):
        bv1 = Battery(21, 21000, 12000, 0.82, 1)
        bv2 = Battery(22, 17500, 7000, 0.80, 1)
        bv3 = Battery(23, 19000, 10000, 0.85, 1)
        self.b_worst_case = [bv1, bv2, bv3]

        # panels based on data
        p1 = Pv(11, 5100, 3100, 0.22, 1.5)  # cena jest druga
        p2 = Pv(12, 6530, 4000, 0.27, 1.5)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
        p3 = Pv(13, 7800, 4500, 0.11, 1.5)
        p4 = Pv(14, 9000, 4600, 0.16, 1.5)
        self.p_based_on_data = [p1, p2, p3, p4]

        # batteries based on data
        b1 = Battery(21, 21000, 10000, 0.82, 1)
        b2 = Battery(22, 17500, 7000, 0.80, 1)
        b3 = Battery(23, 19000, 12000, 0.85, 1)
        self.b_based_on_data = [b1, b2, b3]

        # best case scenario - only one battery is viable
        p1 = Pv(11, 5100, 3610, 0.28, 1.2)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
        p2 = Pv(12, 6530, 3000, 0.27, 1.5)
        p3 = Pv(13, 7800, 3500, 0.11, 1.5)
        p4 = Pv(14, 9000, 3600, 0.16, 1.5)
        self.p_best_case = [p1, p2, p3, p4]

        # only one battery is viable
        # def __init__(self, id, price, capacity, efficiency, area, quantity=0):
        bv1 = Battery(21, 21000, 9000, 0.82, 1)
        bv2 = Battery(22, 17500, 11000, 0.80, 1)
        bv3 = Battery(23, 19000, 10000, 0.85, 1)
        self.b_best_case = [bv1, bv2, bv3]

        self.p_all_cases = [self.p_worst_case, self.p_based_on_data, self.p_best_case]
        self.b_all_cases = [self.b_worst_case, self.b_based_on_data, self.b_best_case]

    def get_panel_set(self):
        return self.p_all_cases[randint(0, len(self.p_all_cases) - 1)]

    def get_battery_set(self):
        return self.b_all_cases[randint(0, len(self.b_all_cases) - 1)]

    @staticmethod  # all param are <0,1>
    def gen_panel_set_over_years(price_decrease: float, power_increase: float, eff_increase: float,
                                 size_decrease: float):
        p1 = Pv(11, 5100 * (1 - price_decrease), 3100 * (1 + power_increase), 0.22 * (1 + eff_increase),
                1.5 * (1 - size_decrease))
        p2 = Pv(12, 6530 * (1 - price_decrease), 4000 * (1 + power_increase), 0.27 * (1 + eff_increase),
                1.5 * (1 - size_decrease))
        p3 = Pv(13, 7800 * (1 - price_decrease), 4500 * (1 + power_increase), 0.11 * (1 + eff_increase),
                1.5 * (1 - size_decrease))
        p4 = Pv(14, 9000 * (1 - price_decrease), 4600 * (1 + power_increase), 0.16 * (1 + eff_increase),
                1.5 * (1 - size_decrease))
        return [p1, p2, p3, p4]

    @staticmethod
    def gen_batteries_set_over_years(price_decrease: float, capacity_increase: float, eff_increase: float,
                                     size_decrease: float):
        b1 = Battery(21, 21000 * (1 - price_decrease), 10000 * (1 + capacity_increase), 0.82 * (1 + eff_increase),
                     1 * (1 + size_decrease))
        b2 = Battery(22, 17500 * (1 - price_decrease), 7000 * (1 + capacity_increase), 0.80 * (1 + eff_increase),
                     1 * (1 + size_decrease))
        b3 = Battery(23, 19000 * (1 - price_decrease), 12000 * (1 + capacity_increase), 0.85 * (1 + eff_increase),
                     1 * (1 + size_decrease))
        return [b1, b2, b3]
