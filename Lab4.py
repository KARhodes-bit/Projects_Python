# Program Name: Lab4.py
# Course: IT1114/Section BWE
# Student Name: Kendres Rhodes
# Assignment Number: Lab4
# Due Date: 09/17/2024
# Purpose: This program calculates the total cost of a resort vacation based on user input
# List specific resources used to complete the assignment: CCSE tutoring center, Module 3&4 from Programming Principles

def roomCost(nights, room_type):
    """
    Calculate the cost of the room based on the number of nights and room type.

    :param nights: Number of nights to stay
    :param room_type: Type of room selected (1: Two Queen Beds, 2: One King Bed, 3: Queen Suite, 4: King Suite)
    :return: Total cost for the room stay
    """
    #Define the cost per night for each room type
    room_prices = {
        1: 375, #Two Queen Beds
        2: 350, #One King Bed
        3: 525, #Queen Suite
        4: 475  #King Suite
    }

    # Get the cost for the selected room type
    price_per_night = room_prices.get( room_type, 0)

    #calculate the total cost for the room
    total_cost = nights * price_per_night

    return total_cost

def mealCost(brunches, dinners):
    """
    Calculate the total meal cost including a 15% gratuity.

    :param brunches: Number of brunches
    :param dinners: Number of dinners
    :return: Total cost for meals including 15% gratuity
    """
    brunch_price = 25
    dinner_price = 75
    gratuity_rate = 0.15

    # Calculate the total meal cost before gratuity
    total_meal_cost = (brunches * 25 ) + (dinners * 75)

    #Add gratuity
    total_meal_cost_with_gratuity = total_meal_cost * (1 + gratuity_rate)

    return total_meal_cost_with_gratuity
def excursionCost(picnics, snorkeling, guided_hikes, boat_dinners):
    """
    Calculate the total cost of excursions.
    :param picnics: Number of picnics
    :param snorkeling: Number of snorkeling activities
    :param guided_hikes: Number of guided hikes
    :param boat_dinners: Number of boat dinners
    :return: Total cost for excursions
    """
    picnic_price = 50
    snorkeling_price = 25
    guided_hike_price = 17
    boat_dinner_price = 200

    #Calculate the total cost of excursions
    total_excursions_cost = (picnics * picnic_price) + \
                            (snorkeling * snorkeling_price) + \
                            (guided_hikes * guided_hike_price) + \
                            (boat_dinners * boat_dinner_price)

    return total_excursions_cost
def main ():
    """
    Main function to interact with the user and calculate the total cost.
    """
    # Get user input for the number of nights and room type
    nights = int(input("Number of nights: "))
    num_people = int(input("Number of people: "))

    # Display room type options
    print("Room Types:")
    print("(1) - Two Queen Beds")
    print("(2) - One King Bed")
    print("(3) - Queen Suite")
    print("(4) - King Suite")

    # Get the selected room type
    room_type = int(input("Select Type: "))
    room_cost = roomCost(nights, room_type)

    #Get the number of brunches and dinners
    brunches = int(input("How many Brunches: "))
    dinners = int(input("How many Dinners: "))

    # Calculate meal cost
    meal_cost = mealCost(brunches, dinners)

    #Get excursion preferences
    picnics = 1 if input("Picnic? (y/n): ").lower() == 'y' else 0
    snorkeling = num_people if input("Snorkeling? (y/n): ").lower() == 'y' else 0
    guided_hikes = num_people if input("Guided Hike? (y/n): ").lower() == 'y' else 0
    boat_dinners = 1 if input("Boat Dinner? (y/n): ").lower() == 'y' else 0

    excursion_cost = excursionCost(picnics, snorkeling, guided_hikes, boat_dinners)

    total_cost = room_cost + meal_cost + excursion_cost

    #Display results
    print(f"Room Cost: ${room_cost}")
    print(f"Meal Cost: ${meal_cost}")
    print(f"Excursion Cost: ${excursion_cost}")
    print(f"Total Cost: ${total_cost}")

if __name__ == "__main__":
    main()




