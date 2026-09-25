# booking.py
# Passenger and Booking classes for managing reservation records.


class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender

    def display_passenger(self):
        print("Passenger Name : " + self.name)
        print("Age            : " + str(self.age))
        print("Gender         : " + self.gender)


class Booking:
    def __init__(self, booking_id, bus_id, passenger, seat_number, fare):
        self.booking_id = booking_id
        self.bus_id = bus_id
        self.passenger = passenger  # Instance of Passenger class
        self.seat_number = int(seat_number)
        self.fare = float(fare)

    def display_ticket(self):
        print("=" * 45)
        print("           CONFIRMED BUS TICKET           ")
        print("=" * 45)
        print("Booking ID     : " + self.booking_id)
        print("Bus ID         : " + self.bus_id)
        print("Passenger Name : " + self.passenger.name)
        print("Age / Gender   : " + str(self.passenger.age) + " / " + self.passenger.gender)
        print("Seat Number    : " + str(self.seat_number))
        print("Total Fare     : Rs. " + str(self.fare))
        print("=" * 45)
