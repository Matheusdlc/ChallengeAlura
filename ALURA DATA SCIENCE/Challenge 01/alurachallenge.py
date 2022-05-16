import pandas as pd 
import numpy
import requests
import json
import time



t = open('Telco-Customer-Churn.json',)
resposta = json.load(t)
df = pd.json_normalize(resposta)

#df = df.rename( columns={   'customerID':'id'
#                            ,'Churn':''
#                            ,'customer.gender':''
#                            ,'customer.SeniorCitizen':''
#                            ,'customer.Partner':''
#                            ,'customer.Dependents':''
#                            ,'customer.tenure':''
#                            ,'phone.PhoneService':''
#                            ,'phone.MultipleLines':''
#                            ,'internet.InternetService':''
#                            ,'internet.OnlineSecurity':''
#                            ,'internet.OnlineBackup':''
#                            ,'internet.DeviceProtection':''
#                            ,'internet.TechSupport':''
#                            ,'internet.StreamingTV':''
#                            ,'internet.StreamingMovies':''
#                            ,'account.Contract':''
#                            ,'account.PaperlessBilling':''
#                            ,'account.PaymentMethod':''
#                            ,'account.Charges.Monthly':''
#                            ,'account.Charges.Total':''})

#print(df.dtypes) #verifica os tipos de dados do DF
#customerID                    object
#Churn                         object
#customer.gender               object
#customer.SeniorCitizen         int64
#customer.Partner              object
#customer.Dependents           object
#customer.tenure                int64
#phone.PhoneService            object
#phone.MultipleLines           object
#internet.InternetService      object
#internet.OnlineSecurity       object
#internet.OnlineBackup         object
#internet.DeviceProtection     object
#internet.TechSupport          object
#internet.StreamingTV          object
#internet.StreamingMovies      object
#account.Contract              object
#account.PaperlessBilling      object
#account.PaymentMethod         object
#account.Charges.Monthly      float64
#account.Charges.Total         object


#------------------Vrificar quantos valores null existem
#print(df.info())  
# #   Column                     Non-Null Count  Dtype
#---  ------                     --------------  -----
# 0   customerID                 7267 non-null   object
# 1   Churn                      7267 non-null   object
# 2   customer.gender            7267 non-null   object
# 3   customer.SeniorCitizen     7267 non-null   int64
# 4   customer.Partner           7267 non-null   object
# 5   customer.Dependents        7267 non-null   object
# 6   customer.tenure            7267 non-null   int64
# 7   phone.PhoneService         7267 non-null   object
# 8   phone.MultipleLines        7267 non-null   object
# 9   internet.InternetService   7267 non-null   object
# 10  internet.OnlineSecurity    7267 non-null   object
# 11  internet.OnlineBackup      7267 non-null   object
# 12  internet.DeviceProtection  7267 non-null   object
# 13  internet.TechSupport       7267 non-null   object
# 14  internet.StreamingTV       7267 non-null   object
# 15  internet.StreamingMovies   7267 non-null   object
# 16  account.Contract           7267 non-null   object
# 17  account.PaperlessBilling   7267 non-null   object
# 18  account.PaymentMethod      7267 non-null   object
# 19  account.Charges.Monthly    7267 non-null   float64
# 20  account.Charges.Total      7267 non-null   object
#dtypes: float64(1), int64(2), object(18)
#print(df.isnull().sum())
#customerID                   0
#Churn                        0
#customer.gender              0
#customer.SeniorCitizen       0
#customer.Partner             0
#customer.Dependents          0
#customer.tenure              0
#phone.PhoneService           0
#phone.MultipleLines          0
#internet.InternetService     0
#internet.OnlineSecurity      0
#internet.OnlineBackup        0
#internet.DeviceProtection    0
#internet.TechSupport         0
#internet.StreamingTV         0
#internet.StreamingMovies     0
#account.Contract             0
#account.PaperlessBilling     0
#account.PaymentMethod        0
#account.Charges.Monthly      0
#account.Charges.Total        0
#dtype: int64


#for coluna in df.columns:               #verificando cada coluna
#    print('---')
#    print(df[coluna].value_counts())
#0002-ORFBO    1
#6614-VBEGU    1
#6637-KYRCV    1
#6635-MYYYZ    1
#6635-CPNUN    1
#             ..
#3374-TTZTK    1
#3374-PZLXD    1
#3374-LXDEV    1
#3373-YZZYM    1
#9995-HOTOH    1
#Name: customerID, Length: 7267, dtype: int64
#---
#No     5174
#Yes    1869
#        224
#Name: Churn, dtype: int64
#---
#Male      3675
#Female    3592
#Name: customer.gender, dtype: int64
#---
#0    6085
#1    1182
#Name: customer.SeniorCitizen, dtype: int64
#---
#No     3749
#Yes    3518
#Name: customer.Partner, dtype: int64
#---
#No     5086
#Yes    2181
#Name: customer.Dependents, dtype: int64
#---
#1     634
#72    369
#2     246
#3     207
#4     185
#     ...
#38     60
#39     59
#44     54
#36     50
#0      11
#Name: customer.tenure, Length: 73, dtype: int64
#---
#Yes    6560
#No      707
#Name: phone.PhoneService, dtype: int64
#---
#No                  3495
#Yes                 3065
#No phone service     707
#Name: phone.MultipleLines, dtype: int64
#---
#Fiber optic    3198
#DSL            2488
#No             1581
#Name: internet.InternetService, dtype: int64
#---
#No                     3608
#Yes                    2078
#No internet service    1581
#Name: internet.OnlineSecurity, dtype: int64
#---
#No                     3182
#Yes                    2504
#No internet service    1581
#Name: internet.OnlineBackup, dtype: int64
#---
#No                     3195
#Yes                    2491
#No internet service    1581
#Name: internet.DeviceProtection, dtype: int64
#---
#No                     3582
#Yes                    2104
#No internet service    1581
#Name: internet.TechSupport, dtype: int64
#---
#No                     2896
#Yes                    2790
#No internet service    1581
#Name: internet.StreamingTV, dtype: int64
#---
#No                     2870
#Yes                    2816
#No internet service    1581
#Name: internet.StreamingMovies, dtype: int64
#---
#Month-to-month    4005
#Two year          1743
#One year          1519
#Name: account.Contract, dtype: int64
#---
#Yes    4311
#No     2956
#Name: account.PaperlessBilling, dtype: int64
#---
#Electronic check             2445
#Mailed check                 1665
#Bank transfer (automatic)    1589
#Credit card (automatic)      1568
#Name: account.PaymentMethod, dtype: int64
#---
#20.05     65
#19.85     46
#19.90     46
#19.70     45
#19.55     45
#          ..
#23.45      1
#116.55     1
#106.85     1
#68.55      1
#67.85      1
#Name: account.Charges.Monthly, Length: 1585, dtype: int64
#---
#           11
#20.2       11
#19.75       9
#19.55       9
#19.9        9
#           ..
#272         1
#1426.45     1
#371.6       1
#6786.4      1
#3707.6      1


#------tratando a coluna churn

print(df.groupby(['Churn']).count())

for row in df['Churn']:
    print(row)               #verificando cada coluna
#    if row == '':
#        df['Churn'] = 'na'





