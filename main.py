# main.py
# Command-Line User Interface for the Bus Ticket Reservation System.
# Built strictly using first-year Python topics without exception handling.

from data import INITIAL_BUSES, SERVICED_CITIES
from system import BusReservationSystem
from booking import Passenger


def display_menu():
    print("\n" + "=" * 50)
    print("          BUS TICKET RESERVATION SYSTEM          ")
    print("=" * 50)
    print("1. Display All Buses")
    print("2. Search Bus by Route")
    print("3. View Bus Details & Available Seats")
    print("4. Book a Ticket")
    print("5. Cancel a Booking")
    print("6. View All Bookings")
    print("7. Check Seat Position (Row/Col Calculator)")
    print("8. View Serviced Cities (Network Info)")
    print("9. Exit")
    print("=" * 50)


def handle_display_all_buses(system):
    buses = system.get_all_buses()
    print("\n--- AVAILABLE BUS SERVICES ---")
    if len(buses) == 0:
        print("No buses are currently registered in the system.")
    else:
        for bus in buses:
            bus.display_details()


def handle_search_buses(system):
    print("\n--- SEARCH BUSES BY ROUTE ---")
    source = input("Enter Source City: ").strip()
    destination = input("Enter Destination City: ").strip()

    # Logical OR to check for empty inputs
    if source == "" or destination == "":
        print("Error: Source and Destination cannot be empty.")
        return

    matching_buses = system.search_buses(source, destination)
    if len(matching_buses) == 0:
        print("No buses found running from '" + source + "' to '" + destination + "'.")
    else:
        print("\nFound " + str(len(matching_buses)) + " matching bus(es):")
        for bus in matching_buses:
            bus.display_details()


def handle_view_bus_details(system):
    print("\n--- VIEW BUS DETAILS & SEATS ---")
    bus_id = input("Enter Bus ID (e.g., BUS101): ").strip().upper()

    bus = system.find_bus(bus_id)
    # Identity operator check against None
    if bus is None:
        print("Error: No bus found with ID '" + bus_id + "'.")
        return

    bus.display_details()

    # Demonstrating division for mixed data types: calculating occupancy percentage (float result)
    booked_count = bus.total_seats - len(bus.available_seats)
    occupancy_rate = (booked_count / bus.total_seats) * 100.0

    # Displaying all seats from the array structure
    print("Seat Configuration:")
    seat_status_list = []
    for seat in bus.all_seats:
        if bus.is_seat_available(seat):
            seat_status_list.append("[" + str(seat) + ":Open]")
        else:
            seat_status_list.append("[" + str(seat) + ":Booked]")

    print("  " + " ".join(seat_status_list))
    print("Current Bus Occupancy: " + str(occupancy_rate) + "%")


def handle_book_ticket(system):
    print("\n--- BOOK A BUS TICKET ---")
    bus_id = input("Enter Bus ID (e.g., BUS101): ").strip().upper()

    bus = system.find_bus(bus_id)
    if bus is None:
        print("Error: Bus ID '" + bus_id + "' does not exist.")
        return

    if len(bus.available_seats) == 0:
        print("Sorry, this bus is completely full!")
        return

    # Passenger Name validation (no try/except)
    name = input("Enter Passenger Name: ").strip()
    if name == "":
        print("Error: Passenger name cannot be blank.")
        return

    # Passenger Age validation using .isdigit()
    age_input = input("Enter Passenger Age: ").strip()
    if not age_input.isdigit():
        print("Error: Age must be a positive integer.")
        return
    age = int(age_input)
    # Relational and logical AND operators
    if age < 1 or age > 120:
        print("Error: Age must be between 1 and 120.")
        return

    # Gender validation using membership operator 'in'
    gender = input("Enter Passenger Gender (M/F/O): ").strip().upper()
    if gender not in ["M", "F", "O"]:
        print("Error: Gender must be M (Male), F (Female), or O (Other).")
        return

    # Display available seats for ease of selection
    sorted_available = sorted(list(bus.available_seats))
    avail_str = ", ".join([str(s) for s in sorted_available])
    print("Currently available seat numbers: " + avail_str)

    # Seat Number validation using .isdigit()
    seat_input = input("Enter desired seat number: ").strip()
    if not seat_input.isdigit():
        print("Error: Seat number must be a valid integer.")
        return
    seat_number = int(seat_input)

    # Validation against seat bounds
    if seat_number < 1 or seat_number > bus.total_seats:
        print("Error: Invalid seat number. Bus only has seats 1 to " + str(bus.total_seats) + ".")
        return

    # Validation against availability
    if not bus.is_seat_available(seat_number):
        print("Error: Seat " + str(seat_number) + " is already occupied. Please select an open seat.")
        return

    # Demonstrating type() function to verify passenger data type before creation
    passenger = Passenger(name, age, gender)
    if type(passenger.age) is int and type(passenger.name) is str:
        # Proceed with booking
        booking = system.book_ticket(bus_id, passenger, seat_number)
        if booking is not None:
            print("\nTicket booked successfully!")
            booking.display_ticket()
        else:
            print("Error: Booking failed due to an unexpected seat conflict.")


