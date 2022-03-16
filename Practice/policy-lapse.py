# INSURANCE POLICY LAPSE PREDICTION CHALLENGE

''' This is a practice challenge in preparation of 
    the UmojaHack.
    The model here predicts if a customer in the insurance
    company is likely to drop their policy. Customer churn 
    is important to insurance. The premiums paid on the
    policies are the company's main source of income. Therefore,
    the ability to predict customer churn, allows them to plan 
    around the possibility of loss of revenue
    '''

# IMPORTING PACKAGES
import numpy as np
import pandas as pd

# DATA IMPORTATION
client_df = pd.read_csv('data/client_data.csv')
payment_df = pd.read_csv('data/payment_history.csv')
policy_df = pd.read_csv('data/policy_data.csv')
train_df = pd.read_csv('data/train.csv')
smp_sub_df = pd.read_csv('data/sample_sub.csv')

#EDA
