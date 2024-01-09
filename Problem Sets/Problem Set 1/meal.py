def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    meal_time(converted_time)

def convert(time):
    hours, minutes = map(float, time.split(":"))
    return hours + minutes / 60

def meal_time(converted_time):
    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")

if __name__ == "__main__":
    main()
