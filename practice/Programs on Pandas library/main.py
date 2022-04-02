# with open ("weather_data.csv") as weather_csv_file:
#     print(weather_csv_file.readlines())
#

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for x in data:
#         if x[1] != "temp":
#             temperature.append(int(x[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].tolist()
average = data['temp'].mean()
print(average)
maximum = data['temp'].max()
print(maximum)