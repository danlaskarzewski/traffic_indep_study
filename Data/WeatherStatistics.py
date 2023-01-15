import pandas as pd
import matplotlib.pyplot as plt


# https://open-meteo.com/en/docs/historical-weather-api#latitude=42.36&longitude=-71.06&start_date=2022-12-11&end_date=2023-01-09&hourly=temperature_2m 

# latitude,longitude,elevation,utc_offset_seconds,timezone,timezone_abbreviation
# 42.40001,-71.1,10.0,-18000,America/New_York,EST
# 2019-01-01 to 2023-01-01

hourly_data = pd.read_csv("BostonHourlyWeather.csv")
hourly_data["snowfall (inch)"] = hourly_data["snowfall (cm)"].div(2.54)
print("Total hourly row count: " + str(len(hourly_data)))
print(hourly_data[0:3])
print("\n\n\n")

daily_data = pd.read_csv("BostonDailyWeather.csv")
daily_data["snowfall_sum (inch)"] = daily_data["snowfall_sum (cm)"].div(2.54)
print("Total daily row count: " + str(len(daily_data)))
print(daily_data[0:3])
print("\n\n\n")

####################
# DESCRIPTIVE DATA (HR)
####################

hourly_mean = hourly_data[["temperature_2m (°F)","apparent_temperature (°F)","precipitation (inch)","rain (inch)","snowfall (cm)", "snowfall (inch)", "cloudcover (%)","windspeed_10m (mp/h)","winddirection_10m (°)","windgusts_10m (mp/h)","soil_moisture_0_to_7cm (m³/m³)"]].mean()
hourly_std = hourly_data[["temperature_2m (°F)","apparent_temperature (°F)","precipitation (inch)","rain (inch)","snowfall (cm)","snowfall (inch)","cloudcover (%)","windspeed_10m (mp/h)","winddirection_10m (°)","windgusts_10m (mp/h)","soil_moisture_0_to_7cm (m³/m³)"]].std()
hourly_median = hourly_data[["temperature_2m (°F)","apparent_temperature (°F)","precipitation (inch)","rain (inch)","snowfall (cm)","snowfall (inch)","cloudcover (%)","windspeed_10m (mp/h)","winddirection_10m (°)","windgusts_10m (mp/h)","soil_moisture_0_to_7cm (m³/m³)"]].median()
hourly_min = hourly_data[["temperature_2m (°F)","apparent_temperature (°F)","precipitation (inch)","rain (inch)","snowfall (cm)","snowfall (inch)","cloudcover (%)","windspeed_10m (mp/h)","winddirection_10m (°)","windgusts_10m (mp/h)","soil_moisture_0_to_7cm (m³/m³)"]].min()
hourly_max = hourly_data[["temperature_2m (°F)","apparent_temperature (°F)","precipitation (inch)","rain (inch)","snowfall (cm)","snowfall (inch)","cloudcover (%)","windspeed_10m (mp/h)","winddirection_10m (°)","windgusts_10m (mp/h)","soil_moisture_0_to_7cm (m³/m³)"]].max()

d_hr = {'Mean': hourly_mean}
desc_data_hr = pd.DataFrame(d_hr)
desc_data_hr['StD'] = hourly_std
desc_data_hr['Median'] = hourly_median
desc_data_hr['Min'] = hourly_min
desc_data_hr['Max'] = hourly_max

print(desc_data_hr)
print("\n\n\n")


####################
# DESCRIPTIVE DATA (DAY)
####################

daily_mean = daily_data[["temperature_2m_max (°F)","temperature_2m_min (°F)","rain_sum (inch)","snowfall_sum (cm)","snowfall_sum (inch)","precipitation_hours (h)","windspeed_10m_max (mp/h)","windgusts_10m_max (mp/h)"]].mean()
daily_std = daily_data[["temperature_2m_max (°F)","temperature_2m_min (°F)","rain_sum (inch)","snowfall_sum (cm)","snowfall_sum (inch)","precipitation_hours (h)","windspeed_10m_max (mp/h)","windgusts_10m_max (mp/h)"]].std()
daily_median = daily_data[["temperature_2m_max (°F)","temperature_2m_min (°F)","rain_sum (inch)","snowfall_sum (cm)","snowfall_sum (inch)","precipitation_hours (h)","windspeed_10m_max (mp/h)","windgusts_10m_max (mp/h)"]].median()
daily_min = daily_data[["temperature_2m_max (°F)","temperature_2m_min (°F)","rain_sum (inch)","snowfall_sum (cm)","snowfall_sum (inch)","precipitation_hours (h)","windspeed_10m_max (mp/h)","windgusts_10m_max (mp/h)"]].min()
daily_max = daily_data[["temperature_2m_max (°F)","temperature_2m_min (°F)","rain_sum (inch)","snowfall_sum (cm)","snowfall_sum (inch)","precipitation_hours (h)","windspeed_10m_max (mp/h)","windgusts_10m_max (mp/h)"]].max()

d_day = {'Mean': daily_mean}
desc_data_day = pd.DataFrame(d_day)
desc_data_day['StD'] = daily_std
desc_data_day['Median'] = daily_median
desc_data_day['Min'] = daily_min
desc_data_day['Max'] = daily_max

print(desc_data_day)
print("\n\n\n")

####################
# PLOTS (HR)
####################

temp_df_19_hr = hourly_data[["time", "temperature_2m (°F)","apparent_temperature (°F)"]].copy().head(365*24)
temp_df_19_hr['Temp SMA(72)'] = temp_df_19_hr["temperature_2m (°F)"].rolling(72).mean()
temp_df_19_hr['App_Temp SMA(72)'] = temp_df_19_hr["apparent_temperature (°F)"].rolling(72).mean()
temp_df_19_hr.set_index("time", inplace=True)
temp_df_19_hr.plot()

precip_df_19_hr = hourly_data[["time", "precipitation (inch)","rain (inch)","snowfall (inch)"]].copy().head(365*24)
precip_df_19_hr.set_index("time", inplace=True)
precip_df_19_hr.plot()

sky_df_19_hr = hourly_data[["windspeed_10m (mp/h)", "windgusts_10m (mp/h)", "winddirection_10m (°)", "cloudcover (%)"]].copy().head(365*24)
sky_df_19_hr.hist()

# plt.show(block=True)