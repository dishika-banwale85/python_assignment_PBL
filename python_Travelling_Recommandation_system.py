# Project 1: Travel Recommendation System

def recommend_vehicle(distance):
    """
    Returns the recommended vehicle based on travel distance.
    """
    if distance < 3:
        return "Bicycle"
    elif distance < 300:
        return "Motor-Cycle"
    else:
        return "Super-Car"


def main():
    try:
        distance = float(input("How far would you like to travel in miles? "))

        vehicle = recommend_vehicle(distance)
        print(f"I suggest {vehicle} to your destination.")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()