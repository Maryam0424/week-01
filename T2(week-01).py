no_of_pupils = 30
weights_first_day = []
weights_last_day = []
names = []

def valid_weight(weight):
    try:
        weight = int(weight)
        if 20 <= weight <=200:
            return True
        
        else:
            print("Ivalid Weight. Weight must be between 20 and 200 kilograms!.")
            return False
    
    except ValueError:
        print("Invalid input. Please enter a numerical value for weight.")
        return False

print("Enter weights for the first day: ")
for i in range(no_of_pupils):
    name = input(f"Enter the name of pupil {i + 1}: ")
    
    while True:
        weight = input(f"Enter the weight of {name} in kilograms: ")
        
        if valid_weight(weight):
            break

    names.append(name)
    weights_first_day.append(int(weight))

print("Enter weights for the last day: ")
for i in range(no_of_pupils):
    name = input(f"Enter the name of pupil {i + 1}: ")
    
    while True:
        weight = input(f"Enter the weight of {name} in kilograms: ")
        
        if valid_weight(weight):
            break

    weights_last_day.append(int(weight))

weight_differences = [last - first for first, last in zip(weights_first_day, weights_last_day)]

print("\nNames, Weights and differences: ")

for name, first, last, difference in zip(names, weights_first_day, weights_last_day, weight_differences):
    print(f"Name: {name}, First day weight: {first} kg, Last day weight: {last} kg, Difference: {difference} kg")
