Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Branch = input("Enter your branch: ")
Marks1 = int(input("Enter the marks taken in Python: "))
Marks2 = int(input("Enter the marks taken in C: "))
Marks3 = int(input("Enter the marks taken in Java: "))

Student = {
    "Name": Name,
    "Age": Age,
    "Branch": Branch,
    "Marks in Python": Marks1,
    "Marks in C": Marks2,
    "Marks in Java": Marks3
}

Total = Marks1 + Marks2 + Marks3
Avg = Total / 3

Student["Total Marks"] = Total
Student["Average Marks"] = round(Avg, 2)

print("\n--- Student Information ---")
print("Name of the student: ", Student["Name"])
print("Age of the student: ", Student["Age"])
print("Branch of the student: ", Student["Branch"])
print("Average marks: ", Student["Average Marks"])

print("\n--- Full Student Record ---")
for key, value in Student.items():
    print(f"{key}: {value}")
