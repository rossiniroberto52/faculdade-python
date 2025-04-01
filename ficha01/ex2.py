age = int(input("AGE: "))
xp_time = int(input("XP_TIME: "))

if age < 18 or xp_time < 1:
    print("High risk!")
elif xp_time >= 1 and xp_time <= 5:
    print("Low risk!")
elif age >= 18 and age <= 60:
    print("Medium risk!")
