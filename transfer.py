import pandas as pd
import re

filename = 'training_data.csv'

df = pd.read_csv(filename)


df['is_good_customer'] = [(1 if v == 'yes' else 0) for v in df['is_good_customer']]

df['pymnt_plan'] = [(1 if v== 'yes' else 0) for v in df['pymnt_plan']]

df.term = df.term.str.extract('([0-9]+)')

df.int_rate = df.int_rate[:-1]

home_ownerships = ['RENT', 'OWN', 'MORTGAGE', 'OTHER']

for index, home_ownership in enumerate(home_ownerships):
    df['home_ownership'] = df['home_ownership'].mask(df['home_ownership'] == home_ownership, index)

df['emp_length'] = df['emp_length'].mask(df['emp_length'] == 'n/a', '0')
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == '< 1 year', '0')
df.emp_length=df.emp_length.str.extract('([0-9]+)')
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == '10+ years', '10')

grades = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for index, grade in enumerate(grades):
    df['grade'] = df['grade'].mask(df['grade']  == grade, index)

df['mo_sin_old_il_acct'] = df['mo_sin_old_il_acct'].fillna(0)
df['mths_since_recent_bc_dlq'] = df['mths_since_recent_bc_dlq'].fillna(0)
df['mths_since_recent_revol_delinq'] = df['mths_since_recent_revol_delinq'].fillna(0)
df['num_tl_120dpd_2m'] = df['num_tl_120dpd_2m'].fillna(0)


df.to_csv('test.csv', index = None)
