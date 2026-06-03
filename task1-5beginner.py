import math
import random

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# 1. Variables
print("1. Variables and Types")
print("\n1.1. Variable pi = 22/7")
pi = 22/7
print(f"pi = {pi}")
print(f"Type of pi: {type(pi)}")

print("\n1.2. Attempting to create variable 'for':")
print("Trying to assign: for = 4")
print("This will cause a SyntaxError because 'for' is a Python keyword.")
print("Keywords are reserved words that cannot be used as variable names.")

print("\n1.3. Simple Interest Calculation:")
principal = 1000
rate = 5.5
time = 3
simple_interest = (principal * rate * time) / 100
print(f"Principal = {principal}")
print(f"Rate of Interest = {rate}%")
print(f"Time = {time} years")
print(f"Simple Interest = {simple_interest}")
print()

# 2. Numbers
print("2. Numbers")

print("\n2.1. Format function with 145 and 'o':")
result = format(145, 'o')
print(f"format(145, 'o') = {result}")
print("Representation: Octal (base 8)")

print("\n2.2. Circular Pond Area and Water Volume:")
radius = 84
pi_value = 3.14
pond_area = pi_value * radius ** 2
print(f"Pond radius = {radius} meters")
print(f"Pond area = {pond_area} square meters")
water_per_sq_meter = 1.4
total_water = pond_area * water_per_sq_meter
print(f"Total water in pond = {int(total_water)} liters")

print("\n2.3. Speed Calculation:")
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print(f"Distance = {distance} meters")
print(f"Time = {time_minutes} minutes = {time_seconds} seconds")
print(f"Speed = {int(speed)} m/s")
print()

# 3. List
print("3. List - Justice League")
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("\n3.1. Number of members:")
print(f"Justice League members: {justice_league}")
print(f"Total members: {len(justice_league)}")

print("\n3.2. Add Batgirl and Nightwing:")
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(f"Justice League: {justice_league}")

print("\n3.3. Move Wonder Woman to the beginning:")
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"Justice League: {justice_league}")

print("\n3.4. Separate Aquaman and Flash with Superman:")
aquaman_idx = justice_league.index("Aquaman")
flash_idx = justice_league.index("Flash")
if abs(aquaman_idx - flash_idx) == 1:
    justice_league.remove("Superman")
    min_idx = min(aquaman_idx, flash_idx)
    justice_league.insert(min_idx + 1, "Superman")
print(f"Justice League: {justice_league}")

print("\n3.5. Replace with new team:")
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"Justice League: {justice_league}")

print("\n3.6. Sort alphabetically:")
justice_league.sort()
print(f"Sorted Justice League: {justice_league}")
print(f"New leader (at index 0): {justice_league[0]}")
print()

# 4. If Condition
print("4. If Condition")

print("\n4.1. BMI Category:")
weight = get_float("Enter weight in kilograms: ")
height = get_float("Enter height in meters: ")
bmi = weight / (height ** 2)
print(f"Your BMI: {bmi:.2f}")
if bmi >= 30:
    category = "Obesity"
elif bmi >= 25:
    category = "Overweight"
elif bmi >= 18.5:
    category = "Normal"
else:
    category = "Underweight"
print(f"Category: {category}")

print("\n4.2. City to Country Mapping:")
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ").strip()
if city in australia:
    country = "Australia"
elif city in uae:
    country = "UAE"
elif city in india:
    country = "India"
else:
    country = "Unknown"
print(f"{city} is in {country}")

print("\n4.3. Check if two cities belong to the same country:")
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

country1 = None
country2 = None

if city1 in australia:
    country1 = "Australia"
elif city1 in uae:
    country1 = "UAE"
elif city1 in india:
    country1 = "India"

if city2 in australia:
    country2 = "Australia"
elif city2 in uae:
    country2 = "UAE"
elif city2 in india:
    country2 = "India"

if country1 == country2 and country1 is not None:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")
print()

# 5. For Loop
print("5. For Loop")

print("\n5.1. Roll a six-sided die 20+ times:")
rolls = 20
count_6 = 0
count_1 = 0
count_double_6 = 0
previous_roll = 0

print(f"Rolling a six-sided die {rolls} times:")
for i in range(rolls):
    face = random.randint(1, 6)
    print(f"Roll {i + 1}: {face}")
    
    if face == 6:
        count_6 += 1
    if face == 1:
        count_1 += 1
    if face == 6 and previous_roll == 6:
        count_double_6 += 1
    
    previous_roll = face

print(f"\nStatistics:")
print(f"Times rolled a 6: {count_6}")
print(f"Times rolled a 1: {count_1}")
print(f"Times rolled two 6s in a row: {count_double_6}")

print("\n5.2. Jumping Jacks Workout:")
total_jacks = 100
jacks_per_set = 10
completed_jacks = 0

for set_num in range(1, 11):
    input(f"Press Enter to start set {set_num} (10 jumping jacks)...")
    completed_jacks += jacks_per_set
    print(f"Set {set_num} completed! Total: {completed_jacks} jumping jacks")
    
    if completed_jacks >= total_jacks:
        print("Congratulations! You completed the workout")
        break
    
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed_jacks} jumping jacks.")
            break
    elif tired in ["no", "n"]:
        remaining = total_jacks - completed_jacks
        print(f"{remaining} jumping jacks remaining.")
