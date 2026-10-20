#!/usr/bin/env python3

from statistics import mean
import math

# fuctions to perform final calculation for each experiment
def HBT(AB, A, B, del_t, time):
    results = []
    for x in range(0, 10):
        results.append((AB[x] * time)/(A[x] * B[x] * 2 * del_t))
    return results

def GRA(TAB, T, TA, TB):
    results = []
    for x in range(0, 10):
        results.append((TAB[x] * T[x])/(TA[x] * TB[x]))
    return results

def GRA_classical(TAB, T, TA, TB):
    results = []
    for x in range(0, 10):
        results.append((TAB[x] * T[x])/(TA[x] * TB[x]))
    return results
    
# experiment 1
count_A = [1028632, 1026800, 1022937, 1025892, 1024544, 1023111, 1022019, 1020066, 1021585, 1019796]
count_B = [753488, 753725, 748970, 748204, 750669, 748797, 749597, 748158, 749049, 747417]
count_A_B = [388, 379, 369, 435, 391, 389, 370, 411, 389, 392]

result_1 = HBT(count_A_B, count_A, count_B, (5*10**-9), 20)

# experiment 2
counts_t = [1505239, 1508031, 1509448, 1495864, 1500528, 1495796, 1494356, 1494065, 1500234, 1504801]
counts_a = [1042761, 1043370, 1045058, 1037919, 1040268, 1035167, 1032711, 1036984, 1036061, 1041598]
counts_b = [758917, 759613, 762884, 757315, 757992, 757290, 758568, 755535, 755327, 758602]
counts_ta = [80814, 80294, 81184, 81527, 80711, 81172, 81403, 81806, 81570, 81359]
counts_tb = [36681, 36955, 37173, 37320, 36584, 37355, 37021, 37287, 37461, 37345]
counts_tab = [50, 50, 51, 48, 50, 43, 37, 54, 43, 54]

result_2 = GRA(counts_tab, counts_t, counts_ta, counts_tb)

# experiment 3
counts_t = [3595636, 3604018, 3600315, 3609193, 3600368, 3604836, 3598179, 3602848, 3603653, 3604810]
counts_a = [2313457, 2309615, 2315073, 2318235, 2311729, 2308441, 2311456, 2310247, 2310983, 2309094]
counts_b = [1901478, 1903475, 1902387, 1906215, 1902472, 1901823, 1899047, 1902258, 1904203, 1903486]
counts_ta = [4136, 4079, 4282, 4200, 4234, 4233, 4093, 4118, 4152, 4107]
counts_tb = [3493, 3451, 3390, 3414, 3477, 3331, 3497, 3494, 3425, 3481]
counts_tab = [7, 3, 2, 3, 6, 3, 2, 4, 6, 6]

result_3 = GRA_classical(counts_tab, counts_t, counts_ta, counts_tb)

# calcualting the mean of all the runs
mean_1 = mean(result_1)
mean_2 = mean(result_2)
mean_3 = mean(result_3)

# calculating standard deviation for statistical uncertainty
N = 10
squared_deviations_1 = 0
for x in result_1:
    squared_deviations_1 += ((x-mean_1)**2)
s_1 = math.sqrt(squared_deviations_1 / (N - 1))

squared_deviations_2 = 0
for x in result_2:
    squared_deviations_2 += ((x-mean_2)**2)
s_2 = math.sqrt(squared_deviations_2 / (N - 1))

squared_deviations_3 = 0
for x in result_3:
    squared_deviations_3 += ((x-mean_3)**2)
s_3 = math.sqrt(squared_deviations_3 / (N - 1))



# rounding to two significant figures
mean_1 = round(mean_1, 3)
mean_2 = round(mean_2, 3)
mean_3 = round(mean_3, 3)
s_1 = round(s_1, 3)
s_2 = round(s_2, 3)
s_3 = round(s_3, 3)

print(f"HBT Result: {mean_1} +/- {s_1}")
print(f"GRA Result: {mean_2} +/- {s_2}")
print(f"GRA Classial Result: {mean_3} +/- {s_3}")
