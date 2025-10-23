while True: 
    day_num = input("What's the day of the week? ")
    day = int(day_num)

    if day == 6 or day == 7:
        print("That's the weekend")
    else:
        print("That's a weekday")

    print("Let's go again!")
