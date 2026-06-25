# Initialize the dictionary with student records
student_records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

def get_average_marks():
    # Get user input for the student's name
    name = input("Enter a name: ")
    
    # Check if the name exists in the dictionary
    if name in student_records:
        marks = student_records[name]
        
        # Calculate the average: (sum of marks) / (number of subjects)
        average = sum(marks) / len(marks)
        
        # Output the result formatted to 2 decimal places if needed
        print(f"Average percentage mark: {average:.2f}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    get_average_marks()