# Weather Data Collector

- This template is a Indian weather data collector which collects details for the mentioned locations in Districts.csv File. 
- This templates collects data for the state of tamil nadu which is located in India.
- Districts.csv can be modified to fetch the weather details of the locations as per our need.
- District_in_india.csv file has all the districts in india listed.

##Output
Output is generated in weather.csv File.

## Data is collected from Weather API
Weather API - https://www.weatherapi.com/

## Variables details

*You can also get the fields details for : https://www.weatherapi.com/docs/ *

| Field | Description |
| ----- | ----------- |
| name | Name of the Location |
| region | Region or state of the location, if available |
| country | Location country |
| lat | Latitude in decimal degree |
| lon | Longitude in decimal degree |
| tz_id | Time zone name |
| localtime_epoch | Local date and time in unix time |
| localtime | Local date and time |
| last_updated_epoch | Local time when the real time data was updated in unix time. |
| last_updated | Local time when the real time data was updated. |
| temp_c | Temperature in celsius |
| temp_f | Temperature in fahrenheit |
| is_day | 1 = Yes 0 = No,  Whether to show day condition icon or night icon |
| wind_mph | Wind speed in miles per hour |
| wind_kph | Wind speed in kilometer per hour |
| wind_degree | Wind direction in degrees |
| wind_dir | Wind direction as 16 point compass. e.g.: NSW |
| pressure_mb | Pressure in millibars |
| pressure_in | Pressure in inches |
| precip_mm | Precipitation amount in millimeters |
| precip_in | Precipitation amount in inches |
| humidity | Humidity as percentage |
| cloud | Cloud cover as percentage |
| feelslike_c | Feels like temperature in celsius |
| feelslike_f | Feels like temperature in fahrenheit |
| vis_km | Visibility in kilometer |
| vis_miles | Visibility in miles |
| uv | UV Index |
| gust_mph | Wind gust in miles per hour |
| gust_kph | Wind gust in kilometer per hour |
| text | Weather condition text |
| co | Carbon Monoxide (μg/m3) |
| no2 | Nitrogen dioxide (μg/m3) |
| o3 | Ozone (μg/m3) |
| so2 | Sulphur dioxide (μg/m3) |
| pm2_5 | PM2.5 (μg/m3) |
| pm10 | PM10 (μg/m3) |
| us-epa-index | US - EPA standard. 1 means Good 2 means Moderate 3 means Unhealthy for sensitive group 4 means Unhealthy 5 means Very Unhealthy 6 means Hazardous |
| gb-defra-index | UK Defra Index (See table below) |



## UK DEFRA INDEX Table										
										
| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :-----: | :---: | --| --| --| --| --| --| --| --| -- |
| **Band**  | Low | Low | Low | Moderate | Moderate | Moderate | High | High | High | Very High |
| **µgm-3** | 0-11 | 12-23 | 24-35 | 36-41 | 42-47 | 48-53 | 54-58 | 59-64 | 65-70 | 71 or more |
