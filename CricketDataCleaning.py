#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Import Necessary Libraries
import pandas as pd
import json


# In[15]:


with open('t20_json_files/''t20_json_files/''t20_wc_match_results.json') as f:
    data = json.load(f)

df_match = pd.DataFrame(data[0]['matchSummary'])
df_match.head()


# In[17]:


df_match.shape


# In[21]:


df_match.rename({'scorecard' : 'match_id'}, axis = 1, inplace = True)
df_match.head()


# batting summary

# In[33]:


with open('t20_json_files/''t20_json_files/''t20_wc_batting_summary.json') as f:
    data = json.load(f)

    all_records = []

    for record in data:
        all_records.extend(record['battingSummary'])
        
df_batting = pd.DataFrame(all_records)
df_batting.head()


# In[74]:


#Convert dismissal column to out/not out
#df_batting['out_notout'] = df_batting.dismissal.apply(lambda x: "out" if len(x)>0 else "not_out")
#df_batting.drop(columns = ["dismissal"],inplace = True)
df_batting.iloc[650:681]


# In[77]:


#Remove special characters from name name column
df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x: x.replace('â€','')) 


# In[86]:


match_ids_dict = {}

for index,row in df_match.iterrows():
    key1 = row['team1'] + ' Vs ' + row['team2']
    key2 = row['team2'] + ' VS ' + row['team1']
    
    match_ids_dict[key1] = row["match_id"]
    match_ids_dict[key2] = row["match_id"]
    
match_ids_dict


# In[88]:


#Create a new column by "mapping" the dictionary to 
df_batting['mach_id'] = df_batting['match'].map(match_ids_dict)
df_batting.head()


# In[90]:


df_batting.to_csv('t20_csv_files/temp.csv',index = False)


# In[ ]:




