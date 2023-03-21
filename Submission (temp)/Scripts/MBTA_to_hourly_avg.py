from numpy import full
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from pprint import pprint


# full_endpts = pd.read_csv("full_endpts.csv")
# full_endpts['dep_datetime'] = pd.to_datetime(full_endpts['dep_time'],unit='s')
# print (full_endpts.dtypes)
# full_endpts['dep_year'] = full_endpts['dep_datetime'].apply(lambda x: x.year)
# full_endpts['dep_month'] = full_endpts['dep_datetime'].apply(lambda x: x.month)
# full_endpts['dep_day'] = full_endpts['dep_datetime'].apply(lambda x: x.day)
# full_endpts['dep_hour'] = full_endpts['dep_datetime'].apply(lambda x: x.hour)
# print(full_endpts)

# full_endpts.to_csv("full_endpts.csv")

# full_endpts = pd.read_csv("MBTA_hr_avgs.csv")
# # full_endpts["date"] = list(zip((full_endpts["dep_year"], full_endpts["dep_month"], full_endpts["dep_day"], full_endpts["dep_hour"])))
# full_endpts['date'] = full_endpts[['dep_year', 'dep_month', 'dep_day', 'dep_hour']].apply(tuple, axis=1)
# full_endpts['u_line'] = full_endpts[['route_id', 'dep_stop_id']].apply(tuple, axis=1)

# full_endpts = full_endpts.pivot(index='date', columns='u_line', values=['avg_travel_time', 'num_trips'])
# full_endpts.columns = full_endpts.columns.to_flat_index()
# print(full_endpts)
# full_endpts.to_csv("MBTA_hr_avgs_byDT.csv")

# full_endpts = pd.read_csv("MBTA_hr_avgs_byDT.csv")
# print(full_endpts)