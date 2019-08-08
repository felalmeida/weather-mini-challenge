#!/usr/bin/python
# -*- coding: UTF-8 -*-
###############################################################################
# Module:   WeatherMiniChallenge.py    Autor: Felipe Almeida                  #
# Start:    29-Jul-2019                Last Update: 29-Jul-2019  Version: 1.0 #
###############################################################################

import sys
import requests
import json
from datetime import datetime, timezone
import calendar

OWM_ApiKey = '11111111111111111111111111111111'
OWM_EndPoint = 'api.openweathermap.org'
OWM_Version = '2.5'
OWM_GlobalUrl = 'https://'+OWM_EndPoint+'/data/'+OWM_Version+'/'


def GetWeatherForecast(v_CityId=-1):
    global OWM_ApiKey, OWM_GlobalUrl

    StrReturn = ''
    PrevWeekDay = ''

    if v_CityId == -1:
        return -1
    else:
        Url = OWM_GlobalUrl + 'forecast'
        QueryString = {
            'APPID': OWM_ApiKey,
            'id': v_CityId,
            'cnt': 40  # 5 days, 3 Hours Interval
        }
        Headers = {
            'User-Agent': "Mozilla/5.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "openweathermap.org",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        Response = requests.request("GET", Url, headers=Headers,
                                    params=QueryString)
        jResponse = json.loads(Response.text)
        # print(json.dumps(jResponse, indent=4, sort_keys=True))
        CityName = jResponse['city']['name']+', '+jResponse['city']['country']
        for jDay in jResponse['list']:
            UnixTSDate = jDay['dt']
            Humidity = jDay['main']['humidity']
            dtDataDate = datetime.fromtimestamp(UnixTSDate, timezone.utc)
            StrWeekDay = calendar.day_name[dtDataDate.weekday()]
            StrDataHour = dtDataDate.strftime("%H")

            if (Humidity > 70):
                if (StrWeekDay == PrevWeekDay):
                    StrReturn = StrReturn+StrDataHour+','
                else:
                    StrReturn = (StrReturn[:-1] + '), ' + StrWeekDay +
                                 ' @('+StrDataHour+',')
                PrevWeekDay = StrWeekDay

    StrReturn = StrReturn[2:-1].strip() + ')'
    print('You should take an umbrella in "' + CityName +
          '" in these days/hours: ' + StrReturn)
    return 0


def GetCityId(v_CityName='São Paulo'):
    global OWM_ApiKey, OWM_GlobalUrl

    CityCode = 0
    Url = OWM_GlobalUrl + 'weather'
    QueryString = {
        'APPID': OWM_ApiKey,
        'q': v_CityName
    }
    Headers = {
        'User-Agent': "Mozilla/5.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "openweathermap.org",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    Response = requests.request("GET", Url, headers=Headers,
                                params=QueryString)
    jResponse = json.loads(Response.text)
    try:
        if v_CityName == jResponse['name']:
            CityCode = jResponse['id']
    except:
        CityCode = -1

    return CityCode


def MainProcess():
    CityName = 'Ribeirão Preto'

    if (GetWeatherForecast(GetCityId(CityName)) == -1):
        print('Invalid City Name')
        sys.exit(1)


def main():
    try:
        MainProcess()
        sys.exit(0)
    except KeyboardInterrupt:
        print("Weather Mini Challenge Interrupted!")
        sys.exit(1)


if __name__ == "__main__":
    main()
