# Created by github.com/zulfadlizainal

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()

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


#Equal Priority
if B1st_to_B2nd == Equal:

    sNonIntraSearchP = param_dict['SIB1_q-RxLevMin'][0] + \
        param_dict['SIB3_s-NonIntraSearchP'][0]

    # Create Search Criteria
    index = 0
    for index in range(len(data_B1st)):

        if data_B1st[f'{B1st}_RSRP (dBm)'][index] < sNonIntraSearchP:
            search[index] = 1
        else:
            search[index] = 0

    data_B1st['Search'] = search

    # Create Decision Criteria
    index = 0
    for index in range(len(data_B1st)):

        if (data_B1st[f'{B2nd}_RSRP (dBm)'][index] > (data_B1st[f'{B1st}_RSRP (dBm)'][index] + param_dict['SIB3_q-Hyst'][0] + param_dict['SIB5_q-OffsetFreq'][0])):
            decide[index] = 1
        else:
            decide[index] = 0

    data_B1st['Decision'] = decide

    # Result
    index = 0
    for index in range(len(data_B1st)):

        if data_B1st['Search'][index] + data_B1st['Decision'][index] == 2:
            result[index] = f'03 Move to {B2nd}'
        elif data_B1st['Search'][index] == 1:
            result[index] = '02 Search Only'
        else:
            result[index] = '01 Not Searching'

        data_B1st['Result'] = result

    # Plot definition
    pmax = -70
    pmin = -140

    # Plot scatter
    data_B1st = data_B1st.sort_values('Result')
    ax = sns.scatterplot(x=f'{B2nd}_RSRP (dBm)', y=f'{B1st}_RSRP (dBm)',
                         hue='Result', data=data_B1st, palette=['steelblue','goldenrod','seagreen'])

    # Define Straight Line Function
    x = np.linspace(pmin, pmax)
    y = x

    # Plot Equal Line
    plt.plot(x, y, color='k', linestyle='-')

    # Plot Search line
    searchline = sNonIntraSearchP
    y = searchline
    plt.axhline(y, color='b', linestyle='--')
    plt.text(pmin, y + 1, f'SIB3_s-NonIntraSearchP = {searchline} dBm')

    # Plot Decision line
    decideline = param_dict['SIB5_q-OffsetFreq'][0] + \
        param_dict['SIB3_q-Hyst'][0]
    y = x - decideline
    plt.plot(x, y, color='b', linestyle='--')
    plt.text(pmin, pmin + 1,
             f'SIB5_q-OffsetFreq + SIB3_q-Hyst = {decideline} dB')

    plt.xlabel(f'{B2nd}_RSRP (dBm)')
    plt.ylabel(f'{B1st}_RSRP (dBm)')
    plt.title(f'[RSRP] {B1st} Reselection to {B2nd} [Equal Priority]')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.ylim((pmin, pmax))
    plt.xlim((pmin, pmax))

    plt.show()


#Low to High
elif B1st_to_B2nd == LowtoHigh

    # Create Search Criteria
    index = 0
    for index in range(len(data_B1st)):
        search[index] = 1

    data_B1st['Search'] = search

    # Create Decision Criteria
    index = 0
    for index in range(len(data_B1st)):

        if (data_B1st[f'{B2nd}_RSRP (dBm)'][index] > (param_dict['SIB5_q-RxLevMin'][0] + param_dict['SIB5_threshX-HighP'][0])):
            decide[index] = 1
        else:
            decide[index] = 0

    data_B1st['Decision'] = decide

    # Result
    index = 0
    for index in range(len(data_B1st)):

        if data_B1st['Search'][index] + data_B1st['Decision'][index] == 2:
            result[index] = f'02 Move to {B2nd}'
        elif data_B1st['Search'][index] == 1:
            result[index] = '01 Always Searching'

        data_B1st['Result'] = result

    # Plot definition
    pmax = -70
    pmin = -140

    # Plot scatter
    data_B1st = data_B1st.sort_values('Result')
    ax = sns.scatterplot(x=f'{B2nd}_RSRP (dBm)', y=f'{B1st}_RSRP (dBm)',
                         hue='Result', data=data_B1st, palette=['goldenrod','seagreen'])

    # Define Straight Line Function
    x = np.linspace(pmin, pmax)
    y = x

    # Plot Equal Line
    plt.plot(x, y, color='k', linestyle='-')

    # Plot Decision line
    decideline = param_dict['SIB5_q-RxLevMin'][0] + param_dict['SIB5_threshX-HighP'][0]
    y = decideline
    plt.axvline(y, color='b', linestyle='--')
    plt.text(pmin, y + 1, f'SIB5_q-RxLevMin + SIB5_threshX-HighP = {decideline} dBm')

    plt.xlabel(f'{B2nd}_RSRP (dBm)')
    plt.ylabel(f'{B1st}_RSRP (dBm)')
    plt.title(f'[RSRP] {B1st} Reselection to {B2nd} [Low -> High Priority]')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.ylim((pmin, pmax))
    plt.xlim((pmin, pmax))

    plt.show()


########################################################Currently testing#######################################################
# REVIEW:


########################################################Currently testing#######################################################


print(' ')
print('ありがとうございました！！')
print('Download this program: https://github.com/zulfadlizainal')
print('Author: https://www.linkedin.com/in/zulfadlizainal')
print(' ')
