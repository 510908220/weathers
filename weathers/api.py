# -*- coding: utf-8 -*-

import requests
from .util import get_city_code, Error
from .weather import Weather


def get(province, city, county, day_index=1):
    city_id = get_city_code(province, city, county)
    if not city_id:
        raise Error("城市id不存在")

    url = "http://www.weather.com.cn/weather/{city_id}.shtml".format(city_id=city_id)
    r = requests.get(url)
    if r.status_code == 200:
        wea = Weather(r.text, day_index)
        print(wea.weather)



