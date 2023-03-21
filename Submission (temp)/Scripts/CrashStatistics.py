from subprocess import check_output
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from pprint import pprint

from sqlalchemy import all_


# data_19 = pd.read_csv("2019_Crash_Level_Details.csv")
# data_20 = pd.read_csv("2020_Crashes.csv")
# data_21 = pd.read_csv("2021_Crashes.csv")
# data_22 = pd.read_csv("2022_Crashes.csv")

# data_19['CRASH_DATETIME'] = data_19['CRASH_DATE']

# data_19_22 = pd.concat([data_19, data_20, data_21, data_22], ignore_index=True)
# print(data_19_22['CRASH_DATETIME'])
# print(len(data_19_22.columns))

# boston_data = data_19_22[data_19_22['CITY_TOWN_NAME']=='BOSTON']
# boston_data.to_csv("Boston_Crashes_full.csv")



# boston_data = pd.read_csv("Boston_Crashes_full.csv")
# print(len(boston_data.columns))
# print(len(boston_data))

# # drop columns with more than n missing rows
# boston_data = boston_data.dropna(thresh=len(boston_data)-1000, axis=1)
# print(len(boston_data.columns))
# print(len(boston_data))

# # drop other columns with irrelevant data
# boston_data = boston_data[["OBJECTID", "CRASH_DATE_TEXT", "CRASH_TIME_2", "CRASH_DATETIME", "AGE_DRVR_YNGST", "AGE_DRVR_OLDEST", "MAX_INJR_SVRTY_CL", "NUMB_NONFATAL_INJR", "NUMB_FATAL_INJR", "AMBNT_LIGHT_DESCR", "WEATH_COND_DESCR", "ROAD_SURF_COND_DESCR", "NUMB_VEHC", "VEHC_TRVL_DIRC_CL", "RDWY", "RDWY_JNCT_TYPE_DESCR", "TRAFY_DESCR_DESCR", "NUM_LANES", "OPP_LANES", "F_F_CLASS", "FACILITY"]].copy()
# boston_data.to_csv("Boston_Crashes_test.csv")

# columns of interest:
# OBJECTID, CRASH_DATE_TEXT, CRASH_TIME_2, CRASH_DATETIME, AGE_DRVR_YNGST, AGE_DRVR_OLDEST, MAX_INJR_SVRTY, NUMB_NONFATAL_INJR, NUM_FATAL_INJR, AMBNT_LIGHT_DESCR, WEATH_COND_DESCR, ROAD_SURF_COND_DESCR, NUMB_VEHC, VEHC_TRVL_DIRC_CL, RDWY, RDWY_JNCT_TYPE_DESCR, TRAFY_DESCR_DESCR, NUM_LANES, OPP_LANES, F_F_CLASS, FACILITY

# potentials:
# MANR_COLL_DESCR, MOST_HRMFL_EVT_CL, VEHC_CONFIG_CL, VEHC_TOWED_FROM_SCENE_CL, HIT_RUN_DESCR, WORK_ZONE_RELD_DESCR, SURFACE_WD, MED_TYPE, 


# bos_crash_data = pd.read_csv("Boston_Crashes_test.csv")
# bos_crash_data['datetime'] = bos_crash_data['CRASH_DATETIME'] 
# bos_crash_data['datetime'] = pd.to_datetime(bos_crash_data['datetime'], errors='coerce', format='%Y-%m-%dT%H:%M')
# bos_crash_data['datetime'] = bos_crash_data['datetime'].dt.tz_localize(None)
# print(bos_crash_data.dtypes)
# bos_crash_data.set_index('datetime', inplace=True)
# print(bos_crash_data)

# bos_weather_data = pd.read_csv("BostonHourlyWeather.csv")
# bos_weather_data['datetime'] = bos_weather_data['time'] 
# bos_weather_data['datetime'] =  pd.to_datetime(bos_weather_data['datetime'], errors='coerce', format='%Y-%m-%dT%H:%M')
# bos_weather_data.set_index('datetime', inplace=True)
# print(bos_weather_data.dtypes)
# print(bos_weather_data)

