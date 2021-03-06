###################################################
# About
# Date: February 10, 2017
# Description:
# Randomly select 5000 INS and DEL from union_altref.vcf
# Start with AWK/SED modifified VCF
# Select true INS and DEL based on alt/ref length
# Ref > Alt : DEL
# Alt > Ref : INS
###################################################

###################################################
# Imports 
###################################################
import pandas as pd
import random
import numpy as np

###################################################
# Data 
###################################################

# Load/Parse .txt file using pd.read_table()
colnames = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
df = pd.read_table('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/union_refalt.sort.formattedforsvviz.txt', names=colnames)
print df.head(5)
# print len(df)


#################################################
# Code
#################################################
# Identify INS and DEL based on length of strings in alt (df['E']) and ref (df['D']) columns
# 1. Convert strings listed in Ref and Alt columns into .str format
# 2. Find lenth of each string and store in new column ['refLen'] and ['altLen']
df['refLen'] = df['D'].astype('str')
df['refLen'] = df['refLen'].str.len()
df['altLen'] = df['E'].astype('str')
df['altLen'] = df['altLen'].str.len()
print df.head()

# 3. Compare the length of strings in ['refLen'] and ['altLen'] 
df['VariantType'] = np.where(df['refLen'] > df['altLen'], 'DEL', 'INS')
print df.head()
my_tab = pd.crosstab(index=df['VariantType'], columns='count')
print 

# Store new INS and DEL in new dataframes
df['VariantType'].fillna('', inplace=True)
dfDel = df[df['VariantType'].str.contains("DEL")]
dfIns = df[df['VariantType'].str.contains("INS")]

'''
Deletions
'''
# Take a random sample of 5000 INS and 5000 DEL and store them in respective .tsv files
row = random.sample(dfDel.index, 5000)
df_del = dfDel.ix[row]
# print ('These are the deletions', df_del.head())
# print df_del.shape


df_del_1to1000 = df_del.iloc[:1000]
df_del_1001to2000 = df_del.iloc[1001:2000]
df_del_2001to3000 = df_del.iloc[2001:3000]
df_del_3001to4000 = df_del.iloc[3001:4000]
df_del_4001to5000 = df_del.iloc[4001:5000]
# print df_del.head(5)
# print len(df_del)

df_del_1to1000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/DEL/1-1000/union_refalt.sort.DEL.1to1000.tsv', sep='\t', header=None, index=False)
df_del_1001to2000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/DEL/1001-2000/union_refalt.sort.DEL.1001to2000.tsv', sep='\t', header=None, index=False)
df_del_2001to3000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/DEL/2001-3000/union_refalt.sort.DEL.2001to3000.tsv', sep='\t', header=None, index=False)
df_del_3001to4000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/DEL/3001-4000/union_refalt.sort.DEL.3001to4000.tsv', sep='\t', header=None, index=False)
df_del_4001to5000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/DEL/4001-5000/union_refalt.sort.DEL.4001to5000.tsv', sep='\t', header=None, index=False)


'''
Insertions
'''
row = random.sample(dfIns.index, 5000)
df_ins = dfIns.ix[row]
# print ('These are the insertions', df_ins.head())
# print df_del.shape


df_ins_1to1000 = df_ins[:1000]
df_ins_1001to2000 = df_ins[1001:2000]
df_ins_2001to3000 = df_ins[2001:3000]
df_ins_3001to4000 = df_ins[3001:4000]
df_ins_4001to5000 = df_ins[4001:5000]
# print df_ins.head(5)
# print len(df_ins)

df_ins_1to1000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/INS/1-1000/union_refalt.sort.INS.1to1000.tsv', sep='\t', header=None, index=False)
df_ins_1001to2000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/INS/1001-2000/union_refalt.sort.INS.1001to2000.tsv', sep='\t', header=None, index=False)
df_ins_2001to3000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/INS/2001-3000/union_refalt.sort.INS.2001to3000.tsv', sep='\t', header=None, index=False)
df_ins_3001to4000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/INS/3001-4000/union_refalt.sort.INS.3001to4000.tsv', sep='\t', header=None, index=False)
df_ins_4001to5000.to_csv('/Volumes/lesleydata/SVVIZOutput/April112017/Step1/RandomSelection.VCFs/VCF/INS/4001-5000/union_refalt.sort.INS.4001to5000.tsv', sep='\t', header=None, index=False)

# SOURCE: randomly select rows
# http://stackoverflow.com/questions/12190874/pandas-sampling-a-dataframe



#################################################
# Extra Code
#################################################

# train = pd.read_csv('union_refalt.sort2.txt')
# df = pd.DataFrame(train)
# print df.head(5)
#FYI: How to include names of columns
# colnames = ['A', 'B', 'C', 'D']
# df = pd.read_table('union_refalt.sort2.txt', header=None, names=colnames)

