# weather
根据中国天气网(http://www.weather.com.cn/)
获取相关天气数据

# 使用

```
>>> import weathers
>>> weathers.get("广东","珠海","珠海")
+----------+----------+------+
| 日期     | 天气状况 | 温度 |
+----------+----------+------+
| 今天19日 |   阵雨   | 25~  |
+----------+----------+------+
>>> weathers.get("广东","珠海","珠海",0) # 0代表一周天气，1-7代表今天，明天...
+----------+------------+-------+
| 日期     |  天气状况  |  温度 |
+----------+------------+-------+
| 今天19日 |    阵雨    |  25~  |
| 明天20日 | 大雨转暴雨  | 24~29 |
| 后天21日 |    暴雨    | 24~28 |
| 周五22日 | 大雨转阵雨  | 24~28 |
| 周六23日 |    阵雨    | 25~29 |
| 周日24日 |    阵雨    | 25~30 |
| 周一25日 | 阵雨转多云  | 26~30 |
+----------+------------+-------+
```
#Python Version
support  python 2.x and python 3.x
