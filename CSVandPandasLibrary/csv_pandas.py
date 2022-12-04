# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = [int(row[1]) for i, row in enumerate(data) if i != 0]
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])
#
# monday_temp_celsius = data[data.day == "Monday"].temp
# monday_temp_farenheit = monday_temp_celsius * 1.8 + 32
# print(monday_temp_farenheit)
#
#
# data_dict = {
#     "students": ["Tom", "Jerry", "Ben"],
#     "scores": [25, 42, 76]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# My solution
import pandas as pd
from math import isnan

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = {
    "Fur Colors": [],
    "Count": []
}

# DataFrame.dropna() to drop nan bullsh*t
furs = data["Primary Fur Color"].dropna().to_list()
print(furs)

data_dict["Fur Colors"] = list(set(furs))
print(data_dict["Fur Colors"])

data_dict["Count"] = [furs.count("Gray"), furs.count("Cinnamon"), furs.count("Black")]
print(data_dict["Count"])

data = pd.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")


# # Course solution
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Red"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [gray_squirrel_count, red_squirrel_count, balck_squirrel_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
