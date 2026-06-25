# Create dictionary

people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display original facts
for name, fact in people.items():
    print(f"{name}: {fact}")

print()

# Modify Jeff's fact
people["Jeff"] = "Is afraid of heights."

# Add a new person
people["Jill"] = "Can hula dance."

# Display updated facts
for name, fact in people.items():
    print(f"{name}: {fact}")