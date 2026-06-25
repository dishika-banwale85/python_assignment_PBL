def sort_hyphenated_colors(color_string):
    # 1. Split the string into a list using the hyphen as a separator
    color_list = color_string.split('-')
    
    # 2. Sort the list alphabetically
    color_list.sort()
    
    # 3. Join the sorted list back into a single string with hyphens
    sorted_string = '-'.join(color_list)
    
    return sorted_string

# Example usage:
if __name__ == "__main__":
    input1 = "green-red-yellow-black-white"
    print(f"Input: {input1}")
    print(f"Output: {sort_hyphenated_colors(input1)}")
    
    print("-" * 20)
    
    input2 = "PINK-BLUE-TAN-PURPLE"
    print(f"Input: {input2}")
    print(f"Output: {sort_hyphenated_colors(input2)}")