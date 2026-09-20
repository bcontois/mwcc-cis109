#mission.py program
#Brian J Contois CIS109-G1 20 September 2026
#Introduction to Programming (Python)
#This program will ask a user for the following information,
# & generate a mission briefing with that information.
#Their agent name
#Their age
#The number of years they have been training
#Their favorite color
#The number of gadgets they are carrying
#The number of minutes they have to complete the mission
#
print("Welcome to the Mission Briefing, Agent! ")
name = input("What is your name? ")
print(f"Hello, Agent {name}! We have a few more questions for you. ")
age = input(f"How old are you, Agent {name}? ")
years_training = input(f"How many years of training do you have, Agent {name}? ")
fav_color = input(f"What is your favorite color, Agent {name}? ")
num_gadgets = input(f"How many gadgets do you currently have, Agent {name}? ")
print(f"OK, Agent {name},",end="")
mission_minutes_total = input(f" how many minutes do you have to complete your mission? ")   
#
#This portion of the code will do calculations with the parameters entered;
#
training_percentage = (float(years_training) / (float(age))) * 100
gadget_density = (float(num_gadgets) / float(years_training))
mission_seconds_total = (float(mission_minutes_total) * 60)
mission_minutes_remaining = (float(mission_minutes_total) - 7)
#
#This part of the code will help generate the Mission Code.
#
uppercase_name = name.upper()
uppercase_color = fav_color.upper()
#
#This portion of the code creates boolean expressions about age, gadgets, and training years;
#
is_adult = float(age) >= 18
has_many_gadgets = float(num_gadgets) >= 5
has_training_experience = float(years_training) > 0
#
#This portion of the code generates the Mission Briefing;
#
print("====================================")
print("        SECRET MISSION BRIEFING")
print("====================================")
print(" ")
print(f"Agent: {name}")
print(f"Mission Code: {uppercase_name}-{uppercase_color}-{age}")
print(" ")
print(f"Age: {age}")
print(f"Training: {years_training} years")
print(f"Training Percentage: {training_percentage}%")
print(" ")
print(f"Gadgets: {num_gadgets}")
print(f"Gadget Density: {gadget_density} per training year")
print(" ")
print(f"Mission Time: {mission_minutes_total} minutes")
print(f"Mission Time Remaining: {mission_minutes_remaining} minutes")
print(f"Mission Time in Seconds: {mission_seconds_total}")
print(" ")
print(f"Adult Agent: {is_adult}")
print(f"Many Gadgets: {has_many_gadgets}")
print(f"Training Experience: {has_training_experience}")
print(" ")
print("====================================")
print("        GOOD LUCK, AGENT!")
print("====================================")