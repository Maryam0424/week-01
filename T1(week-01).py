no_of_pupils = 30
weights = []
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

for i in range(no_of_pupils):
    name = input(f"Enter the name of pupil {i + 1}: ")
    
    while True:
        weight = input(f"Enter the weight of {name} in kilograms: ")
        
        if valid_weight(weight):
            break

    names.append(name)
    weights.append(int(weight))

print("\nNames and Weights of Pupils: ")

for name, weight in zip(names, weights):
    print(f"{name}: {weight} kg")
