# part-1 - user input

city = input("city name:")
temp = float(input("temperature in C: "))


# part 2 - if STATEMENT
if temp > 35:
    print("warning: it is hot today")


# part-3 IF-ELSE statement
if temp > 25:
    print("great day to go out")
else:
    print("grab a jacket before you go out")


# PART 4 - IF-ELIF-ELSE statement
if temp > 35:
    print("weather: it is scorching hot today")
elif temp > 25:
    print("weather: warm")
elif temp > 15:
    print("weather: cool and windy")
else:
    print("weather: cold - stay inside")


#part 5- datetime
import datetime
import calendar

now = datetime.datetime.now()
print("city:", city)
print("time now:", now)

print(calendar.calendar(now.year))