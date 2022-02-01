travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_countries(new_country,new_visits,new_cities):
    added_country = {}
    added_country["country"] = new_country
    added_country["visits"] = new_visits
    added_country["cities"] = new_cities
    travel_log.append(added_country)

print("Enter the country, cities and number of times you have visited those cities with empty space: ")
country = input("Enter the country: ")
city = input("Enter the Cities: ").split(" ")
visits = int(input("Enter the number of times you have visited those cities: "))

add_countries(new_country=country,new_visits=visits,new_cities=city)

print(travel_log)

# add_countries("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
