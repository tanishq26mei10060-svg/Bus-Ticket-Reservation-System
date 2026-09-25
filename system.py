# system.py
# BusReservationSystem controller managing buses, seat reservations, and tickets.

from bus import Bus
from booking import Booking


class BusReservationSystem:
    def __init__(self):
        # Dictionaries for efficient record lookup by ID
        self.buses = {}
        self.bookings = {}
        # Simple integer counter for generating sequential booking IDs
        self.booking_counter = 1

    def load_initial_data(self, bus_data_list):
        for bus_info in bus_data_list:
            bus = Bus(
                bus_id=bus_info["bus_id"],
                bus_name=bus_info["bus_name"],
                route=bus_info["route"],
                schedule=bus_info["schedule"],
                base_fare=bus_info["base_fare"],
                total_seats=bus_info["total_seats"],
                amenities=bus_info["amenities"]
            )
            # Store Bus object in dictionary using bus_id as key
            self.buses[bus.bus_id] = bus

    def get_all_buses(self):
        bus_list = []
        for bus_id in self.buses:
            bus_list.append(self.buses[bus_id])
        return bus_list

    def find_bus(self, bus_id):
        # Membership operator 'in' on dictionary keys
        if bus_id in self.buses:
            return self.buses[bus_id]
        return None

    def search_buses(self, source, destination):
        results = []
        clean_source = source.strip().lower()
        clean_dest = destination.strip().lower()

        for bus_id in self.buses:
            bus = self.buses[bus_id]
            bus_source = bus.route[0].strip().lower()
            bus_dest = bus.route[1].strip().lower()

            # Logical AND operator to verify both source and destination match
            if bus_source == clean_source and bus_dest == clean_dest:
                results.append(bus)

        return results

    def calculate_seat_position(self, seat_num):
        # Natural use of floor division (//), modulus (%), and operator precedence
        # Layout: 4 seats per row (2 on left, 2 on right)
        row = ((seat_num - 1) // 4) + 1
        col = ((seat_num - 1) % 4) + 1
        return (row, col)  # Returning meaningful tuple of coordinates

    def calculate_fare(self, base_fare, seat_number):
        # Front rows (seats 1 to 4) have a flat comfort charge of Rs. 50
        if seat_number <= 4:
            total_fare = base_fare + 50.0
        else:
            total_fare = base_fare
        return total_fare

    def book_ticket(self, bus_id, passenger, seat_number):
        bus = self.find_bus(bus_id)

        # Identity operator 'is' used legitimately to check against None
        if bus is None:
            return None

        # Logical NOT and membership check via method
        if not bus.is_seat_available(seat_number):
            return None

        # Calculate final fare
        total_fare = self.calculate_fare(bus.base_fare, seat_number)

        # Generate simple sequential booking ID: B001, B002, etc.
        if self.booking_counter < 10:
            booking_id = "B00" + str(self.booking_counter)
        elif self.booking_counter < 100:
            booking_id = "B0" + str(self.booking_counter)
        else:
            booking_id = "B" + str(self.booking_counter)

        # Assignment operator += for counter
        self.booking_counter += 1

        # Reserve seat in the Bus instance
        bus.reserve_seat(seat_number)

        # Create new Booking instance
        new_booking = Booking(booking_id, bus_id, passenger, seat_number, total_fare)

        # Save into bookings dictionary
        self.bookings[booking_id] = new_booking
        return new_booking

    def cancel_booking(self, booking_id):
        # Membership operator 'not in'
        if booking_id not in self.bookings:
            return False

        booking = self.bookings[booking_id]
        bus = self.find_bus(booking.bus_id)

        # Identity operator 'is not' used legitimately to check against None
        if bus is not None:
            bus.release_seat(booking.seat_number)

        del self.bookings[booking_id]
        return True

    def get_all_bookings(self):
        booking_list = []
        for b_id in self.bookings:
            booking_list.append(self.bookings[b_id])
        return booking_list
