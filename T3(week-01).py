no_of_pupils = 30
weight_diff_threshold = 2.5

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

print("\nPupils with a Difference in Weight > 2.5 kg: ")

for name, first, last, difference in zip(names, weights_first_day, weights_last_day, weight_differences):
    difference = last - first
    if difference > weight_diff_threshold:
        change_type = "rise"
        print(f"{name}, Difference: {difference} kg, {change_type} in weight.")
    
    elif difference < weight_diff_threshold:
        change_type = "fall"
        print(f"{name}, Difference: {abs(difference)} kg, {change_type} in weight.")
