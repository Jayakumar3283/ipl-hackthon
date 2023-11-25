#!/usr/bin/env python
# coding: utf-8

# In[129]:


import pandas as pd
import numpy as np


# In[130]:


df_deliveries = pd.read_csv("deliveries.csv")

df_matches = pd.read_csv("matches.csv")


# In[131]:


df_deliveries.head()


# In[132]:


df_matches.head()


# In[133]:


df_deliveries.info()


# In[134]:


df_deliveries.describe(include="all")


# In[135]:


df_matches.info()


# In[136]:


df_matches["date"]=pd.to_datetime(df_matches["date"],errors="coerce")


# In[141]:


df_matches.info()


# In[142]:


df_matches.loc[636]


# In[ ]:





# In[143]:


df_matches.describe(include="all")


# In[144]:


df_merged = pd.merge(left=df_deliveries,right=df_matches , left_on="match_id", right_on="id")


# In[145]:


df_merged


# In[147]:


df_merged.to_csv("df_merged1.csv")


# In[148]:


df_merged.info()


# In[149]:


df_merged.isnull(axis=0)


# In[150]:


df_merged.loc[df_merged["wide_runs"]==2]["wide_runs"]


# In[151]:


df_merged["inning"].unique()


# In[152]:


df_merged[df_merged["inning"]==5]


# In[153]:


city_season_grouped=df_merged.groupby(["city","season"])


# In[201]:


city_season_grouped.groups.keys()


# In[206]:


city_season_grouped["season"].mean()


# In[203]:


type(df_merged)


# In[205]:


city_season_grouped


# In[204]:


type(city_season_grouped)


# In[160]:


df_matches.season.unique()


# In[162]:


df_matches.season.value_counts()


# In[165]:


df_matches


# In[172]:


df_matches["winner"].unique()


# In[174]:


df_matches.loc[(df_matches["season"]==2011)&(df_matches["winner"]=="Mumbai Indians")].shape


# In[179]:


opt_bat=df_matches.loc[df_matches["toss_decision"]=="bat"].shape[0]


# In[182]:


print(round((opt_bat/df_matches.shape[0])*100,1))


# In[184]:


opt_field_win=df_matches.loc[(df_matches["toss_decision"]=="field")&(df_matches["toss_winner"]==df_matches["winner"])].shape[0]


# In[185]:


opt_field_win


# In[186]:


opt_bat_win=df_matches.loc[(df_matches["toss_decision"]=="bat")&(df_matches["toss_winner"]==df_matches["winner"])].shape[0]
opt_bat_win


# In[191]:


l1=[2009,2017]


# In[194]:


df_merged.loc[(df_merged["season"].isin(l1))&(df_merged["inning"]==2)&(df_merged["winner"])].shape


# In[196]:


six_four=[6,4]


# In[198]:


df_s_f=df_merged.loc[(df_merged["season"]==2019)&(df_merged["batsman_runs"].isin(six_four))]


# In[199]:


type(df_s_f)


# In[207]:


gp_df_s_f.groupby("batsman")


# In[ ]:




