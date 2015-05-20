# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from prettytable import PrettyTable


class DayWeatherInfo(object):
    __slots__ = ['day_des_', 'day_num_', 'day_wea_', 'day_temperature_high_', 'day_temperature_low_']

    def __init__(self, day_des, day_num, day_wea, day_temperature_high, day_temperature_low):
        self.day_des_ = day_des
        self.day_num_ = day_num
        self.day_wea_ = day_wea
        self.day_temperature_high_ = day_temperature_high
        self.day_temperature_low_ = day_temperature_low


def parse(weather_data):
    soup = BeautifulSoup(weather_data)
    div_7d = soup.find("div", {'id': "7d"})
    weather_infos = []
    if div_7d:
        for day_index in range(1, 8):
            day_item = div_7d.find("li", {'data-dn': ("7d" + str(day_index))})

            day_des = day_item.find("h1").text
            day_num = day_item.find("h2").text
            day_wea = day_item.find("p", {"class": "wea"}).text
            day_temperature_high = day_item.find("p", {"class": "tem tem1"}).find("span").text
            day_temperature_low = day_item.find("p", {"class": "tem tem2"}).find("span").text

            weather_infos.append(
                DayWeatherInfo(day_des, day_num, day_wea, day_temperature_high, day_temperature_low))
    return weather_infos


class Weather(object):
    def __init__(self, weather_data, day_index):
        self.weather_infos_ = parse(weather_data)
        self.day_index_ = day_index
        self.__create_pretty_table()

    def __create_pretty_table(self):
        pretty_table = PrettyTable(["日期", "天气状况", "温度"])
        pretty_table.align["日期"] = "l"
        pretty_table.padding_width = 1
        return pretty_table

    @property
    def weather(self):
        pretty_table = self.__create_pretty_table()
        if 1 <= self.day_index_ <= 7:
            weather_info = self.weather_infos_[self.day_index_ - 1]
            pretty_table.add_row(["".join([weather_info.day_des_, weather_info.day_num_]), weather_info.day_wea_,
                                  "~".join(
                                      [weather_info.day_temperature_low_, weather_info.day_temperature_high_])])
        else:
            for weather_info in self.weather_infos_:
                pretty_table.add_row(["".join([weather_info.day_des_, weather_info.day_num_]), weather_info.day_wea_,
                                      "~".join(
                                          [weather_info.day_temperature_low_, weather_info.day_temperature_high_])])
        return str(pretty_table)







