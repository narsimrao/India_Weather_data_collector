try:
  import requests
  import json
  import numpy as np
  import pandas as pd
  import os.path
  from os import path
  import csv
  import sys
  import datetime

  district_df = pd.read_csv('Districts_in_india.csv')

  districts_all = district_df.iloc[:,1].values

  url_list = []
  for i in range(0,districts_all.size):
    district = str(districts_all[i])
    len_dist = district.split(" ")
    if len(len_dist) == 1:
      url_list.append('http://api.weatherapi.com/v1/current.json?key=9ac8e54e64434eafaa4175429210304&q='+ district +'&aqi=yes')
    else:
        continue

  failed_url_list = []

  for url in url_list:
      res = requests.get(url)
      if res.status_code == 200 and res.reason == 'OK':
        dt = res.json()
        location = dt['location']
        current = dt['current']

        loc = location['country']

        if str(loc).lower() != 'india':
            continue

        loc_df = pd.DataFrame(data=[location])
        curr_df = pd.DataFrame(data=[current])

        air_quality = {}
        condition = {}
        for key in current:
          if key == 'air_quality':
            air_quality = current[key]
          if key == 'condition':
            condition = current[key]

        air_quality_df = pd.DataFrame(data=[air_quality])
        condition_df = pd.DataFrame(data=[condition])

        weather_df = pd.concat([loc_df,curr_df,condition_df,air_quality_df],axis=1)

        weather_df.drop(labels=['air_quality','condition','icon','code'],axis=1,inplace=True,errors="ignore")

        if path.isfile('weather.csv') == True:
          weather_df.to_csv('weather.csv',index=False,header=False,mode='a')
        else:
          weather_df.to_csv('weather.csv',index=False)
      else:
          failed_url_list.append(url)

  dt = datetime.datetime.now()
  if path.isfile(r'Failure_count.txt') == True:
      f = open(r"Failure_count.txt", "a")
      f.write("\n---------------------------------------------------------------------\n")
      f.write("date : " + str(dt) + "\n\n")
      f.write("Failed Count : " + str(len(failed_url_list)) + "\n\n")
      f.write("\n---------------------------------------------------------------------")
      f.close()
  else:
      f = open(r"Failure_count.txt", "w")
      f.write("---------------------------------------------------------------------\n")
      f.write("date : " + str(dt) + "\n\n")
      f.write("Failed Count : " + str(len(failed_url_list)) + "\n\n")
      f.write(str(ex))
      f.write("\n---------------------------------------------------------------------")
      f.close()

except Exception as ex:
    dt = datetime.datetime.now()
    if path.isfile(r'Exception.txt') == True:
        f = open(r"Exception.txt","a")
        f.write("\n---------------------------------------------------------------------\n")
        f.write("date : "+ str(dt) + "\n\n")
        f.write(str(ex))
        f.write("\n---------------------------------------------------------------------")
        f.close()
    else:
        f = open(r"Exception.txt","w")
        f.write("---------------------------------------------------------------------\n")
        f.write("date : "+ str(dt) + "\n\n")
        f.write(str(ex))
        f.write("\n---------------------------------------------------------------------")
        f.close()
