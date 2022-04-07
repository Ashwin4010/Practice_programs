import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(squirrel_data)

grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "fur color" : ["grey","cinnamon","black"],
    "count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count],
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv", index=None)
