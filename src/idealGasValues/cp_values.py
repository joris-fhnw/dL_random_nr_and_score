''' This calculates the average mass-specific heat capacities of main combustion exhaust gases'''

import numpy as np
import pandas as pd
from matplotlib.pyplot import Subplot
from scipy.interpolate import interp1d
import os

path = os.path.dirname(__file__)
excel_name = "Thd Skript Anhang Tabelle A-07.3 Rev07.xlsx"
total_path1 = path +"/" +excel_name
df1 = pd.read_excel(total_path1, sheet_name='a73_Air')
T1 = np.array(df1['T'])
Cp_Air = np.array(df1['Cp'])
# Cp_N2s = np.array(df1['N2*'])
# Cp_N2 = np.array(df1['N2'])
# Cp_O2 = np.array(df1['O2'])
# Cp_CO2 = np.array(df1['CO2'])
# Cp_H2O = np.array(df1['H2O'])
# Cp_SO2 = np.array(df1['SO2'])


# Interpolating data from the data in table
def Cp_ave_Air(t_value):
    Cp_value = interp1d(T1, Cp_Air)
    return Cp_value(t_value)

excel_name2 = "Thd Skript Anhang Tabelle A-07.1 Rev07.xlsx"
total_path2 = path +"/" +excel_name2
df2 = pd.read_excel(total_path2, sheet_name='A-7.1')
T2 = np.array(df2['T'])
h2 = np.array(df2['h'])

def h_ave_Air(t_value):
    h_value = interp1d(T2, h2)
    return h_value(t_value)

# def Cp_ave_N2s(t_value):
#     Cp_value = interp1d(t1, Cp_N2s)
#     return Cp_value(t_value)
#
#
# def Cp_ave_N2(t_value):
#     Cp_value = interp1d(t1, Cp_N2)
#     return Cp_value(t_value)
#

# def Cp_ave_O2(t_value):
#     Cp_value = interp1d(t1, Cp_O2)
#     return Cp_value(t_value)
#
#
# def Cp_ave_CO2(t_value):
#     Cp_value = interp1d(t1, Cp_CO2)
#     return Cp_value(t_value)
#
#
# def Cp_ave_H2O(t_value):
#     Cp_value = interp1d(t1, Cp_H2O)
#     return Cp_value(t_value)
#
#
# def Cp_ave_SO2(t_value):
#     Cp_value = interp1d(t1, Cp_SO2)
#     return Cp_value(t_value)
#
#
# df2 = pd.read_excel('./static/data.xlsx', sheet_name='A-8.2')
# t2 = np.array(df2['T (°C)'])
# s_Air = np.array(df2['Air'])
# s_N2s = np.array(df2['N2*'])
# s_N2 = np.array(df2['N2'])
# s_O2 = np.array(df2['O2'])
# s_CO2 = np.array(df2['CO2'])
# s_H2O = np.array(df2['H2O'])
# s_SO2 = np.array(df2['SO2'])
#
#
# # Interpolating data from the data in table
# def s_abs_Air(t_value):
#     s_abs_value = interp1d(t2, s_Air)
#     return s_abs_value(t_value)
#
#
# def s_abs_N2s(t_value):
#     s_abs_value = interp1d(t2, s_N2s)
#     return s_abs_value(t_value)
#
#
# def s_abs_N2(t_value):
#     s_abs_value = interp1d(t2, s_N2)
#     return s_abs_value(t_value)
#
#
# def s_abs_O2(t_value):
#     s_abs_value = interp1d(t2, s_O2)
#     return s_abs_value(t_value)
#
#
# def s_abs_CO2(t_value):
#     s_abs_value = interp1d(t2, s_CO2)
#     return s_abs_value(t_value)
#
#
# def s_abs_H2O(t_value):
#     s_abs_value = interp1d(t2, s_H2O)
#     return s_abs_value(t_value)
#
#
# def s_abs_SO2(t_value):
#     s_abs_value = interp1d(t2, s_SO2)
#     return s_abs_value(t_value)
#
#
# # Plotting the data and comparing (starting always from 0 °C)
# temps = np.linspace(-60, 2200, 200)  # the range of data is -60 °C  to 2'200 °C
#
#
# def Cp_ave_plot(plt: Subplot):
#     plt.plot(temps, Cp_ave_Air(temps), label='Cp_ave_Air')
#     plt.plot(temps, Cp_ave_N2s(temps), label='Cp_ave_N2*')
#     plt.plot(temps, Cp_ave_N2(temps), label='Cp_ave_N2')
#     plt.plot(temps, Cp_ave_O2(temps), label='Cp_ave_O2')
#     plt.plot(temps, Cp_ave_CO2(temps), label='Cp_ave_CO2')
#     plt.plot(temps, Cp_ave_H2O(temps), label='Cp_ave_H2O')
#     plt.plot(temps, Cp_ave_SO2(temps), label='Cp_ave_SO2')
#
#     plt.title('Cp_averages from 0 °C to t(°C)')
#     plt.xlabel('Final Temperature [deg C]')
#     plt.ylabel('Cp_ave in kJ/(kg K)')
#     plt.legend(loc='best')
#     plt.grid()
#     plt.show()
