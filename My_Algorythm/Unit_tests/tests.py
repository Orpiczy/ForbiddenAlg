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

        assert round(sol_best_case[0], 2) == -2802903.29
        assert round(sol_worst_case[0], 2) == -2895465.24
        assert round(sol_real_case[0], 2) == -2895465.24

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

        assert round(sol_best_case[0], 2) == -2802903.29
        assert round(sol_worst_case[0], 2) == -2895465.24
        assert round(sol_real_case[0], 2) == -2895465.24

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
        area_pvs = 1500
        area_batteries = 200

        # v1 nie jest zopymalizowany -> stąd długi czas działania
        for budget in range(5000, 1000, 50000):
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

        for budget in range(5000, 1000, 50000):
            alg = ForbiddenAlgorithm(Scenarios().p_based_on_data, Scenarios().b_based_on_data, budget, area_batteries,
                                     area_pvs)
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


# area_batteries = 1500
# area_pvs = 1500
# budget = 100000
#
# sol_best_case = ForbiddenAlgorithm(Scenarios().p_best_case, Scenarios().b_best_case, budget, area_batteries,
#                                    area_pvs).find_min_v2()
# sol_worst_case = ForbiddenAlgorithm(Scenarios().p_worst_case, Scenarios().b_worst_case, budget, area_batteries,
#                                     area_pvs).find_min_v2()
# sol_real_case = ForbiddenAlgorithm(Scenarios().p_based_on_data, Scenarios().b_based_on_data, budget,
#                                    area_batteries,
#                                    area_pvs).find_min_v2()
#
# print(sol_best_case[0],sol_worst_case[0],sol_real_case[0] )

if __name__ == "__main__":
    unittest.main()
    print("All tests were passed")
