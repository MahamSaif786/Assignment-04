import random

def print_random_numbers():
    for _ in range(10):  # Loop runs 10 times
        print(random.randint(1, 100), end=" ")  
    print() 

# Function to calculate weight on Mars
def mars_weight():
    earth_weight = float(input("Enter your weight on Earth: "))  
    mars_weight = round(earth_weight * 0.378, 2)  
    print(f"The equivalent weight on Mars: {mars_weight}") 

# Function to calculate weight on different planets
def planetary_weight():
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    earth_weight = float(input("Enter your weight on Earth: "))  
    planet = input("Enter a planet: ") 
    
    if planet in gravity_factors: 
        planet_weight = round(earth_weight * gravity_factors[planet], 2)  
        print(f"The equivalent weight on {planet}: {planet_weight}") 
    else:
        print("Invalid planet name! Please enter a valid planet.")  

# Main function to call all other functions
def main():
    print_random_numbers()  
    mars_weight()  
    planetary_weight()  
if __name__ == "__main__":
    main()