# -*- coding: utf-8 -*-


import pandas as pd
import re

inputname = 'training_data.csv'
outputname = 'output.csv'

df = pd.read_csv(inputname)

# months を削除(int)
df.term = df.term.str.extract('([0-9]+)')

# % を削除(float)
df.int_rate = df.int_rate.str.extract('([0.0-9]+)').astype(float)
df.revol_util = df.revol_util.str.extract('([0.0-9]+)').astype(float)

# gradeを数値化
grades = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for index, grade in enumerate(grades):
    df['grade'] = df['grade'].mask(df['grade']  == grade, index)

# emp_lengthを数値化 n/aを0に、1年未満を0に、10年以上を10に、他はそのまま
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == 'n/a', '0')
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == '< 1 year', '0')
df.emp_length=df.emp_length.str.extract('([0-9]+)')
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == '10+ years', '10')

# is_good_customerを数値化 (yes → 1 no → 0)
df['is_good_customer'] = [(1 if v == 'yes' else 0) for v in df['is_good_customer']]

# pymnt_planを数値化 (yes → 1 no → 0)
df['pymnt_plan'] = [(1 if v== 'yes' else 0) for v in df['pymnt_plan']]

# initial_list_statusを数値化 (w → 1 f → 0)
df['initial_list_status'] = [(1 if v== 'w' else 0) for v in df['initial_list_status']]


# home_ownership を数値化
home_ownerships = ['RENT', 'OWN', 'MORTGAGE', 'OTHER']
for index, home_ownership in enumerate(home_ownerships):
    df['home_ownership'] = df['home_ownership'].mask(df['home_ownership'] == home_ownership, index)

# verification_status　を数値化
verification_status = ['Not Verified', 'Source Verified', 'Verified']
for index, verification_status in enumerate(verification_status):
    df['verification_status'] = df['verification_status'].mask(df['verification_status'] == verification_status, index)


# 0で穴埋め
df['mo_sin_old_il_acct'] = df['mo_sin_old_il_acct'].fillna(0)
df['mths_since_recent_bc_dlq'] = df['mths_since_recent_bc_dlq'].fillna(0)
df['mths_since_recent_revol_delinq'] = df['mths_since_recent_revol_delinq'].fillna(0)
df['num_tl_120dpd_2m'] = df['num_tl_120dpd_2m'].fillna(0)
df['mths_since_last_delinq'] = df['mths_since_last_delinq'].fillna(0)
df['mths_since_last_record'] = df['mths_since_last_record'].fillna(0)
df['mths_since_last_major_derog'] = df['mths_since_last_major_derog'].fillna(0)
df['il_util'] = df['il_util'].fillna(0)

#出力
df.to_csv(outputname, index = None)
