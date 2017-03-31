############################################################
# About
# Date: March 31 2017

'''
Mark rows/entries in final BED file that have Mendelian consistent sites
'''
############################################################

############################################################
# Imports
############################################################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as p
import sklearn as sol

############################################################
# Load Data
############################################################

DEL_250bp = pd.read_csv("250bp.Mend.DEL.csv")
DEL_10x = pd.read_csv("10x.Mend.DEL.csv")
DEL_300x = pd.read_csv("300x.Mend.DEL.csv")
DEL_MP = pd.read_csv("MP.Mend.DEL.csv")
DEL_PacBio = pd.read_csv("PacBio.Mend.DEL.csv")
INS_250bp = pd.read_csv("250bp.Mend.INS.csv")
INS_300x = pd.read_csv("300x.Mend.DEL.csv")
INS_10x = pd.read_csv("10x.Mend.DEL.csv")
INS_MP = pd.read_csv("MP.Mend.DEL.csv")
INS_PacBio = pd.read_csv("PacBio.Mend.DEL.csv")

all_data_DEL = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ML.Training/svvizAllData.DEL.csv")
all_data_INS = pd.read_csv("/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ML.Training/svvizAllData.INS.2.csv")
# print all_data_DEL.head(3)
# print all_data_INS.head(3)

'''
Store Data in Dataframes
'''

new_df_DEL = pd.concat([DEL_250bp, DEL_10x, DEL_300x,DEL_MP,DEL_PacBio], axis=0)
new_df_DEL['Counts'] = new_df_DEL.groupby(['start'])['end'].transform('count')
new_df_DEL['Count_2'] = new_df_DEL.groupby(['id'])['start'].transform('count')
new_df_DEL['AllRefCount'] = np.where((new_df_DEL['HG002'] == 0) & (new_df_DEL['HG003'] == 0) & (new_df_DEL['HG004'] == 0), '0', '')
new_df_DEL.to_csv('mend_Del.csv', index=False)
mend_DEL = pd.read_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/Mendelian/MarkMendSites/mend_Del.csv')
print mend_DEL.head(3)
print all_data_DEL.head(3)


'''
Find matches between 2 dataframes and create a new column with corresponding label
'''

all_data_DEL['Count_2'] = -1

for j, i in enumerate(range(all_data_DEL.shape[0])):
	if j > 100:
		break
	start_value = all_data_DEL.loc[i, 'start']
	start_indices = np.where(mend_DEL['start'] == start_value)[0].tolist()
	# print(start_indices)
	end_value = all_data_DEL.loc[i, 'end']
	end_indices = np.where(mend_DEL['end'] == end_value)[0].tolist()
	# print(end_indices)
	index = set(start_indices) & set(end_indices)
	if len(index) == 0:
		continue
	# if len(index) > 1:
	# 	print("Unexpected hits found", i, index)
	# 	print(mend_DEL.loc[index, 'Counts'])
	# print(i, start_value, end_value, index)
	all_data_DEL.loc[i, 'Count_2'] = np.median(mend_DEL.loc[index, 'Count_2'])
	# print(all_data_DEL.loc[i])

print(all_data_DEL.head(10))
all_data_DEL.to_csv('all.csv')



"""
Extra Code 

all_data_DEL['MendConsist'] = np.where((mend_DEL['start'] == all_data_DEL['start']) & (mend_DEL['end'] == all_data_DEL['end']), mend_DEL['Counts'], '0')
all_data_DEL.to_csv('/Users/lmc2/Desktop/NIST/Projects/ML1-TrainingData/Code/PythonCode/Feb132017/ML.Training/svvizAllData.DEL_mend.csv', index=False)
new_df_INS = pd.concat([INS_250bp,INS_300x,INS_10x,INS_MP,INS_PacBio], axis=0)

# print new_df_DEL.head()
new_df_DEL.columns = ['index2', 'chrom.mend', 'start.mend', 'end.mend','id.mend', 'SVtype.mend', 'HG002.mend', 'HG003.mend', 'HG004.mend', 'tech.mend'] 
# print new_df_DEL.head()

# print new_df_DEL.head()
# print new_df_DEL.shape

# print new_df_INS.head()
# print new_df_INS.shape

# ne_stacked = (all_data_DEL != new_df_DEL).stack()
# print ne_stacked.head()

# pd.concat([df,df1], ignore_index=True, axis=1)

# def random(row):
# 	return new_df_DEL['size']
# 	else '1'

# all_data_DEL['new'] = all_data_DEL.apply(func = random, axis = 1)
# print all_data_DEL.head(3)

all_data_DEL['MendConsist'] = np.where((all_data_DEL[['start']].isin(['3262328', '3816054', '3816054', '9168051'])), '1', '0')

print all_data_DEL.head()

df = pd.concat([all_data_DEL,new_df_DEL])
# df['MendConsist'] = np.where((df['start'].isin(df['start.mend']), '1', '0'))
print df.head(3)
df.to_csv('all.csv')

# merged = all_data_DEL.merge(new_df_DEL, on='chrom')
# print merged.head(3)

# merged.to_csv('all.csv')
# merged['MendConsist'] = np.where((merged[['start_x']] == new_df_DEL[['start_y']]), '1', '0')

# all_data_DEL['MendConsist'] = np.where((all_data_DEL[['start']].isin([]) == new_df_DEL[['start']]), '1', '0')
# us_mq_airlines_index = data['unique_carrier'].isin(['US','MQ'])
# # all_data_DEL['MendConsist'] = np.where((all_data_DEL[['start']] == new_df_DEL[['start']]), '1', '0')
# s2[s2.isin(s1)]
"""

