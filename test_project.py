# tests/test_project.py
# Automated test suite using ONLY plain Python assert statements.
# No unittest, no pytest, no external dependencies.

import os
import sys
from array import array

# Ensure root directory is accessible in module path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data import INITIAL_BUSES, SERVICED_CITIES, AMENITY_AC, AMENITY_WIFI, AMENITY_SLEEPER
from bus import Bus
from booking import Passenger, Booking
from system import BusReservationSystem


def test_bus_initialization():
    bus = Bus(
        bus_id="TEST01",
        bus_name="Test Bus",
        route=("CityA", "CityB"),
        schedule=("10:00 AM", "02:00 PM"),
        base_fare=300.0,
        total_seats=10,
        amenities=AMENITY_AC | AMENITY_WIFI
    )
    assert bus.bus_id == "TEST01", "Bus ID initialization failed"
    assert bus.route == ("CityA", "CityB"), "Route tuple initialization failed"
    assert bus.total_seats == 10, "Total seats initialization failed"
    assert len(bus.available_seats) == 10, "Available seats set initialization failed"
    assert type(bus.base_fare) is float, "Base fare type conversion failed"


def test_amenity_bitwise_flags():
    # Bitwise OR to combine
    combined_flags = AMENITY_AC | AMENITY_SLEEPER  # 1 | 4 = 5
    bus = Bus("TEST02", "Express", ("A", "B"), ("01:00", "05:00"), 200.0, 8, combined_flags)

    # Bitwise AND to check active amenities
    assert (bus.amenities & AMENITY_AC) != 0, "AC amenity bitwise flag should be active"
    assert (bus.amenities & AMENITY_SLEEPER) != 0, "Sleeper amenity bitwise flag should be active"
    assert (bus.amenities & AMENITY_WIFI) == 0, "WiFi amenity flag should NOT be active"

    amenities_list = bus.get_amenities_list()
    assert "AC" in amenities_list, "Amenities list should contain AC"
    assert "Sleeper" in amenities_list, "Amenities list should contain Sleeper"
    assert "WiFi" not in amenities_list, "Amenities list should not contain WiFi"


def test_seat_array_type():
    bus = Bus("TEST03", "ArrayBus", ("A", "B"), ("06:00", "09:00"), 150.0, 12, 0)
    assert type(bus.all_seats) is array, "all_seats must be an instance of array.array"
    assert bus.all_seats.typecode == 'i', "all_seats must have typecode 'i' for integers"
    assert len(bus.all_seats) == 12, "all_seats array length must match total_seats"
    assert bus.all_seats[0] == 1, "First seat in array must be 1"
    assert bus.all_seats[11] == 12, "Last seat in array must be 12"


def test_search_buses():
    system = BusReservationSystem()
    system.load_initial_data(INITIAL_BUSES)

    results = system.search_buses("Delhi", "Jaipur")
    assert len(results) >= 1, "Should find at least 1 bus for Delhi to Jaipur"
    assert results[0].route == ("Delhi", "Jaipur"), "Found bus route must match search criteria"

    invalid_results = system.search_buses("UnknownCity", "OtherCity")
    assert len(invalid_results) == 0, "Non-existent route should return empty list"


def test_book_ticket_success():
    system = BusReservationSystem()
    system.load_initial_data(INITIAL_BUSES)

    passenger = Passenger("Aman Verma", 20, "M")
    booking = system.book_ticket("BUS101", passenger, 5)

    assert booking is not None, "Booking should succeed for open seat"
    assert booking.booking_id == "B001", "First booking ID must be B001"
    assert booking.seat_number == 5, "Booked seat number must match requested seat"

    bus = system.find_bus("BUS101")
    assert 5 not in bus.available_seats, "Booked seat must be removed from available_seats set"


def test_book_ticket_duplicate_seat():
    system = BusReservationSystem()
    system.load_initial_data(INITIAL_BUSES)

    passenger1 = Passenger("Rohit Sharma", 22, "M")
    passenger2 = Passenger("Pooja Patel", 21, "F")

    booking1 = system.book_ticket("BUS101", passenger1, 6)
    assert booking1 is not None, "First booking should succeed"

    booking2 = system.book_ticket("BUS101", passenger2, 6)
    assert booking2 is None, "Second booking for identical seat must fail and return None"


def test_cancel_booking():
    system = BusReservationSystem()
    system.load_initial_data(INITIAL_BUSES)

    passenger = Passenger("Simran Kaur", 19, "F")
    booking = system.book_ticket("BUS101", passenger, 7)
    assert booking is not None, "Booking must succeed initially"

    bus = system.find_bus("BUS101")
    assert 7 not in bus.available_seats, "Seat 7 should be occupied"

    cancel_success = system.cancel_booking(booking.booking_id)
    assert cancel_success is True, "Cancellation of valid booking ID must succeed"
    assert 7 in bus.available_seats, "Cancelled seat must be restored to available_seats set"
    assert booking.booking_id not in system.bookings, "Booking record must be removed"

    cancel_invalid = system.cancel_booking("INVALID999")
    assert cancel_invalid is False, "Cancelling non-existent booking ID must return False"


def test_seat_math_precedence():
    system = BusReservationSystem()
    # Floor division and modulus test for 4-seats-per-row layout
    row1, col1 = system.calculate_seat_position(1)
    assert row1 == 1 and col1 == 1, "Seat 1 should be Row 1, Column 1"

    row4, col4 = system.calculate_seat_position(4)
    assert row4 == 1 and col4 == 4, "Seat 4 should be Row 1, Column 4"

    row5, col5 = system.calculate_seat_position(5)
    assert row5 == 2 and col5 == 1, "Seat 5 should be Row 2, Column 1"

    row10, col10 = system.calculate_seat_position(10)
    assert row10 == 3 and col10 == 2, "Seat 10 should be Row 3, Column 2"


def test_identity_operator():
    system = BusReservationSystem()
    system.load_initial_data(INITIAL_BUSES)

    # Legitimate identity checks against None
    bus_found = system.find_bus("BUS101")
    assert bus_found is not None, "Existing bus lookup should not be None"

    bus_missing = system.find_bus("BUS999")
    assert bus_missing is None, "Missing bus lookup must return None"


def test_frozenset_cities():
    assert "Delhi" in SERVICED_CITIES, "Delhi should be in serviced cities frozenset"
    assert "Jaipur" in SERVICED_CITIES, "Jaipur should be in serviced cities frozenset"
    assert "London" not in SERVICED_CITIES, "London should not be in serviced cities"
    assert type(SERVICED_CITIES) is frozenset, "SERVICED_CITIES must be a frozenset instance"


def run_all_tests():
    print("=" * 55)
    print("Running Bus Ticket Reservation System Test Suite...")
    print("=" * 55)

    tests = [
        test_bus_initialization,
        test_amenity_bitwise_flags,
        test_seat_array_type,
        test_search_buses,
        test_book_ticket_success,
        test_book_ticket_duplicate_seat,
        test_cancel_booking,
        test_seat_math_precedence,
        test_identity_operator,
        test_frozenset_cities,
    ]

    passed_count = 0
    for test in tests:
        test_name = test.__name__
        test()
        print("[PASS] " + test_name)
        passed_count += 1

    print("=" * 55)
    print("All " + str(passed_count) + " tests passed successfully!")
    print("=" * 55)


if __name__ == "__main__":
    run_all_tests()
