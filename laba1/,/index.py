from TouristPass import TouristPass
from insertion import insertion
from quick import quicksort

austria_pass = TouristPass("Austria", 12, 1300)
germany_pass = TouristPass("Germany", 6, 900)
columbia_pass = TouristPass("Columbia", 15, 2100)
england_pass =TouristPass("England", 9, 3200)

country_array = [austria_pass, germany_pass, columbia_pass, england_pass]

country_array = quicksort(country_array)
#country_array = insertion(country_array)

for i in range(len(country_array)):
    print(country_array[i].country)
