def schedule_shifts(employees, shifts):
    scheduled_shifts = []
    employee_index = 0 
    for day, shift_type, required_employees in shifts:
        assigned_employees = []
        
        for _ in range(required_employees):
            assigned_employee = employees[employee_index]
            assigned_employees.append(assigned_employee)
            employee_index = (employee_index + 1) % len(employees)

        scheduled_shifts.append((day, shift_type, assigned_employees))

    return scheduled_shifts

employees = ["Sohag", "Krishna", "Mandy", "Gaurav"]
shifts = [
    ("Monday", "Morning", 2),
    ("Monday", "Evening", 2),
    ("Tuesday", "Morning", 2),
    ("Tuesday", "Evening", 2),
    ("Wednesday", "Morning", 2),
    ("Wednesday", "Evening", 2)
]

schedule = schedule_shifts(employees, shifts)
for entry in schedule:
    print(entry)
