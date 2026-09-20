# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Created by: Khushboo Jeswani

def calculate_grade(average):
    """Calculate grade and comment based on average marks."""
    if average >= 90:
        return "A", "Excellent! Keep up the great work!"
    elif average >= 80:
        return "B", "Very Good! You're doing well."
    elif average >= 70:
        return "C", "Good. Room for improvement."
    elif average >= 60:
        return "D", "Needs Improvement. Please study more."
    else:
        return "F", "Please seek help and work harder."


def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within the given range."""
    while True:
        try:
            value = float(input(prompt))

            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("=" * 60)
    print("             STUDENT GRADE CALCULATOR")
    print("=" * 60)

    # Get number of students
    while True:
        try:
            num_students = int(input("Enter number of students: "))

            if num_students > 0:
                break
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    student_names = []
    student_marks = []
    student_results = []

    # Collect student data
    for i in range(num_students):
        print(f"\n=== STUDENT {i + 1} ===")

        name = input("Student name: ").strip()

        while name == "":
            print("Name cannot be empty!")
            name = input("Student name: ").strip()

        student_names.append(name)

        print("Enter marks (0-100):")

        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        marks = [math, science, english]
        student_marks.append(marks)

        average = sum(marks) / len(marks)

        grade, comment = calculate_grade(average)

        student_results.append({
            "average": average,
            "grade": grade,
            "comment": comment
        })

    # Display results
    print("\n" + "=" * 75)
    print("                         RESULTS SUMMARY")
    print("=" * 75)

    print(f"{'Name':<20} | {'Avg':>6} | {'Grade':^5} | Comment")
    print("-" * 75)

    for i in range(num_students):
        name = student_names[i]
        avg = student_results[i]["average"]
        grade = student_results[i]["grade"]
        comment = student_results[i]["comment"]

        print(f"{name:<20} | {avg:>6.1f} | {grade:^5} | {comment}")

    # Class statistics
    averages = [result["average"] for result in student_results]

    class_average = sum(averages) / len(averages)
    highest = max(averages)
    lowest = min(averages)

    highest_index = averages.index(highest)
    lowest_index = averages.index(lowest)

    print("\n" + "=" * 60)
    print("                    CLASS STATISTICS")
    print("=" * 60)

    print(f"Total Students: {num_students}")
    print(f"Class Average: {class_average:.1f}")
    print(f"Highest Average: {highest:.1f} ({student_names[highest_index]})")
    print(f"Lowest Average: {lowest:.1f} ({student_names[lowest_index]})")

    print("\n" + "=" * 60)
    print("Thank you for using the Grade Calculator!")
    print("=" * 60)


if __name__ == "__main__":
    main()