# bos_combined = pd.DataFrame(columns=["b", "b", "OBJECTID","CRASH_DATE_TEXT","CRASH_TIME_2","CRASH_DATETIME","AGE_DRVR_YNGST","AGE_DRVR_OLDEST","MAX_INJR_SVRTY_CL","NUMB_NONFATAL_INJR","NUMB_FATAL_INJR","AMBNT_LIGHT_DESCR","WEATH_COND_DESCR","ROAD_SURF_COND_DESCR","NUMB_VEHC","VEHC_TRVL_DIRC_CL","RDWY","RDWY_JNCT_TYPE_DESCR","TRAFY_DESCR_DESCR","NUM_LANES","OPP_LANES","F_F_CLASS","FACILITY","datetime","b", "time","temperature_2m (°F)","apparent_temperature (°F)","precipitation (inch)","rain (inch)","snowfall (cm)","cloudcover (%)","windspeed_10m (mp/h)","winddirection_10m (°)","windgusts_10m (mp/h)","soil_moisture_0_to_7cm (m³/m³)", "datetime"])
# bos_combined = bos_combined.combine_first(bos_crash_data)
# bos_combined['datetime'] = pd.to_datetime(bos_combined['datetime'], errors='coerce', format='%Y-%m-%dT%H:%M')
# print(bos_combined.dtypes)

# for row in bos_crash_data.itertuples():
#     ts = row[-1]
#     c_hour_stamp = (ts.year, ts.month, ts.day, ts.hour)

#     for row2 in bos_weather_data.itertuples():
#        ts2 = row2[-1]
#        w_hour_stamp = (ts2.year, ts2.month, ts2.day, ts2.hour)
#     #    print(w_hour_stamp)
    
#        if w_hour_stamp == c_hour_stamp:
#            row_full = row + row2
#            bos_combined.loc[len(bos_combined.index)] = list(row_full)
#            print(len(bos_combined))
#            break
           


    

# bos_combined = pd.concat([bos_weather_data, bos_crash_data])
# # # # bos_combined.set_index('datetime', inplace=True)
# bos_combined.drop(columns=['Unnamed: 0'], inplace=True)
# # print(bos_combined.dtypes)
# print(bos_combined)
# bos_combined.to_csv("Boston_CrashWeather_temp.csv")

# bos_data = pd.read_csv("Boston_CrashWeather_temp.csv")
# bos_data['datetime'] = pd.to_datetime(bos_data['datetime'], errors='coerce')
# print(bos_data.dtypes)
# bos_data.set_index('datetime', inplace=True)
# bos_data = bos_data.sort_index()
# print(bos_data)
# bos_data.to_csv("Boston_CrashWeather_byDT.csv")

# bos_data = pd.read_csv("Boston_CrashWeather_byDT.csv")
# bos_data['ROAD_SURF_COND_DESCR'].value_counts().plot(kind='bar')
# bos_data.groupby('AMBNT_LIGHT_DESCR').size().plot(kind='bar')
# plt.show(block=True)

# features = ["row_num"]

# VariablesToOneHot=["AGE_DRVR_YNGST", "AGE_DRVR_OLDEST", "MAX_INJR_SVRTY_CL", "AMBNT_LIGHT_DESCR", "ROAD_SURF_COND_DESCR", "RDWY_JNCT_TYPE_DESCR", "TRAFY_DESCR_DESCR", "F_F_CLASS", "FACILITY"]
# # COLUMNS REMAINING CATEGORICAL: WEATH_COND_DESCR, VEHC_TRVL_DIRC_CL, RDWY

# for f in VariablesToOneHot:
#     one_hot = pd.get_dummies(bos_data[f])
#     one_hot = one_hot.add_prefix(f+"_")
#     # print(one_hot)
#     features = features + one_hot.columns.tolist()
#     bos_data = bos_data.join(one_hot)

# print(bos_data)
# bos_data.to_csv("temp_Boston_CrashWeather_byDT.csv")