def handle_cancel_booking(system):
    print("\n--- CANCEL A BOOKING ---")
    booking_id = input("Enter Booking ID to cancel (e.g., B001): ").strip().upper()

    if booking_id == "":
        print("Error: Booking ID cannot be empty.")
        return

    # Cancel ticket via system
    is_cancelled = system.cancel_booking(booking_id)
    if is_cancelled:
        print("Success: Booking ID '" + booking_id + "' has been cancelled and seat released.")
    else:
        print("Error: Booking ID '" + booking_id + "' was not found in active records.")


def handle_view_all_bookings(system):
    print("\n--- ALL CONFIRMED BOOKINGS ---")
    bookings = system.get_all_bookings()
    if len(bookings) == 0:
        print("No bookings found in the system.")
    else:
        print("Total Active Bookings: " + str(len(bookings)))
        for booking in bookings:
            booking.display_ticket()


def handle_seat_position_calculator(system):
    print("\n--- SEAT POSITION CALCULATOR ---")
    print("Our buses use a standard 4-seats-per-row layout (Seats 1-2 Left, Seats 3-4 Right).")
    seat_input = input("Enter seat number to locate (e.g., 7): ").strip()

    if not seat_input.isdigit():
        print("Error: Seat number must be a valid number.")
        return

    seat_num = int(seat_input)
    if seat_num <= 0:
        print("Error: Seat number must be greater than zero.")
        return

    # Demonstrates floor division (//) and modulus (%)
    row, col = system.calculate_seat_position(seat_num)
    side = "Left Side (Window/Aisle)" if (col == 1 or col == 2) else "Right Side (Aisle/Window)"
    print("Seat " + str(seat_num) + " is located at Row " + str(row) + ", Column " + str(col) + " [" + side + "].")


def handle_view_serviced_cities():
    print("\n--- SERVICED CITIES NETWORK ---")
    # Demonstrating frozenset iteration and membership
    print("Cities in our frozen network directory:")
    for city in sorted(list(SERVICED_CITIES)):
        print(" - " + city)
    print("Total network hubs: " + str(len(SERVICED_CITIES)))


def main():
    # Initialize the core reservation system
    system = BusReservationSystem()
    system.load_initial_data(INITIAL_BUSES)

    print("Welcome to the Bus Ticket Reservation System!")
    print("System initialized with " + str(len(system.buses)) + " scheduled buses.")

    # Control flow statement: while loop for interactive menu
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        # Relational and logical OR operators
        if choice == "1":
            handle_display_all_buses(system)
        elif choice == "2":
            handle_search_buses(system)
        elif choice == "3":
            handle_view_bus_details(system)
        elif choice == "4":
            handle_book_ticket(system)
        elif choice == "5":
            handle_cancel_booking(system)
        elif choice == "6":
            handle_view_all_bookings(system)
        elif choice == "7":
            handle_seat_position_calculator(system)
        elif choice == "8":
            handle_view_serviced_cities()
        elif choice == "9" or choice.lower() == "exit":
            print("\nThank you for using the Bus Ticket Reservation System. Goodbye!")
            # Control flow statement: break out of loop
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")
            # Control flow statement: continue to re-display menu
            continue


if __name__ == "__main__":
    main()
