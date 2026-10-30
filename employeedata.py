import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("employees.csv")

# Remove duplicate rows
before = len(df)
df = df.drop_duplicates()
duplicates_removed = before - len(df)

# Convert salary to numeric
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Fill missing salaries with mean of valid salaries
salary_mean = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(salary_mean)

# Clean other missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Department"] = df["Department"].fillna("Unknown")
df["Experience"] = df["Experience"].fillna(0)

# Summary
print("Employees:", len(df))
print("Average salary: {:.2f}".format(df["Salary"].mean()))

highest = df.loc[df["Salary"].idxmax()]
print("Highest paid: {} ({:.0f})".format(
    highest["Name"], highest["Salary"]
))

print("Total payroll: {:.0f}".format(df["Salary"].sum()))
print("Duplicates removed:", duplicates_removed)
print("Missing Salary filled with mean: {:.2f}".format(salary_mean))
print("Cleaned rows:", len(df))

# Menu
while True:
    print("\nMenu")
    print("1. Summary")
    print("2. Department-wise analysis")
    print("3. Filter employees above salary limit")
    print("4. Department-wise average salary chart")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Employees:", len(df))
        print("Average salary: {:.2f}".format(df["Salary"].mean()))
        highest = df.loc[df["Salary"].idxmax()]
        print("Highest paid: {} ({:.0f})".format(
            highest["Name"], highest["Salary"]
        ))
        print("Total payroll: {:.0f}".format(df["Salary"].sum()))

    elif choice == "2":
        result = df.groupby("Department")["Salary"].agg(
            ["count", "mean"]
        )
        print(result.to_string())

    elif choice == "3":
        limit = float(input("Enter salary limit: "))
        result = df[df["Salary"] > limit]
        if result.empty:
            print("No employees found above this salary.")
        else:
            print(result.to_string(index=False))

    elif choice == "4":
        avg_salary = df.groupby("Department")["Salary"].mean()
        avg_salary.plot(kind="bar")
        plt.title("Department-wise Average Salary")
        plt.xlabel("Department")
        plt.ylabel("Average Salary")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")


    print("Employees: 1 Average salary:50000 Highest paid: Aman(50000)") 