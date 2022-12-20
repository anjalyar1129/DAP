# -*- coding: utf-8 -*-
"""
Created on Fri Dec  10 14:36:16 2022

@author: Anjaly
"""

import plotly.express as px
import pymongo
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["AirlineData"]

def date_conc(r):
    if(len(str(r['MONTH']))==1):
        dt='2020'+'-0'+str(r['MONTH'])
    if(len(str(r['MONTH']))==2):
        dt='2020'+'-'+str(r['MONTH'])
    if(len(str(r['DAY_OF_MONTH']))==1):
        dt=dt+'-0'+str(r['DAY_OF_MONTH'])
    if(len(str(r['DAY_OF_MONTH']))==2):
        dt=dt+'-'+str(r['DAY_OF_MONTH'])
    return dt

# ONTIME_REPORTING_01
col = db["ONTIME_REPORTING_01"]

df=pd.DataFrame(list(col.find()))



df['dt']=df.apply( lambda x: date_conc(x),axis=1)


# ONTIME_REPORTING_02
col2 = db["ONTIME_REPORTING_02"]

df2=pd.DataFrame(list(col2.find()))
df2['dt']=df2.apply( lambda x: date_conc(x),axis=1)

# ONTIME_REPORTING_03
col2_rep = db["ONTIME_REPORTING_03"]

df2_rep=pd.DataFrame(list(col2_rep.find()))
df2_rep['dt']=df2_rep.apply( lambda x: date_conc(x),axis=1)

# ONTIME_REPORTING_04
col4_rep = db["ONTIME_REPORTING_04"]

df4_rep=pd.DataFrame(list(col4_rep.find()))
df4_rep['dt']=df4_rep.apply( lambda x: date_conc(x),axis=1)

# ONTIME_REPORTING_05
col5_rep = db["ONTIME_REPORTING_05"]

df5_rep=pd.DataFrame(list(col5_rep.find()))
df5_rep['dt']=df5_rep.apply( lambda x: date_conc(x),axis=1)

# ONTIME_REPORTING_06
col6_rep = db["ONTIME_REPORTING_06"]

df6_rep=pd.DataFrame(list(col6_rep.find()))
df6_rep['dt']=df6_rep.apply( lambda x: date_conc(x),axis=1)

# ONTIME_REPORTING_07
col7_rep = db["ONTIME_REPORTING_07"]

df7_rep=pd.DataFrame(list(col7_rep.find()))
df7_rep['dt']=df7_rep.apply( lambda x: date_conc(x),axis=1)


# ONTIME_REPORTING_08
col8_rep = db["ONTIME_REPORTING_08"]

df8_rep=pd.DataFrame(list(col8_rep.find()))
df8_rep['dt']=df8_rep.apply( lambda x: date_conc(x),axis=1)

# ONTIME_REPORTING_09
col9_rep = db["ONTIME_REPORTING_09"]

df9_rep=pd.DataFrame(list(col9_rep.find()))
df9_rep['dt']=df9_rep.apply( lambda x: date_conc(x),axis=1)

# ONTIME_REPORTING_10
col10_rep = db["ONTIME_REPORTING_10"]

df10_rep=pd.DataFrame(list(col10_rep.find()))
df10_rep['dt']=df10_rep.apply( lambda x: date_conc(x),axis=1)


# ONTIME_REPORTING_11
col11_rep = db["ONTIME_REPORTING_11"]

df11_rep=pd.DataFrame(list(col11_rep.find()))
df11_rep['dt']=df11_rep.apply( lambda x: date_conc(x),axis=1)


# ONTIME_REPORTING_12
col12_rep = db["ONTIME_REPORTING_12"]

df12_rep=pd.DataFrame(list(col12_rep.find()))
df12_rep['dt']=df12_rep.apply( lambda x: date_conc(x),axis=1)



comb=[df,df2,df2_rep,df4_rep,df5_rep,df6_rep,df7_rep,df8_rep,df9_rep,df10_rep,df11_rep,df12_rep]
df3=pd.concat(comb)
df_excl=df3[~df3['OP_UNIQUE_CARRIER'].isin(['OO','UA','YX','MQ','B6','OH'])]

col_p10 = db.P10_EMPLOYEES
p10_employees_df = pd.DataFrame(list(col_p10.find()))



col_carr = db.CARRIER_DECODE
df_carr = pd.DataFrame(list(col_carr.find()))
carrier_decode_df=df_carr.drop_duplicates(subset='OP_UNIQUE_CARRIER', keep="first")

p10_employees_df_1=p10_employees_df.drop_duplicates(subset='OP_UNIQUE_CARRIER', keep="first")

df_carrier1 = pd.merge(carrier_decode_df, p10_employees_df_1, on='OP_UNIQUE_CARRIER')

f1=pd.merge(df_carrier1,df3,on='OP_UNIQUE_CARRIER')

f1['MONTH']=f1['MONTH'].astype('Int64').astype('str')
f1['DEP_DEL15']=f1['DEP_DEL15'].astype('Int64').astype(str)
f2= f1[f1['DEP_DEL15']!='<NA>']


#Plot7
p7_1=f2[f2['OP_UNIQUE_CARRIER']=='AA']
p7_2=p7_1.groupby(['MONTH'])['CARRIER_DELAY','WEATHER_DELAY','NAS_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY'].sum().reset_index()

p7_2['CARRIER_DELAY_1']=p7_2['CARRIER_DELAY']/60
fig_7 = px.line(p7_2, x="MONTH", y="CARRIER_DELAY_1")
fig_7.update_layout(
    title={'text' :"Carrier delayed for American Airlines",'x':0.5,'xanchor': 'center'},
    xaxis_title="Month",
    yaxis_title="Total hours reported for carrier delays#",
    #legend_title="Factors",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)
#fig_7.update_xaxes(categoryorder='array', categoryarray= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

fig_7.show()

#Plot8 Late aircraft delay
p8_1=f2[f2['LATE_AIRCRAFT_DELAY']!=0]
p8_2=p8_1.groupby(['CARRIER_NAME_x'])['CARRIER_DELAY','WEATHER_DELAY','NAS_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY'].sum().reset_index()

p8_2['LATE_AIRCRAFT_DELAY_1']=p8_2['LATE_AIRCRAFT_DELAY']/60
fig_8 = px.line(p8_2, x="CARRIER_NAME_x", y="LATE_AIRCRAFT_DELAY_1")
fig_8.update_layout(
    title={'text' :"Late aircraft delays",'x':0.5,'xanchor': 'center'},
    xaxis_title="Carrier",
    yaxis_title="Total hours reported#",
    #legend_title="Factors",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)



 