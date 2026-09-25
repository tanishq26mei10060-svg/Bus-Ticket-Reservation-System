# Academic Project Report: Bus Ticket Reservation System

**Course:** Python Essentials  
**Academic Year:** First-Year B.Tech  
**Project Title:** Bus Ticket Reservation System  
**Submission Date:** September 30, 2026  

---

## 1. Title
**Bus Ticket Reservation System in Python**

---

## 2. Introduction
The Bus Ticket Reservation System is a terminal-based console application developed as part of the first-year B.Tech curriculum for the course "Python Essentials". The software simulates the core operations of an intercity passenger bus ticketing counter. It allows users to browse scheduled bus routes, query route availability, view real-time seat status, book tickets with seat selection, calculate fares, and cancel reservations.

The application has been engineered exclusively using the foundational principles taught within the first-year syllabus, avoiding external third-party libraries, complex database servers, and graphical user interfaces.

---

## 3. Problem Statement
In traditional manual ticket counters, managing bus occupancy, seat allocation, and ticket cancellation leads to clerical errors, double-booking, and slow service. Developing a computerized system eliminates these issues. 

For students learning computer programming, designing a functional reservation system offers a realistic scenario to apply core data structures (lists, tuples, sets, dictionaries, arrays), control flow constructs, functions, and fundamental object-oriented programming without relying on automated black-box libraries.

---

## 4. Objectives
1. To implement an interactive, menu-driven bus ticketing system running on standard Python.
2. To manage bus routes, schedules, seat occupancy, and customer bookings using in-memory Python data structures.
3. To prevent duplicate seat bookings and calculate accurate fares based on seat positioning.
4. To apply Object-Oriented Programming (OOP) concepts (`class`, `object`, `__init__`, instance methods) in a clean, modular architecture.
5. To perform input validation without complex exception-handling frameworks, relying on conditional logic and built-in type verification.

---

## 5. Scope
The application is scoped to simulate the operations of a regional bus transport agency connecting 5 northern cities (Delhi, Jaipur, Agra, Chandigarh, Shimla).
* **Included:** Preloaded bus schedules, route-based bus search, seat availability checking, ticket booking, seat position calculation, ticket cancellation, and automated assertion testing.
* **Excluded:** Persistent SQL/file databases, online payment gateways, SMS notifications, and GUI windows (as these exceed the first-year curriculum).

---

## 6. Technologies Used
* **Programming Language:** Python 3 (3.8+)
* **Standard Library Modules Used:**
  * `array` (for homogeneous seat storage)
  * `sys` and `os` (for test runner directory resolution)
* **Execution Environment:** Command-Line Interface (CLI) / Terminal
* **External Dependencies:** None (Zero third-party packages)

---

## 7. Python Concepts Used

The project maps directly to the 21 topics of the "Python Essentials" syllabus:

1. **Python Fundamentals:** Standard indentation, identifiers, variables, and clean commenting conventions.
2. **Membership Operators (`in`, `not in`):** Used to check seat vacancy in sets (`seat in available_seats`), city network validity, and bus IDs in dictionaries.
3. **Assignment Operators (`=`, `+=`, `-=`):** Used for variable initialization, incrementing booking counters (`booking_counter += 1`), and seat counting.
4. **Bitwise Operators (`|`, `&`):** Used for legitimate feature flags representing bus amenities (Air Conditioning = `1`, WiFi = `2`, Sleeper Berth = `4`). Combining features uses `|`, testing active features uses `&`.
5. **`type()` Function:** Used to verify that passenger inputs and seat numbers match expected basic data types before ticket generation.
6. **Identity Operators (`is`, `is not`):** Used legitimately to test against `None` when searching for buses and bookings (e.g., `if bus is None:`).
7. **Arithmetic Operators (`+`, `-`, `*`, `/`, `//`, `%`):** Used for fare calculations, line dividers (`"=" * 50`), and coordinate math.
8. **Logical OR Operator (`or`):** Used for multi-condition input checking (e.g., `if source == "" or destination == "":`).
9. **Logical NOT Operator (`not`):** Used to verify negation (e.g., `if not bus.is_seat_available(seat_num):`).
10. **Logical AND Operator (`and`):** Used to validate range constraints (e.g., `if age >= 1 and age <= 120:`).
11. **Relational / Comparison Operators (`==`, `!=`, `<`, `>`, `<=`, `>=`):** Used for menu selection and seat boundary checks.
12. **Division Operators for Mixed Data Types:** Single slash `/` for calculating bus occupancy percentage (`float`), and double slash `//` for seat row indexing (`int`).
13. **Input and Output Operations:** `input()` for receiving passenger details and `print()` for formatted ticket receipts.
14. **Operator Precedence and Associativity:** Evaluated in mathematical formulas such as row index computation `((seat_num - 1) // 4) + 1`.
15. **Type Conversion:** Explicit conversions using `int()`, `float()`, and `str()`.
16. **Core Data Structures:**
    * **List:** Iterating through buses and booking records.
    * **Tuple:** Fixed pairs for bus routes `(source, destination)` and schedules `(departure, arrival)`.
    * **Set:** Dynamic tracking of available seats (`available_seats`) supporting $O(1)$ addition and removal.
    * **Dictionary:** Fast lookup of bus records by `bus_id` and tickets by `booking_id`.
    * **Frozen Set:** Immutable set of serviced cities (`SERVICED_CITIES`).