# cw_data = pd.read_csv("temp_Boston_CrashWeather_byDT.csv")
# mbta_data = pd.read_csv("MBTA_hr_avgs_byDT.csv")
# bos_combined = pd.DataFrame(columns=(["b"] + list(cw_data.columns) + ["b"] + list(mbta_data.columns)))
# print(len(bos_combined.columns))
# # print(bos_combined)

# for row in cw_data.itertuples():
#     c_hour_stamp = str((row[-4], row[-3], row[-2], row[-1]))

#     for row2 in mbta_data.itertuples():
#         w_hour_stamp = row2[1]

#         if w_hour_stamp == c_hour_stamp:
#             print(w_hour_stamp)
#             row_full = row + row2
#             bos_combined.loc[len(bos_combined.index)] = list(row_full)
#             print(len(bos_combined))
#             break
           
# print(bos_combined)
# bos_combined.to_csv("temp_Boston_ALL_byDT.csv")

# all_data = pd.read_csv("temp_Boston_ALL_byDT.csv")
# cols = all_data.columns
# new_cols = []

# #('num_trips', ('Red', 70088))
# for cl in cols:
#     try:
#         c = tuple(map(str, cl.split(', ')))
#         t = (c[1] + "_" + c[2] + "_" +c[0]).replace('(','').replace(')','').replace("'",'')
#         print(t)
#         new_cols.append(t)
#     except:
#         print(cl)
#         new_cols.append(cl)
#         print("skipped: " + str(c))

# print(new_cols)
# all_data.columns = new_cols
# print(all_data)
# all_data.to_csv("Boston_ALL_byDT.csv")

# all_data = pd.read_csv("Boston_ALL_byDT.csv")
# all_data["Blue_70059_norm_travel_time"] = 1161.3607 - all_data["Blue_70059_avg_travel_time"]
# all_data["Blue_70038_norm_travel_time"] = 1207.9939 - all_data["Blue_70038_avg_travel_time"]
# all_data["Green-B_70154_norm_travel_time"] = 972.8414 - all_data["Green-B_70154_avg_travel_time"]
# all_data["Green-C_70154_norm_travel_time"] = 1021.1364 - all_data["Green-C_70154_avg_travel_time"]
# all_data["Green-D_70154_norm_travel_time"] = 1044.9637 - all_data["Green-D_70154_avg_travel_time"]
# all_data["Green-E_70154_norm_travel_time"] = 1006.6679 - all_data["Green-E_70154_avg_travel_time"]
# all_data["Green-B_70210_norm_travel_time"] = 1034.5550 - all_data["Green-B_70210_avg_travel_time"]
# all_data["Green-C_70210_norm_travel_time"] = 1098.2164 - all_data["Green-C_70210_avg_travel_time"]
# all_data["Green-D_70210_norm_travel_time"] = 1113.0510 - all_data["Green-D_70210_avg_travel_time"]
# all_data["Green-E_70210_norm_travel_time"] = 1065.5288 - all_data["Green-E_70210_avg_travel_time"]
# all_data["Red_70088_norm_travel_time"] = 1762.9007 - all_data["Red_70088_avg_travel_time"]
# all_data["Red_70063_norm_travel_time"] = 1689.5010 - all_data["Red_70063_avg_travel_time"]
# all_data["Orange_70003_norm_travel_time"] = 2171.0569 - all_data["Orange_70003_avg_travel_time"]
# all_data["Orange_70034_norm_travel_time"] = 2100.3642 - all_data["Orange_70034_avg_travel_time"]
# all_data.to_csv("Boston_ALL_norm_byDT.csv")

all_data = pd.read_csv("../Boston_ALL_norm_byDT.csv")
all_data.set_index("I1", inplace=True)
# print(all_data)

early = -600
late = 600

for i in range (157, 171):
    col = all_data.iloc[:, i]
    print(col.name)

    start = "_".join(col.name.split("_", 2)[:2])
    early_name = start + "_Early"
    late_name = start + "_Late"

    all_data.loc[all_data[col.name] > late, late_name] = 1
    all_data.loc[all_data[col.name] < early, early_name] = 1


all_data.to_csv("TEMP10m_Boston_ALL_norm_byDT.csv")
