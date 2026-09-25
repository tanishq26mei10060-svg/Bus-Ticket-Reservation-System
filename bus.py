# bus.py
# Bus entity class representing individual buses in the reservation system.

from array import array
from data import AMENITY_AC, AMENITY_WIFI, AMENITY_SLEEPER


class Bus:
    def __init__(self, bus_id, bus_name, route, schedule, base_fare, total_seats, amenities):
        self.bus_id = bus_id
        self.bus_name = bus_name
        self.route = route          # Tuple: (source, destination)
        self.schedule = schedule    # Tuple: (departure_time, arrival_time)
        self.base_fare = float(base_fare)
        self.total_seats = int(total_seats)
        self.amenities = amenities  # Bitwise integer mask

        # Homogeneous integer array for physical seat numbers
        seat_numbers_list = []
        for seat_num in range(1, self.total_seats + 1):
            seat_numbers_list.append(seat_num)
        self.all_seats = array('i', seat_numbers_list)

        # Set data structure for dynamic tracking of vacant seats
        self.available_seats = set(range(1, self.total_seats + 1))

    def get_amenities_list(self):
        # Uses bitwise AND (&) to test active amenity flags
        amenity_names = []
        if (self.amenities & AMENITY_AC) != 0:
            amenity_names.append("AC")
        if (self.amenities & AMENITY_WIFI) != 0:
            amenity_names.append("WiFi")
        if (self.amenities & AMENITY_SLEEPER) != 0:
            amenity_names.append("Sleeper")

        if len(amenity_names) == 0:
            amenity_names.append("Standard")
        return amenity_names

    def display_details(self):
        source = self.route[0]
        destination = self.route[1]
        departure = self.schedule[0]
        arrival = self.schedule[1]
        amenities_str = ", ".join(self.get_amenities_list())
        available_count = len(self.available_seats)

        print("-" * 50)
        print("Bus ID         : " + self.bus_id)
        print("Bus Name       : " + self.bus_name)
        print("Route          : " + source + " -> " + destination)
        print("Departure/Arr  : " + departure + " - " + arrival)
        print("Base Fare      : Rs. " + str(self.base_fare))
        print("Available Seats: " + str(available_count) + " / " + str(self.total_seats))
        print("Amenities      : " + amenities_str)
        print("-" * 50)

    def is_seat_available(self, seat_num):
        # Membership operator 'in' on set
        return seat_num in self.available_seats

    def reserve_seat(self, seat_num):
        if seat_num in self.available_seats:
            self.available_seats.remove(seat_num)
            return True
        return False

    def release_seat(self, seat_num):
        if seat_num <= self.total_seats and seat_num not in self.available_seats:
            self.available_seats.add(seat_num)
            return True
        return False
