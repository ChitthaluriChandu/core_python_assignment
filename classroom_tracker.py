def calculate_average(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = round(sum(marks) / len(marks), 2)
    return averages
def find_top_performer(averages):
    top_student = max(averages, key=averages.get)
    return top_student

if __name__ == "__main__":
    students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
    averages = calculate_average(students)
    top_student = find_top_performer(averages)
    print(f"Average Marks: {averages}")
    print(f"Top Performer: {top_student}")
