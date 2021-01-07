import time
import unittest
from ClassesReqByAlgorithm import Battery
from ClassesReqByAlgorithm import ForbiddenAlgorithm
from ClassesReqByAlgorithm import Pv
from Unit_tests.test_scenarios import Scenarios


class TestForbiddenAlg(unittest.TestCase):
    def test_alg_v1_correctness_on_predefined_scenarios(self):

        area_batteries = 1500
        area_pvs = 1500
        budget = 100000

        sol_best_case = ForbiddenAlgorithm(Scenarios().p_best_case, Scenarios().b_best_case, budget, area_batteries,
                                           area_pvs).find_min()
        sol_worst_case = ForbiddenAlgorithm(Scenarios().p_worst_case, Scenarios().b_worst_case, budget, area_batteries,
                                            area_pvs).find_min()
        sol_real_case = ForbiddenAlgorithm(Scenarios().p_based_on_data, Scenarios().b_based_on_data, budget,
                                           area_batteries,
                                           area_pvs).find_min()

        assert sol_best_case[0] == sol_worst_case[0] == sol_real_case[0] == -1714968.725

    def test_alg_v2_correctness_on_predefined_scenarios(self):

        area_batteries = 1500
        area_pvs = 1500
        budget = 100000

        sol_best_case = ForbiddenAlgorithm(Scenarios().p_best_case, Scenarios().b_best_case, budget, area_batteries,
                                           area_pvs).find_min_v2()
        sol_worst_case = ForbiddenAlgorithm(Scenarios().p_worst_case, Scenarios().b_worst_case, budget, area_batteries,
                                            area_pvs).find_min_v2()
        sol_real_case = ForbiddenAlgorithm(Scenarios().p_based_on_data, Scenarios().b_based_on_data, budget,
                                           area_batteries,
                                           area_pvs).find_min_v2()

        assert sol_best_case[0] == sol_worst_case[0] == sol_real_case[0] == -1714968.725

    def test_return_same_solution(self):
        area_pvs = 1500
        area_batteries = 200

        for budget in range(1000, 1000, 10000):
            pvs = Scenarios().get_panel_set()
            battery = Scenarios().get_panel_set()
            sol_v1 = ForbiddenAlgorithm(pvs, battery, budget, area_batteries, area_pvs).find_min()
            sol_v2 = ForbiddenAlgorithm(pvs, battery, budget, area_batteries, area_pvs).find_min_v2()
            for i in range(len(pvs)):
                assert sol_v2[1][i].quantity == sol_v1[1][i].quantity
            for i in range(len(battery)):
                assert sol_v2[2][i].quantity == sol_v1[2][i].quantity
            assert sol_v1[0] == sol_v2[0]

    def test_optimisation(self):
        # inicjalizacja typow paneli
        p1 = Pv(11, 4900, 3100, 0.3, 1.5)  # cena jest druga
        p2 = Pv(12, 7000, 3100, 0.3, 1.5)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
        p3 = Pv(13, 1680, 3100, 0.3, 1.5)
        p4 = Pv(14, 7000, 3100, 0.3, 1.5)
        # inicjalizacja typow akumulatorow
        b1 = Battery(21, 20000, 10000, 0.85,
                     1)  # def __init__(self, id, price, capacity, efficiency, area, quantity=0):
        b2 = Battery(22, 18000, 7000, 0.85, 1)
        b3 = Battery(23, 19200, 12000, 0.85, 1)

        # Budżet

        Pvs1 = [p1, p2, p3, p4]
        batteries1 = [b1, b2, b3]

        budget = 50000
        area_pvs = 1500
        area_batteries = 200

        # v1 nie jest zopymalizowany -> stąd długi czas działania
        alg = ForbiddenAlgorithm(Scenarios().p_best_case, Scenarios().b_best_case, budget, area_batteries, area_pvs)
        start_v1 = time.time()
        for i in range(10):
            alg.find_min()
        end_v1 = time.time()
        time_v1 = end_v1 - start_v1
        start_v2 = time.time()

        for i in range(10):
            alg.find_min_v2()
        end_v2 = time.time()
        time_v2 = end_v2 - start_v2

        assert time_v2 <= time_v1


if __name__ == "__main__":
    unittest.main()
    print("All tests were passed")
