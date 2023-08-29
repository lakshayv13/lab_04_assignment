class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name.lower() == name.lower()]
        return result

    def search_by_salary(self, operator, salary):
        if operator == "<":
            result = [emp for emp in self.employees if emp.salary < salary]
        elif operator == ">":
            result = [emp for emp in self.employees if emp.salary > salary]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= salary]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= salary]
        else:
            result = []
        return result

if __name__ == "__main__":
    database = EmployeeDatabase()

    emp_data = [
        ("161E90", "Raman", 41, 56000),
        ("161F91", "Himadri", 38, 67500),
        ("161F99", "Jaya", 51, 82100),
        ("171E20", "Tejas", 30, 55000),
        ("171G30", "Ajay", 45, 44000)
    ]

    for emp_id, name, age, salary in emp_data:
        emp = Employee(emp_id, name, age, salary)
        database.add_employee(emp)

    print("Search Options:")
    print("1. Age\n2. Name\n3. Salary")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter age to search: "))
        result = database.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        result = database.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (<, >, <=, >=): ")
        salary = int(input("Enter salary to compare: "))
        result = database.search_by_salary(operator, salary)
    else:
        print("Invalid choice!")
        result = []

    if result:
        print("Search Results:")
        for emp in result:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found.")