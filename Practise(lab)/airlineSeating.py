def assign_seats(passengers, seating_chart):
    passengerCount = 0
    plan = []
    for row, seat, avail in seating_chart:
        if passengerCount >= len(passengers):
            plan.append(("<Vacant>", row, seat))
        elif avail:
            plan.append((passengers[passengerCount], row, seat))
            passengerCount += 1
        else:
            plan.append(("<Taken>", row, seat))
    return plan

passengers = ["Krishna", "Vanshit", "Sphag De", "Amit", "Preeti"]
seating_chart = [(1, 1, True), (1, 2, False), (1, 3, False), (2, 4, True), (2, 5, True), (2, 6, True)]

print(assign_seats(passengers, seating_chart))