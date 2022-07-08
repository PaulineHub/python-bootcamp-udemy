import pandas

######### WEATHER DATA EXAMPLE #############

#data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)

#data_list = data["temp"].tolist()
#print(data_list)

#data_moy = data["temp"].mean()
#print(data_moy)

#data_max = data["temp"].max()
#print(data_max)

###########################################
#Get data in Columns
#print(data["condition"])
#print(data.condition)

###########################################
#Get data in Rows
#print(data[data.day == "Monday"])

#row with max temperature
#print(data[data.temp == data_max])

###########################################
#Create a dataframe from scratch
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#   "scores" : [76, 56, 65]
#}
#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("new_data.csv")

########### SQUIRRELS EXAMPLE #############

#read file
data_squirrels = pandas.read_csv("squirrel_data.csv")
#print(data_squirrels)
#extract number of squirrels by color
grey_squirrels_count = len(data_squirrels[data_squirrels["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data_squirrels[data_squirrels["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data_squirrels[data_squirrels["Primary Fur Color"] == "Black"])
#print(black_squirrels_count)
#create a dictionnary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
#print(data_dict)
data_squirrels_color = pandas.DataFrame(data_dict)
#print(data_squirrels_color)
data_squirrels_color.to_csv("squirrels_count_color.csv")
