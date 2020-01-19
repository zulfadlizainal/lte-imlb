# Created by github.com/zulfadlizainal

import pandas as pd
import numpy as np

# Import Data
data = pd.read_excel('Input_Data.xlsx', encoding='utf-8')
param = pd.read_excel('Input_Parameter.xlsx', encoding='utf-8')
note = pd.read_excel('Notes.xlsx', encoding='utf-8')

# Change Parameter to Dictionary
temp = param
temp.drop(columns=['Formula'], inplace=True)
param_dict = temp.set_index('Parameter').T.to_dict('list')
del temp

print('\n####################################################################\n')
print('Inter Freq Load Balancing Simulation - Through Reselection Parameter')
print('\n####################################################################\n')

# Band Variable
B1st = param.columns[1]
B2nd = param.columns[2]
Equal = "Equal Priority"
LowtoHigh = "Low to High"
HightoLow = "High to Low"

# 1st to 2nd band priority condition
if param_dict['SIB3_cellReselectionPriority'][0] == param_dict['SIB5_cellReselectionPriority'][0]:
    B1st_to_B2nd = Equal
elif param_dict['SIB3_cellReselectionPriority'][0] < param_dict['SIB5_cellReselectionPriority'][0]:
    B1st_to_B2nd = LowtoHigh
elif param_dict['SIB3_cellReselectionPriority'][0] > param_dict['SIB5_cellReselectionPriority'][0]:
    B1st_to_B2nd = HightoLow

# 2nd to 1st band priority condition
if param_dict['SIB3_cellReselectionPriority'][1] == param_dict['SIB5_cellReselectionPriority'][1]:
    B2nd_to_B1st = Equal
elif param_dict['SIB3_cellReselectionPriority'][1] < param_dict['SIB5_cellReselectionPriority'][1]:
    B2nd_to_B1st = LowtoHigh
elif param_dict['SIB3_cellReselectionPriority'][1] > param_dict['SIB5_cellReselectionPriority'][1]:
    B2nd_to_B1st = HightoLow

# Simulate 1st Band (RP Parameter)
data_B1st = data.copy()
search = pd.Series([])
decide = pd.Series([])
result = pd.Series([])

if B1st_to_B2nd == HightoLow:

    sNonIntraSearchP = param_dict['SIB1_q-RxLevMin'][0] + param_dict['SIB3_s-NonIntraSearchP'][0]

    #Create Search Criteria
    index = 0
    for index in range(len(data_B1st)):

        if data_B1st[f'{B1st}_RSRP (dBm)'][index] < sNonIntraSearchP:
            search[index] = 1
        else:
            search[index] = 0

    data_B1st['Search'] = search

    #Create Decision Criteria
    index = 0
    for index in range(len(data_B1st)):

        if (data_B1st[f'{B2nd}_RSRP (dBm)'][index] - param_dict['SIB5_q-OffsetFreq'][0]) > (data_B1st[f'{B1st}_RSRP (dBm)'][index] + param_dict['SIB3_q-Hyst'][0]):
            decide[index] = 1
        else:
            decide[index] = 0

    data_B1st['Decision'] = decide

    #Result
    index = 0
    for index in range(len(data_B1st)):

        if data_B1st['Search'][index] + data_B1st['Decision'][index] == 2:
            result[index] = f'Move to {B2nd}'
        elif data_B1st['Search'][index] == 1:
            result[index] = 'Search Only'
        else:
            result[index] = 'Not Searching'

        data_B1st['Result'] = result

print(' ')
print('ありがとうございました！！')
print('Download this program: https://github.com/zulfadlizainal')
print('Author: https://www.linkedin.com/in/zulfadlizainal')
print(' ')
