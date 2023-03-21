import pandas as pd
import matplotlib.pyplot as plt
import datetime, time
from pprint import pprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


# lr_data_q1 = pd.read_csv("MBTA/Events_2022/2022-01_LREvents.csv")
# lr_data_q2 = pd.read_csv("MBTA/Events_2022/2022-02_LREvents.csv")
# lr_data_q3 = pd.read_csv("MBTA/Events_2022/2022-03_LREvents.csv")
# lr_data_q4 = pd.read_csv("MBTA/Events_2022/2022-04_LREvents.csv")
# lr_data_q5 = pd.read_csv("MBTA/Events_2022/2022-05_LREvents.csv")
# lr_data_q6 = pd.read_csv("MBTA/Events_2022/2022-06_LREvents.csv")
# lr_data_q7 = pd.read_csv("MBTA/Events_2022/2022-07_LREvents.csv")
# lr_data_q8 = pd.read_csv("MBTA/Events_2022/2022-08_LREvents.csv")
# lr_data_q9 = pd.read_csv("MBTA/Events_2022/2022-09_LREvents.csv")
# lr_data_q10 = pd.read_csv("MBTA/Events_2022/2022-10_LREvents.csv")
# lr_data_q11 = pd.read_csv("MBTA/Events_2022/2022-11_LREvents.csv")
# # lr_data_q12 = pd.read_csv("MBTA/Events_2022/2022-12_LREvents.csv")

# hr_data_q1 = pd.read_csv("MBTA/Events_2022/2022-01_HREvents.csv")
# hr_data_q2 = pd.read_csv("MBTA/Events_2022/2022-02_HREvents.csv")
# hr_data_q3 = pd.read_csv("MBTA/Events_2022/2022-03_HREvents.csv")
# hr_data_q4 = pd.read_csv("MBTA/Events_2022/2022-04_HREvents.csv")
# hr_data_q5 = pd.read_csv("MBTA/Events_2022/2022-05_HREvents.csv")
# hr_data_q6 = pd.read_csv("MBTA/Events_2022/2022-06_HREvents.csv")
# hr_data_q7 = pd.read_csv("MBTA/Events_2022/2022-07_HREvents.csv")
# hr_data_q8 = pd.read_csv("MBTA/Events_2022/2022-08_HREvents.csv")
# hr_data_q9 = pd.read_csv("MBTA/Events_2022/2022-09_HREvents.csv")
# hr_data_q10 = pd.read_csv("MBTA/Events_2022/2022-10_HREvents.csv")
# hr_data_q11 = pd.read_csv("MBTA/Events_2022/2022-11_HREvents.csv")
# # hr_data_q12 = pd.read_csv("MBTA/Events_2022/2022-12_HREvents.csv")

# print(len(lr_data_q1.columns))
# print(len(lr_data_q1))

# lr_data = pd.concat([lr_data_q1, lr_data_q2, lr_data_q3, lr_data_q4, lr_data_q5, lr_data_q6, lr_data_q7, lr_data_q8, lr_data_q9, lr_data_q10, lr_data_q11], ignore_index=True)
# hr_data = pd.concat([hr_data_q1, hr_data_q2, hr_data_q3, hr_data_q4, hr_data_q5, hr_data_q6, hr_data_q7, hr_data_q8, hr_data_q9, hr_data_q10, hr_data_q11], ignore_index=True)
# lr_data["train_type"] = "LR"
# hr_data["train_type"] = "HR"


# full_data_19 = pd.concat([lr_data, hr_data])
# print(full_data_19)
# full_data_19.index.name = 'row_num'

# # full_data_19 = full_data_19.drop(full_data_19.columns[[0]], axis=1)
# # full_data_19['unix_date'] = pd.to_datetime(full_data_19['service_date']).map(pd.Timestamp.timestamp)

# # print(full_data_19)
# # full_data_19['unix_start_time'] = full_data_19[['start_time_sec', 'unix_date']].sum(axis=1)
# # print(full_data_19)
# # full_data_19.to_csv("MBTA/temp_TravelTimes_2019.csv")
# full_data_19 = full_data_19.sort_values(by=['event_time'])

# # full_data_19 = full_data_19.drop(columns=["Unnamed: 0"])
# full_data_19.to_csv("MBTA/FullEvents_2022.csv")


full_data_19 = pd.read_csv("MBTA/FullEvents_2019.csv")
print(len(full_data_19))
full_data_20 = pd.read_csv("MBTA/FullEvents_2020.csv")
print(len(full_data_20))
# full_data_19.index.name = 'del'

# full_data_19.to_csv("MBTA/FullEvents_2021.csv")
# travel_data = pd.read_csv("MBTA/temp_TravelTimes_2019.csv")
# travel_data.index.name = 'index'

# travel_data = travel_data.drop(travel_data.columns[[0]], axis=1)
# print(travel_data['unix_start_time'])
# travel_data.to_csv("MBTA/temp_TravelTimes_2019.csv")


# filter by end terminals
# filter by train
# make pairs of line data 
# calc avg time of line per hour for each line