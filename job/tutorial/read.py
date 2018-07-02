# -*- coding: utf-8 -*-
import pandas as pd
import pymysql
from sqlalchemy import create_engine

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
import warnings
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

file_='327.csv'
data = pd.read_csv(file_,encoding='utf-8')
data.to_csv('327_.csv',encoding='gbk')
# connect = create_engine('mysql+pymysql://root:hunteron@192.168.50.90:3306/test?charset=utf8',echo=True)
# pd.io.sql.to_sql(data,'51job_hc',connect,if_exists='replace')
print(data)


