age = int(input("Enter your age: "))
qualification = input("Have you completed +2? (yes/no): ")

if age >= 18 and qualification.lower() == "yes":
    print("You are eligible for admission in bachelor.")
else:
    print("You are not eligible for admission bachelor.")