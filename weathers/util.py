# -*- coding: utf-8 -*-
import os
import sys

_ver = sys.version_info

#:Python 2.x
is_py2 = (_ver[0] == 2)

if is_py2:
    import codecs
    open = codecs.open

def get_city_code(province, city, county):
    """
    :param province: 一级城市(省)
    :param city: 二级城市(市)
    :param county: 三级城市(县)
    :return:城市id
    """

    def get_city_ids():
        city_id_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "city_id.py")
        city_ids = {}
        with open(city_id_path, encoding="utf-8") as f:
            for line in f:
                line = line.encode('utf-8') if is_py2 else line
                city_id, county, city, province = line.split(",")
                key = province.strip() + city.strip() + county.strip()
                city_ids[key] = city_id.strip()
        return city_ids

    city_ids = get_city_ids()
    key = province.strip() + city.strip() + county.strip()
    if key in city_ids:
        return city_ids[key]


class Error(Exception):
    def __init__(self, error):
        self.error_ = error

    def __str__(self):
        return repr(self.error_)






