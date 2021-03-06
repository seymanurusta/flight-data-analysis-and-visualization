# -*- coding: utf-8 -*-
"""flight

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lWCbecLOY6QPWJhdMA1HSaTuOFMKVDMq
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pandas import DataFrame 
from collections import Counter

#Apply the theme
sns.set_theme()

#Load dataset
from google.colab import files
dataset = files.upload()

#Load dataset
df=pd.read_csv("activity.csv")

df.rename(columns ={'cide':'code'},inplace=True)

df.head() #Return the first 5 rows

df.info() #Information about the data

df["code"].describe()

df["activity"].describe()

df["date"] = df["date"].astype('string') #Convert object to string
df["date"] = pd.to_datetime(df["date"], format="%d.%m.%Y %H:%M:%S") #Convert string to datetime
df['year'] = pd.to_datetime(df['date']).dt.year ##Convert datetime to year
df['month'] = pd.to_datetime(df['date']).dt.month #Convert datetime to month
df['day']= pd.to_datetime(df['date']).dt.day #Convert datetime to day of month
df['day name']= pd.to_datetime(df['date']).dt.day_name() #Convert datetime to day's name of week
df['hour'] = pd.to_datetime(df['date']).dt.hour #Convert datetime to hour

df["code"] = df["code"].astype('category') #Convert object to category
df["activity"] = df["activity"].astype('category') #Convert object to category
df["fleet"] = df["fleet"].astype('category') #Convert object to category
df["activity_definition"] = df["activity_definition"].astype('string') #Convert object to string

df.head()

df.info()

plt.figure(figsize=(15,8))
sns.countplot(x="hour", data=df, palette="Set1")
plt.xlabel("Hour", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Hour Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="hour", hue="definition", data=df, palette="Set1")
plt.xlabel("Hour", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Hour Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.kdeplot(data=df, x="hour")
plt.xlabel("Hour", fontsize=15)
plt.ylabel("Density", fontsize=15)
plt.title("Hour Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="day", data=df, palette="Set1")
plt.xlabel("Day", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Day Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="day", hue="definition", data=df, palette="Set1")
plt.xlabel("Day", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Day Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="day name", data=df, palette="Set1")
plt.xlabel("Day", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Day of the Week Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="day name", data=df, hue="definition", palette="Set1")
plt.xlabel("Day", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Day Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.kdeplot(data=df, x="day")
plt.xlabel("Day", fontsize=15)
plt.ylabel("Density", fontsize=15)
plt.title("Day Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="month", data=df, palette="Set1")
plt.xlabel("Month", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Month Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="month", data=df, hue="definition", palette="Set1")
plt.xlabel("Month", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Month Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="year", hue="definition", data=df, palette="Set1")
plt.xlabel("Year", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Year Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="code", hue="definition", data=df, palette="Set1")
plt.xlabel("Code", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Code Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,10))
sns.countplot(x="fleet", hue="fleet", data=df, palette="Set1")
plt.xlabel("Fleet", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Fleet Based Analysis", fontsize=20)
plt.show()

plt.figure(figsize=(15,8))
sns.countplot(x="fleet", hue="definition", data=df, palette="Set1")
plt.xlabel("Fleet", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Fleet Based Analysis", fontsize=20)
plt.show()

crew_id_list = df['crew_id'].tolist() #Convert a Dataframe Column to a List
counted_id = pd.value_counts(np.array(crew_id_list)) #Count id values in column

id = counted_id.to_dict() #Convert pandas series to a dictionary

first_ten_keys_id = list(id.keys())[:10]
first_ten_values_id = list(id.values())[:10]

crew = pd.DataFrame(
    {"crew id": first_ten_keys_id,
     "frequency": first_ten_values_id
    }) #Create dataframe

crew["crew id"] = crew["crew id"].astype('category') #Convert object to category

# the 10 most common element of crew id
ci = Counter(crew_id_list)

most_frequent_id = (ci.most_common(10)) 
print(most_frequent_id)

plt.figure(figsize=(15,8))
plt.bar(crew["crew id"], crew["frequency"], width = 0.5, color = ["green", "orange", "blue","red", "purple", "yellow","pink"])
 
plt.xlabel("Crew Id", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Crew Id Based Analysis", fontsize=20)
plt.show()

activity_list = df['activity_definition'].tolist() #Convert a Dataframe Column to a List
counted_activity = pd.value_counts(np.array(activity_list))

ac = counted_activity.to_dict() #Convert pandas series to a dictionary

first_ten_keys_ac = list(ac.keys())[:5]
first_ten_values_ac = list(ac.values())[:5]

act = pd.DataFrame(
    {"activity": first_ten_keys_ac,
     "activity frequency": first_ten_values_ac,
    }) #Create dataframe

act["activity"] = act["activity"].astype('category') #Convert object to category

# the 10 most common element of activity
d = Counter(activity_list)

most_frequent_departure = (d.most_common(5))
print(most_frequent_departure)

plt.figure(figsize=(15,8))
plt.bar(act["activity"], act["activity frequency"], width = 0.5, color = ["green", "orange", "blue","red", "purple", "yellow","pink"])
 
plt.xlabel("Activity", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Activity Based Analysis", fontsize=20)
plt.show()

#Create dataframe where activity definition is airport

df_filtered = df[df["activity_definition"] == "Airport"]

df_filtered

airport_list = df_filtered['activity'].tolist() #Convert a Dataframe Column to a List
counted_airport = pd.value_counts(np.array(airport_list))

aa = counted_airport.to_dict() #Convert pandas series to a dictionary

first_ten_keys_aa = list(aa.keys())[:10]
first_ten_values_aa = list(aa.values())[:10]

airport = pd.DataFrame(
    {"airport": first_ten_keys_aa,
     "airport frequency": first_ten_values_aa,
    }) #Create dataframe for where activity

airport["airport"] = airport["airport"].astype('category') #Convert object to category

unique_airport = df_filtered.activity.unique()
uniq_airport_list = unique_airport.tolist()
len(uniq_airport_list)

# the 10 most common of  Airport Activity

aa = Counter(airport_list)

most_frequent_airport = (aa.most_common(10)) 
print(most_frequent_airport)

plt.figure(figsize=(15,8))
plt.bar(airport["airport"], airport["airport frequency"], width = 0.5, color = ["green", "orange", "blue","red", "purple", "yellow","pink"])
 
plt.xlabel("Airport", fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.title("Airport Based Analysis", fontsize=20)
plt.show()

#list of airports

int_airport = {'CPH': 111, 'JFK': 98, 'ISU': 30, 'JED': 47, 'MIA': 77, 'LYS': 54, 'BOS': 30, 'BCN': 94, 'CCS': 31, 'MFM': 11, 'HEL': 54, 'NAP': 30, 'YUL': 14, 'FNA': 17, 'BGW': 72, 'KGF': 1, 'ZNZ': 13, 'CKY': 13, 'KHE': 24, 'BOG': 34, 'PRG': 69, 'HSA': 10, 'AWZ': 1, 'RIX': 31, 'TAS': 63, 'VNO': 76, 'HYD': 13, 'PRN': 73, 'RAK': 36, 'UIO': 5, 'KHI': 40, 'HKG': 26, 'ROV': 17, 'SVO': 8, 'LHE': 31, 'JIB': 17, 'HAM': 108, 'YVR': 13, 'IAD': 43, 'MRS': 50, 'NSI': 30, 'PNH': 4, 'LHR': 167, 'HRK': 24, 'VAR': 30, 'FIH': 25, 'KBP': 64, 'HAV': 12, 'MZR': 1, 'NIM': 24, 'LAD': 9, 'ZAG': 60, 'VIE': 138, 'KIV': 50, 'MAA': 18, 'SFO': 43, 'LAX': 60, 'MAD': 104, 'SYZ': 22, 'UBN': 13, 'BOM': 47, 'CMN': 34, 'EDI': 32, 'AER': 12, 'SKP': 57, 'TGD': 60, 'LIS': 60, 'OMH': 8, 'CMB': 47, 'SKD': 13, 'SKG': 28, 'BEY': 119, 'DEL': 51, 'BER': 143, 'IFN': 22, 'ALA': 152, 'VCE': 43, 'SCO': 13, 'AMM': 79, 'CEB': 13, 'MRU': 17, 'JNB': 31, 'UGC': 4, 'CPT': 17, 'VLC': 33, 'TNR': 5, 'AMD': 8, 'SIN': 40, 'DMM': 13, 'SZX': 13, 'MNL': 56, 'OSL': 66, 'PTY': 30, 'AMS': 226, 'AGP': 60, 'ABJ': 30, 'BUD': 70, 'DLA': 30, 'GRU': 56, 'HND': 30, 'BRI': 17, 'MHD': 31, 'BLQ': 44, 'SXB': 12, 'DSS': 48, 'BLL': 23, 'EWR': 30, 'SHJ': 21, 'BLR': 13, 'LJU': 48, 'BRE': 35, 'SVX': 13, 'TBZ': 38, 'KTM': 21, 'TBS': 122, 'LBV': 21, 'MXP': 142, 'NQZ': 22, 'MGQ': 30, 'SSH': 58, 'OPO': 35, 'LCK': 12, 'NVI': 7, 'ACC': 34, 'DOH': 60, 'ODS': 58, 'ABV': 30, 'LUX': 22, 'ATL': 30, 'ATH': 90, 'KUL': 50, 'TPE': 36, 'CTA': 22, 'MUC': 114, 'PEK': 29, 'ISB': 30, 'COO': 30, 'DBV': 15, 'CGK': 30, 'NCE': 43, 'NJF': 14, 'CGN': 159, 'ECN': 374, 'OUA': 60, 'BKO': 32, 'SEZ': 13, 'BSR': 16, 'BKK': 58, 'BSL': 69, 'ASB': 12, 'IKA': 199, 'NBO': 51, 'PVG': 23, 'SNN': 2, 'NUE': 59, 'ASM': 13, 'FCO': 90, 'TLS': 22, 'FEG': 8, 'FRA': 166, 'NDJ': 23, 'TLV': 304, 'CLJ': 30, 'AUH': 30, 'DUB': 71, 'KRW': 1, 'KRT': 52, 'BEG': 98, 'SJJ': 81, 'ADD': 29, 'FRU': 143, 'WAW': 40, 'CUN': 30, 'DUS': 157, 'TLL': 36, 'MED': 42, 'RUH': 26, 'CDG': 198, 'LED': 91, 'HBE': 38, 'ALG': 34, 'BRU': 122, 'BJL': 8, 'OZH': 17, 'YYZ': 29, 'SOF': 90, 'TUN': 43, 'ORD': 90, 'KZN': 26, 'MEX': 38, 'LWO': 25, 'PNR': 8, 'DPS': 14, 'MST': 24, 'HAJ': 67, 'MSQ': 17, 'LOS': 47, 'CAI': 99, 'CAN': 33, 'GNJ': 9, 'BAH': 65, 'IAH': 38, 'BIO': 17, 'GYD': 154, 'HAN': 22, 'DAC': 73, 'KWI': 95, 'DYU': 8, 'DAR': 22, 'SGN': 25, 'DFW': 17, 'BOD': 18, 'AQJ': 12, 'MLA': 59, 'ICN': 32, 'MLE': 60, 'STN': 102, 'GVA': 79, 'DWC': 26, 'CND': 20, 'NAJ': 9, 'STR': 140, 'VKO': 294, 'GOT': 46, 'ZRH': 131, 'SZG': 21, 'NKC': 30, 'HRG': 60, 'KBL': 17, 'EBB': 29, 'ROB': 2, 'EBL': 68, 'MAN': 76, 'KGL': 22, 'BHX': 64, 'DXB': 115, 'BUS': 29, 'OTP': 95, 'EZE': 17, 'MCT': 44, 'LGW': 98, 'ARN': 89}

dom_airport = {'BGG': 33, 'MQM': 86, 'GNY': 111, 'KSY': 58, 'MSR': 49, 'ERZ': 110, 'IST': 21471, 'ISL': 5, 'NAV': 107, 'DIY': 175, 'ERC': 57, 'BAL': 74, 'ANK': 57, 'ISE': 14, 'CKZ': 14, 'ASR': 286, 'KFS': 26, 'TZX': 362, 'KYA': 117, 'SZF': 142, 'KCM': 52, 'VAS': 71, 'TEQ': 1, 'SXZ': 22, 'ONQ': 7, 'SAW': 3372, 'YEI': 22, 'VAN': 131, 'YKO': 35, 'DLM': 230, 'ADF': 36, 'AJI': 46, 'IGD': 44, 'ADB': 627, 'ESB': 1787, 'ADA': 495, 'AYT': 1193, 'MLX': 86, 'DNZ': 88, 'KZR': 17, 'OGU': 155, 'NOP': 21, 'TJK': 20, 'EDO': 30, 'EZS': 96, 'BJV': 258, 'NKT': 67, 'GZP': 84, 'GZT': 337, 'MZH': 23, 'KCO': 3, 'HTY': 131}

int_ratios = {}
dom_ratios = {}  
for airport, counts in most_frequent_airport:
  if airport in int_airport:
    total_count = int_airport[airport]
    ratio = counts / total_count
    int_ratios[airport] = round(ratio * 100, 2)
  
  elif airport in dom_airport:
    total_count = dom_airport[airport]
    ratio = counts / total_count
    dom_ratios[airport] = round(ratio * 100, 2)

keys_dom = list(dom_ratios.keys())
values_dom= list(dom_ratios.values())

dom_df = pd.DataFrame(
    {"domestic airport": keys_dom,
     "frequency": values_dom,
    }) #Create dataframe for where activity
  

dom_df["domestic airport"] = dom_df["domestic airport"].astype('category') #Convert object to category

sorted_dom = dom_df.sort_values(by="frequency",ascending=False)
dom = sorted_dom.head(10)

plt.figure(figsize=(15,8))
plt.bar(dom["domestic airport"], dom["frequency"], width = 0.5, color = ["green", "orange", "blue","red", "purple", "yellow","pink"])
 
plt.xlabel("Domestic Airport", fontsize=15)
plt.ylabel("Ratio", fontsize=15)
plt.title("Domestic Airport Based Analysis", fontsize=20)
plt.show()

keys_int = list(int_ratios.keys())
values_int= list(int_ratios.values())

int_df = pd.DataFrame(
    {"international airport": keys_int,
     "frequency": values_int,
    }) #Create dataframe for where activity
  

int_df["international airport"] = int_df["international airport"].astype('category') #Convert object to category

sorted_int = int_df.sort_values(by="frequency",ascending=False)
int = sorted_int.head(10)

plt.figure(figsize=(15,8))
plt.bar(int["international airport"], int["frequency"], width = 0.5, color = ["green", "orange", "blue","red", "purple", "yellow","pink"])
 
plt.xlabel("International Airport", fontsize=15)
plt.ylabel("Ratio", fontsize=15)
plt.title("International Airport Based Analysis", fontsize=20)
plt.show()

emp_cabin = 12750
emp_320 = 1240
emp_340 = 975
emp_738 = 1430 
emp_777 = 959

#Filtered dataframe for Fleet:Cabin

filtered_cabin = df_filtered[df_filtered["fleet"] == "Cabin"]

unique_cabin = filtered_cabin.crew_id.unique()
uniq_cabin_list = unique_cabin.tolist()
len(uniq_cabin_list)

#Filtered dataframe for Fleet:320

filtered_320 = df_filtered[df_filtered["fleet"] == "320"]

unique_320 = filtered_320.crew_id.unique()
uniq_320_list = unique_320.tolist()
len(uniq_320_list)

#Filtered dataframe for Fleet:340

filtered_340 = df_filtered[df_filtered["fleet"] == "340"]

unique_340 = filtered_340.crew_id.unique()
uniq_340_list = unique_340.tolist()
len(uniq_340_list)

#Filtered dataframe for Fleet:738

filtered_738 = df_filtered[df_filtered["fleet"] == "738"]

unique_738 = filtered_738.crew_id.unique()
uniq_738_list = unique_738.tolist()
len(uniq_738_list)

#Filtered dataframe for Fleet:77

filtered_777 = df_filtered[df_filtered["fleet"] == "777"]

unique_777 = filtered_777.crew_id.unique()
uniq_777_list = unique_777.tolist()
len(uniq_777_list)

#fleet employee rates

f_cabin = round((len(uniq_cabin_list)/emp_cabin)* 100, 2)
f_320 = round((len(uniq_320_list)/emp_320)* 100, 2)
f_340 = round((len(uniq_340_list)/emp_340)* 100, 2)
f_738 = round((len(uniq_738_list)/emp_738)* 100, 2)
f_777 = round((len(uniq_777_list)/emp_777)* 100, 2)

fleet = {"Cabin":f_cabin, 
         "320":f_320,
         "340":f_340,
         "738":f_cabin,
         "777":f_777}

fleet

f_key= fleet.keys()
f_value= fleet.values()

fleet_df = pd.DataFrame(
    {"fleet": f_key,
     "ratio": f_value,
    }) 
  

fleet_df["fleet"] = fleet_df["fleet"].astype('category') #Convert object to category

plt.figure(figsize=(15,8))
plt.bar(fleet_df["fleet"], fleet_df["ratio"], width = 0.5, color = ["green", "orange", "blue","red", "purple", "yellow","pink"])
 
plt.xlabel("Fleet", fontsize=15)
plt.ylabel("Percentage", fontsize=15)
plt.title("Fleet Based Analysis", fontsize=20)
plt.show()

