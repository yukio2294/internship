# -*- coding: utf-8 -*-


import pandas as pd
import re

inputname = 'training_data.csv'
outputname = 'output.csv'

df = pd.read_csv(inputname)

#列消去
del df['installment']
del df['id']
del df['int_rate']
del df['grade']
del df['sub_grade']
del df['verification_status']
del df['pymnt_plan']
del df['title']
del df['zip_code']
del df['dti']
del df['delinq_2yrs']
del df['earliest_cr_line']
del df['inq_last_6mths']
del df['mths_since_last_delinq']
del df['mths_since_last_record']
del df['open_acc']
del df['pub_rec']
del df['revol_bal']
del df['revol_util']
del df['total_acc']
del df['initial_list_status']
del df['mths_since_last_major_derog']
del df['acc_now_delinq']
del df['tot_cur_bal']
del df['open_acc_6m']
del df['open_il_6m']
del df['open_il_12m']
del df['open_il_24m']
del df['mths_since_rcnt_il']
del df['total_bal_il']
del df['il_util']
del df['open_rv_12m']
del df['open_rv_24m']
del df['max_bal_bc']
del df['all_util']
del df['total_rev_hi_lim']
del df['inq_fi']
del df['total_cu_tl']
del df['inq_last_12m']
del df['acc_open_past_24mths']
del df['avg_cur_bal']
del df['bc_open_to_buy']
del df['bc_util']
del df['chargeoff_within_12_mths']
del df['delinq_amnt']
del df['mo_sin_old_il_acct']
del df['mo_sin_old_rev_tl_op']
del df['mo_sin_rcnt_rev_tl_op']
del df['mo_sin_rcnt_tl']
del df['mort_acc']
del df['mths_since_recent_bc']
del df['mths_since_recent_bc_dlq']
del df['mths_since_recent_inq']
del df['mths_since_recent_revol_delinq']
del df['num_accts_ever_120_pd']
del df['num_actv_bc_tl']
del df['num_actv_rev_tl']
del df['num_bc_sats']
del df['num_bc_tl']
del df['num_il_tl']
del df['num_op_rev_tl']
del df['num_rev_accts']
del df['num_rev_tl_bal_gt_0']
del df['num_sats']
del df['num_tl_120dpd_2m']
del df['num_tl_30dpd']
del df['num_tl_90g_dpd_24m']
del df['num_tl_op_past_12m']
del df['pct_tl_nvr_dlq']
del df['percent_bc_gt_75']
del df['pub_rec_bankruptcies']
del df['tax_liens']
del df['tot_hi_cred_lim']
del df['total_bal_ex_mort']
del df['total_bc_limit']
del df['total_il_high_credit_limit']

# months を削除(int)
df.term = df.term.str.extract('([0-9]+)')
#df.zip_code = df.zip_code.str.extract('([0-9]+)')

# % を削除(float)
#df.int_rate = df.int_rate.str.extract('([0.0-9]+)').astype(float)
#df.revol_util = df.revol_util.str.extract('([0.0-9]+)').astype(float)

# gradeを数値化
#grades = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#for index, grade in enumerate(grades):
#    df['grade'] = df['grade'].mask(df['grade']  == grade, index)

# emp_lengthを数値化 n/aを0に、1年未満を0に、10年以上を10に、他はそのまま
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == 'n/a', '0')
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == '< 1 year', "0.5")
df.emp_length=df.emp_length.str.extract('([0-9]+)')
df['emp_length'] = df['emp_length'].mask(df['emp_length'] == '10+ years', '10')

# is_good_customerを数値化 (yes → 1 no → 0)
df['is_good_customer'] = [(1 if v == 'yes' else 0) for v in df['is_good_customer']]

# pymnt_planを数値化 (yes → 1 no → 0)
#df['pymnt_plan'] = [(1 if v== 'yes' else 0) for v in df['pymnt_plan']]

# initial_list_statusを数値化 (w → 1 f → 0)
#df['initial_list_status'] = [(1 if v== 'w' else 0) for v in df['initial_list_status']]


# home_ownership を数値化
home_ownerships = ['RENT', 'OWN', 'MORTGAGE', 'OTHER']
for index, home_ownership in enumerate(home_ownerships):
    df['home_ownership'] = df['home_ownership'].mask(df['home_ownership'] == home_ownership, index)

# verification_status　を数値化
#verification_status = ['Not Verified', 'Source Verified', 'Verified']
#for index, verification_status in enumerate(verification_status):
#    df['verification_status'] = df['verification_status'].mask(df['verification_status'] == verification_status, index)


# 0で穴埋め
#df['mo_sin_old_il_acct'] = df['mo_sin_old_il_acct'].fillna(0)
#df['mths_since_recent_bc_dlq'] = df['mths_since_recent_bc_dlq'].fillna(0)
#df['mths_since_recent_revol_delinq'] = df['mths_since_recent_revol_delinq'].fillna(0)
#df['num_tl_120dpd_2m'] = df['num_tl_120dpd_2m'].fillna(0)
#df['mths_since_last_delinq'] = df['mths_since_last_delinq'].fillna(0)
#df['mths_since_last_record'] = df['mths_since_last_record'].fillna(0)
#df['mths_since_last_major_derog'] = df['mths_since_last_major_derog'].fillna(0)
#df['il_util'] = df['il_util'].fillna(0)

#出力
df.to_csv(outputname, index = None)