17. **Control Flow Statements:** `while True:` loop for the main menu, `for` loops for iteration, `if`/`elif`/`else` for decision branching, `break` to exit, and `continue` to handle input re-prompting.
18. **Functions:** Modular utility routines (`display_menu()`, `calculate_seat_position()`, `handle_book_ticket()`).
19. **Modules and Packages:** Division of code into logical files (`data.py`, `bus.py`, `booking.py`, `system.py`, `main.py`).
20. **Array Data Structure:** Standard `array('i', ...)` storing physical seat numbers in the bus chassis.
21. **Object-Oriented Programming (OOP):** Domain modeling using classes (`Bus`, `Passenger`, `Booking`, `BusReservationSystem`) with `__init__` and instance methods.

---

## 8. System Design / Program Flow

```text
                  +-----------------------------+
                  |         Program Start       |
                  +-----------------------------+
                                 |
                                 v
                  +-----------------------------+
                  |  Initialize System & Seed   |
                  |  Load Buses from data.py    |
                  +-----------------------------+
                                 |
                                 v
                   +---------------------------+
                   |     Display Main Menu     |<-------------+
                   +---------------------------+              |
                                 |                            |
                 +---------------+---------------+            |
                 |               |               |            |
                 v               v               v            |
           [1. View Buses] [2. Search]   [4. Book Ticket]     |
                 |               |               |            |
                 v               v               v            |
             Display          Filter by        Validate       |
             Details         Source/Dest      Input & Seat    |
                 |               |               |            |
                 |               |         Confirm Booking    |
                 |               |         Generate Ticket    |
                 |               |               |            |
                 +---------------+---------------+            |
                                 |                            |
                 +---------------+---------------+            |
                 |               |               |            |
                 v               v               v            |
           [5. Cancel]    [6. Bookings]    [9. Exit Program]  |
                 |               |               |            |
             Release Seat   Print List        Terminate       |
             Delete Ticket  of Tickets         Process        |
                 |               |                            |
                 +---------------+----------------------------+
```

---

## 9. Modules

1. **`data.py`:** Holds static configuration, city frozenset, amenity bitmasks, and initial bus schedules.
2. **`bus.py`:** Contains the `Bus` class managing physical seats and occupancy.
3. **`booking.py`:** Contains `Passenger` and `Booking` classes representing tickets.
4. **`system.py`:** Central controller class managing state dictionaries and transactional methods.
5. **`main.py`:** Terminal user interface and interactive menu loop.
6. **`tests/test_project.py`:** Assert-based test suite verifying system integrity.

---

## 10. Classes

### 1. `Passenger` (in `booking.py`)
* **Attributes:** `name` (`str`), `age` (`int`), `gender` (`str`).
* **Methods:** `__init__()`, `display_passenger()`.

### 2. `Booking` (in `booking.py`)
* **Attributes:** `booking_id` (`str`), `bus_id` (`str`), `passenger` (`Passenger`), `seat_number` (`int`), `fare` (`float`).
* **Methods:** `__init__()`, `display_ticket()`.

### 3. `Bus` (in `bus.py`)
* **Attributes:** `bus_id` (`str`), `bus_name` (`str`), `route` (`tuple`), `schedule` (`tuple`), `base_fare` (`float`), `total_seats` (`int`), `amenities` (`int`), `all_seats` (`array`), `available_seats` (`set`).
* **Methods:** `__init__()`, `get_amenities_list()`, `display_details()`, `is_seat_available()`, `reserve_seat()`, `release_seat()`.

### 4. `BusReservationSystem` (in `system.py`)
* **Attributes:** `buses` (`dict`), `bookings` (`dict`), `booking_counter` (`int`).
* **Methods:** `__init__()`, `load_initial_data()`, `get_all_buses()`, `find_bus()`, `search_buses()`, `calculate_seat_position()`, `calculate_fare()`, `book_ticket()`, `cancel_booking()`, `get_all_bookings()`.

---

## 11. Functions

