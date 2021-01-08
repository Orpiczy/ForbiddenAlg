# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:59:58 2021

@author: sucho
"""
    
import ClassesReqByAlgorithm as backend
from timeit import timeit
import matplotlib.pyplot as plt

############################################ BUDZET ##########################################################################

#REPEAT_NUM = 100
##print("Test wplywu wysokosci budzetu na czas realizacji algorytmu:")
#SETUP_CODE = '''
#import ClassesReqByAlgorithm as backend
#p1 = backend.Pv(11, 4900, 3100, 0.4, 1.5)  # cena jest druga
#p2 = backend.Pv(12, 7000, 3100, 0.5, 1.5)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
#p3 = backend.Pv(13, 1680, 3100, 0.2, 1.5)
#p4 = backend.Pv(14, 7000, 3100, 0.3, 1.5)
#
#b1 = backend.Battery(21, 20000, 10000, 0.85, 1)  # def __init__(self, id, price, capacity, efficiency, area, quantity=0):
#b2 = backend.Battery(22, 18000, 7000, 0.85, 1)
#b3 = backend.Battery(23, 19200, 12000, 0.85, 1)
#
#Pvs = [p1, p2, p3, p4]
#batteries = [b1, b2, b3]
#'''
#
#TEST_CODEp1 = '''
#alg = backend.ForbiddenAlgorithm(Pvs[:], batteries[:],
#'''
#TEST_CODEp2 = ''' , 200, 300)
#alg.Zd = 100000
#alg.Zn = 100000
#alg.cp = 0.00067
#solution = alg.find_min_v2()
#'''
#
#x_budget = [1000, 10000, 100000, 1000000, 10000000, 100000000]
#y_budget = [timeit(setup = SETUP_CODE ,stmt = TEST_CODEp1 + str(b) +TEST_CODEp2, number = REPEAT_NUM)/REPEAT_NUM for b in x_budget]
#
#plt.plot(x_budget, y_budget, 'o-')
#plt.title("Test wplywu wysokosci budzetu na czas realizacji algorytmu:")
#plt.xlabel('Budzet [zl]')
#plt.ylabel('Czas [s]')
#plt.yscale('log')
#plt.xscale('log')
#plt.show()
#
################################# ILOSC PANELI ########################################

#REPEAT_NUM = 100
#SETUP_CODE = '''
#import ClassesReqByAlgorithm as backend
#p1 = backend.Pv(11, 4900, 3100, 0.4, 1.5)  # cena jest druga
#p2 = backend.Pv(12, 7000, 3100, 0.5, 1.5)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
#p3 = backend.Pv(13, 1680, 3100, 0.2, 1.5)
#p4 = backend.Pv(14, 7000, 3100, 0.3, 1.5)
#p5 = backend.Pv(15, 4600, 3100, 0.45, 1.5)  
#p6 = backend.Pv(16, 8000, 3100, 0.58, 1.5)  
#p7 = backend.Pv(17, 1900, 3100, 0.25, 1.5)
#p8 = backend.Pv(18, 6500, 3100, 0.33, 1.5)
#p9 = backend.Pv(19, 5300, 3100, 0.31, 1.5)
#p10 = backend.Pv(110, 1800, 3100, 0.24, 1.5)
#p11 = backend.Pv(111, 6800, 3100, 0.35, 1.5)
#p12 = backend.Pv(112, 5500, 3100, 0.32, 1.5)
#
#b1 = backend.Battery(21, 20000, 10000, 0.85, 1)  # def __init__(self, id, price, capacity, efficiency, area, quantity=0):
#b2 = backend.Battery(22, 18000, 7000, 0.85, 1)
#b3 = backend.Battery(23, 19200, 12000, 0.85, 1)
#
#Pvs = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
#batteries = [b1, b2, b3]
#'''
#
#TEST_CODEp1 = '''
#alg = backend.ForbiddenAlgorithm(Pvs[0:
#'''
#TEST_CODEp2 = '''], batteries[:] ,1000000 , 200, 300)
#alg.Zd = 100000
#alg.Zn = 100000
#alg.cp = 0.00067
#solution = alg.find_min_v2()
#'''
#
#x_pvs = [i for i in range(1, 13)]
#y_pvs= [timeit(setup = SETUP_CODE ,stmt = TEST_CODEp1 + str(i) + TEST_CODEp2, number = REPEAT_NUM)/REPEAT_NUM for i in x_pvs]
#
#plt.plot(x_pvs, y_pvs, 'o-')
#plt.title("Test wplywu ilosci typow paneli na czas realizacji algorytmu:")
#plt.xlabel('Ilosc typow paneli')
#plt.ylabel('Czas [s]')
##plt.yscale('log')
##plt.xscale('log')
#plt.show()

################################### ILOSC BATERII #################################################
#
########## TEMP ###############


########## /TEMP ##########
REPEAT_NUM = 100
SETUP_CODE = '''
import ClassesReqByAlgorithm as backend
p1 = backend.Pv(11, 4900, 3100, 0.4, 1.5)  # cena jest druga
p2 = backend.Pv(12, 7000, 3100, 0.5, 1.5)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
p3 = backend.Pv(13, 1680, 3100, 0.2, 1.5)
p4 = backend.Pv(14, 7000, 3100, 0.3, 1.5)
p4 = backend.Pv(14, 7000, 3100, 0.3, 1.5)


b1 = backend.Battery(21, 20000, 10000, 0.85, 1)  # def __init__(self, id, price, capacity, efficiency, area, quantity=0):
b2 = backend.Battery(22, 18000, 7000, 0.85, 1)
b3 = backend.Battery(23, 19200, 12000, 0.85, 1)
b4 = backend.Battery(24, 21000, 11000, 0.85, 1)  
b5 = backend.Battery(25, 19000, 8000, 0.85, 1)
b6 = backend.Battery(26, 21000, 13000, 0.85, 1)
b7 = backend.Battery(27, 17000, 90000, 0.85, 1)  
b8 = backend.Battery(28, 16000, 6000, 0.85, 1)
b9 = backend.Battery(29, 25000, 15000, 0.85, 1)

Pvs = [p1, p2, p3, p4]
batteries = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
'''

TEST_CODEp1 = '''
alg = backend.ForbiddenAlgorithm(Pvs[:], batteries[0:
'''
TEST_CODEp2 = '''] ,1000000 , 200, 300)
alg.Zd = 100000
alg.Zn = 100000
alg.cp = 0.00067
solution = alg.find_min_v2()
'''

x_batt = [i for i in range(1, 9)]
y_batt = [timeit(setup = SETUP_CODE ,stmt = TEST_CODEp1 + str(i) + TEST_CODEp2, number = REPEAT_NUM)/REPEAT_NUM for i in x_batt]

plt.plot(x_batt, y_batt, 'o-')
plt.title("Test wplywu ilosci typow baterii na czas realizacji algorytmu:")
plt.xlabel('Ilosc typow baterii')
plt.ylabel('Czas [s]')
plt.ylim(0, max(y_batt)*1.05)
#plt.yscale('log')
#plt.xscale('log')
plt.show()

################################ POWIERZCHNIA PIWNICY ########################################
#REPEAT_NUM = 100
#SETUP_CODE = '''
#import ClassesReqByAlgorithm as backend
#p1 = backend.Pv(11, 4900, 3100, 0.4, 1.5)  # cena jest druga
#p2 = backend.Pv(12, 7000, 3100, 0.5, 1.5)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
#p3 = backend.Pv(13, 1680, 3100, 0.2, 1.5)
#p4 = backend.Pv(14, 7000, 3100, 0.3, 1.5)
#
#b1 = backend.Battery(21, 20000, 10000, 0.85, 1)  # def __init__(self, id, price, capacity, efficiency, area, quantity=0):
#b2 = backend.Battery(22, 18000, 7000, 0.85, 1)
#b3 = backend.Battery(23, 19200, 12000, 0.85, 1)
#
#Pvs = [p1, p2, p3, p4]
#batteries = [b1, b2, b3]
#'''
#
#TEST_CODEp1 = '''
#alg = backend.ForbiddenAlgorithm(Pvs[:], batteries[:] ,1000000 ,
#'''
#TEST_CODEp2 = ''', 300)
#alg.Zd = 100000
#alg.Zn = 100000
#alg.cp = 0.00067
#solution = alg.find_min_v2()
#'''
#
#x_blim = [1, 25, 50, 100, 150, 200, 500, 1000, 1500, 2000]
#y_blim = [timeit(setup = SETUP_CODE ,stmt = TEST_CODEp1 + str(i) + TEST_CODEp2, number = REPEAT_NUM)/REPEAT_NUM for i in x_blim]
#
#plt.plot(x_blim, y_blim, 'o-')
#plt.title("Test wplywu powierzchni piwnicy na czas realizacji algorytmu:")
#plt.xlabel('Powierzchnia dachu [m^2]')
#plt.ylabel('Czas [s]')
#plt.ylim(0, max(y_blim)*1.05)
##plt.yscale('log')
##plt.xscale('log')
#plt.show()

################################ POWIERZCHNIA DACHU ########################################
#REPEAT_NUM = 100
#
#SETUP_CODE = '''
#import ClassesReqByAlgorithm as backend
#p1 = backend.Pv(11, 4900, 3100, 0.4, 1.5)  # cena jest druga
#p2 = backend.Pv(12, 7000, 3100, 0.5, 1.5)  # def __init__(self, id, price, power, efficiency, area, quantity=0):
#p3 = backend.Pv(13, 1680, 3100, 0.2, 1.5)
#p4 = backend.Pv(14, 7000, 3100, 0.3, 1.5)
#
#b1 = backend.Battery(21, 20000, 10000, 0.85, 1)  # def __init__(self, id, price, capacity, efficiency, area, quantity=0):
#b2 = backend.Battery(22, 18000, 7000, 0.85, 1)
#b3 = backend.Battery(23, 19200, 12000, 0.85, 1)
#
#Pvs = [p1, p2, p3, p4]
#batteries = [b1, b2, b3]
#'''
#TEST_CODEp1 = '''
#alg = backend.ForbiddenAlgorithm(Pvs[:], batteries[:] ,1000000 , 200, 
#'''
#TEST_CODEp2 = ''')
#alg.Zd = 100000
#alg.Zn = 100000
#alg.cp = 0.00067
#solution = alg.find_min_v2()
#'''
#
#x_plim = [25, 50, 100, 200, 500, 1000, 2000, 5000]
#y_plim = [timeit(setup = SETUP_CODE ,stmt = TEST_CODEp1 + str(i) + TEST_CODEp2, number = REPEAT_NUM)/REPEAT_NUM for i in x_plim]
#
#plt.plot(x_plim, y_plim, 'o-')
#plt.title("Test wplywu powierzchni dachu na czas realizacji algorytmu:")
#plt.xlabel('Powierzchnia dachu [m^2]')
#plt.ylabel('Czas [s]')
#plt.ylim(0, max(y_plim)*1.05)
##plt.yscale('log')
##plt.xscale('log')
#plt.show()