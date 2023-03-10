from src.idealGasValues.cp_values import *

T1 = 450
T2 = 650


cp_av = (Cp_ave_Air(T1) + Cp_ave_Air(T2)) / 2  # [kJ/(kg K)]
dh = h_ave_Air(T2) - h_ave_Air(T1)  # [kJ/kg]
Q12_ans = cp_av * (T2-T1)  # [kJ/kg]