import sys

def calculate_happiness():
    # sys.argv contains the command-line arguments.
    # sys.argv[0] is the script name.
    # We expect 3 additional arguments representing the strings.
    if len(sys.argv) < 4:
        print("Usage: python happiness_calculator.py <str1> <str2> <str3>")
        return

    # Extract strings from command line arguments
    string1 = sys.argv[1].split('-')
    string2 = sys.argv[2].split('-')
    given_numbers = sys.argv[3].split('-')

    # Convert to sets for O(1) average lookup time
    set1 = set(string1)
    set2 = set(string2)

    happiness = 0

    # Calculate happiness
    for num in given_numbers:
        if num in set1:
            happiness += 1
        elif num in set2:
            happiness -= 1

    print(f"Final happiness: {happiness}")

if __name__ == "__main__":
    calculate_happiness()