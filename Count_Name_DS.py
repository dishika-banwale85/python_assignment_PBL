def count_alex_occurrences(input_string):
    # Split the string into a list of words based on spaces
    words = input_string.split()
    
    # Count how many times the word "Alex" appears in the list
    count = words.count("Alex")
    
    return count

# Example usage:
if __name__ == "__main__":
    # Example input as per project
    input_text = "Hi Alex WelcomeAlex Bye Alex."
    
    # Note: In the sample "WelcomeAlex", the name is attached to another word.
    # To handle cases where "Alex" might be part of another word, 
    # we can use the string count method instead:
    
    # Using string count:
    result = input_text.count("Alex")
    
    print(f"Number of times 'Alex' appears: {result}")