* `display_menu()`: Formats and outputs the 9 available terminal actions.
* `handle_display_all_buses(system)`: Iterates through and displays all registered buses.
* `handle_search_buses(system)`: Accepts user origin and destination and displays matching routes.
* `handle_view_bus_details(system)`: Displays detailed information, seat layout array, and occupancy rate.
* `handle_book_ticket(system)`: Collects passenger details, validates seat availability, and creates a confirmed booking.
* `handle_cancel_booking(system)`: Cancels an active booking ID and releases the seat.
* `handle_view_all_bookings(system)`: Displays all confirmed tickets currently in memory.
* `handle_seat_position_calculator(system)`: Calculates row and column coordinates from a seat number using integer arithmetic.
* `handle_view_serviced_cities()`: Iterates over the `SERVICED_CITIES` frozenset.

---

## 12. Data Structures Used

* **List:** Used to store collections of buses for display and iterate over search results.
* **Tuple:** Used for immutable pairs: route `("Delhi", "Jaipur")` and schedule `("06:00 AM", "11:30 AM")`.
* **Set:** Used for `available_seats`. Allows instantaneous check (`seat in available_seats`) and automatic uniqueness.
* **Dictionary:** Key-value pairs for $O(1)$ lookups: `buses[bus_id]` and `bookings[booking_id]`.
* **Frozen Set:** Immutable set `SERVICED_CITIES` that guards the transit network against accidental modification.
* **Array:** Fixed integer typecode `'i'` array representing the manufactured physical seats in the vehicle.

---

## 13. Working of the System

1. **Initialization:** On startup, `main()` instantiates `BusReservationSystem` and populates it with 4 seed buses from `data.py`.
2. **Browsing & Searching:** Passengers browse routes or search by typing their starting city and destination.
3. **Seat Selection:** When booking, the system presents all remaining open seat numbers.
4. **Validation:** All inputs are validated using `.isdigit()`, boundary checks, and membership tests without triggering uncaught exceptions.
5. **Ticketing:** The system assigns a sequential ID (`B001`, `B002`), removes the seat from `available_seats`, computes the fare, and prints a formatted ticket.
6. **Cancellation:** When a booking ID is provided for cancellation, the system identifies the bus, restores the seat to the `available_seats` set, and deletes the booking record.

---

## 14. Sample Input / Output

### Booking a Ticket
```text
Enter your choice (1-9): 4

--- BOOK A BUS TICKET ---
Enter Bus ID (e.g., BUS101): BUS101
Enter Passenger Name: Rahul Sharma
Enter Passenger Age: 21
Enter Passenger Gender (M/F/O): M
Currently available seat numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
Enter desired seat number: 3

Ticket booked successfully!
=============================================
           CONFIRMED BUS TICKET           
=============================================
Booking ID     : B001
Bus ID         : BUS101
Passenger Name : Rahul Sharma
Age / Gender   : 21 / M
Seat Number    : 3
Total Fare     : Rs. 500.0
=============================================
```

---

## 15. Testing
The application underwent automated testing through `tests/test_project.py` using standard Python `assert` statements. 

Ten distinct automated test cases were executed:
1. `test_bus_initialization` — Verified object attributes and data types.
2. `test_amenity_bitwise_flags` — Tested bitwise OR and bitwise AND operations.
3. `test_seat_array_type` — Verified the `array.array('i')` structure.
4. `test_search_buses` — Verified route matching and non-matching behavior.
5. `test_book_ticket_success` — Verified sequential ID assignment and seat set removal.
6. `test_book_ticket_duplicate_seat` — Verified collision rejection when attempting to book an occupied seat.
7. `test_cancel_booking` — Verified seat recovery and record deletion.
8. `test_seat_math_precedence` — Verified integer floor division (`//`) and modulus (`%`) for layout coordinates.
9. `test_identity_operator` — Verified legitimate usage of `is None` and `is not None`.
10. `test_frozenset_cities` — Verified immutable set membership.

**Result:** All 10 tests passed with 0 errors.

---

## 16. Limitations
1. **Volatile Memory:** Because file persistence and database engines are outside the course scope, all reservations reset when the program terminates.
2. **Single-User Terminal Interface:** The application is designed for single-operator console execution and does not support simultaneous network access.
3. **Fixed Schedule:** Bus departure timings are predefined and cannot be edited dynamically during runtime.

---

## 17. Future Scope
1. **File Storage:** Integrate basic text file handling (`open()`, `read()`, `write()`) to preserve bookings across sessions.
2. **Dynamic Scheduling:** Allow transport administrators to add new routes, buses, and modify fares at runtime.
3. **Seat Matrix Visualization:** Implement an ASCII graphical layout rendering window seats vs. aisle seats.

---

## 18. Conclusion
The Bus Ticket Reservation System successfully demonstrates how foundational programming constructs, data structures, and beginner Object-Oriented Programming can solve a practical real-world problem. By adhering strictly to the first-year "Python Essentials" syllabus, the project illustrates clear, maintainable, and understandable Python code suitable for academic evaluation.
