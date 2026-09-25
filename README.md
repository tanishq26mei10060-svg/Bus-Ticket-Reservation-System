# Bus Ticket Reservation System

A simple, interactive, terminal-based Bus Ticket Reservation System developed in Python for the first-year B.Tech course **"Python Essentials"**.

This project demonstrates core programming concepts, fundamental data structures, control flow statements, and beginner-level Object-Oriented Programming (OOP) without using external libraries, databases, or graphical frameworks.

---

## 1. Project Description
The Bus Ticket Reservation System simulates an intercity bus booking counter. Through a clean, numbered terminal menu, users can browse available buses, search for specific routes, inspect seat availability and occupancy, book tickets with custom seat selection, calculate fares, and cancel bookings.

---

## 2. Objectives
* Build an operational console application using only first-year Python topics.
* Manage in-memory bus schedules, seat assignments, and confirmed reservations.
* Demonstrate practical application of Lists, Tuples, Sets, Dictionaries, Frozen Sets, and Arrays.
* Implement Object-Oriented domain entities (`Bus`, `Passenger`, `Booking`, `BusReservationSystem`).
* Apply safe, exception-free input validation using standard conditional checks.

---

## 3. Features
1. **Display All Buses:** View list of scheduled buses with route, departure/arrival times, fare, and amenities.
2. **Search Bus by Route:** Filter buses matching specified source and destination cities.
3. **View Bus Details & Seats:** Inspect individual bus specifications, seat layout array, and occupancy rate.
4. **Book a Ticket:** Book a seat with passenger name, age, and gender validation. Generates a formatted ticket receipt.
5. **Cancel a Booking:** Cancel an existing ticket by Booking ID; automatically restores the seat to the available pool.
6. **View All Bookings:** Display all active confirmed tickets.
7. **Seat Position Calculator:** Calculates the exact physical row and column for any seat number using floor division (`//`) and modulus (`%`).
8. **View Serviced Cities:** Lists all cities supported across the transit network using an immutable `frozenset`.
9. **Clean Exit:** Graceful program termination.

---

## 4. Technologies Used
* **Language:** Python 3 (Version 3.8 or newer recommended)
* **Libraries:** Pure Python standard library only (`array`, `sys`, `os`).
* **External Dependencies:** None. No `pip install` required.

---

## 5. Python Concepts Used

| Syllabus Topic | Usage in Project |
| :--- | :--- |
| **Python Fundamentals** | Clean indentation, descriptive variable names, inline documentation. |
| **Membership Operators** | `in` and `not in` checking seat availability in sets, bus keys in dictionaries. |
| **Assignment Operators** | `=`, `+=` incrementing booking counters, `-=` in seat tallies. |
| **Bitwise Operators** | Standard binary flags for bus amenities: AC (`1`), WiFi (`2`), Sleeper (`4`). Combined with `\|`, tested with `&`. |
| **`type()` Function** | Type validation verifying passenger attributes during booking and in testing. |
| **Identity Operators** | `is None` and `is not None` to test object lookups. |
| **Arithmetic Operators** | `+`, `-`, `*`, `/`, `//`, `%` in fare computation, row/column positioning, and line formatting. |
| **Logical Operators** | `and`, `or`, `not` in compound conditions and input verification. |
| **Relational Operators** | `==`, `!=`, `<`, `>`, `<=`, `>=` for menu selection and age bounds. |
| **Division Operators** | Single slash `/` (float occupancy rate) and floor division `//` (integer row number). |
| **I/O Operations** | `input()` for terminal prompts, formatted `print()` for menus and tickets. |
| **Operator Precedence** | Natural evaluation in `((seat_num - 1) // 4) + 1` and fare pricing formulas. |
| **Type Conversion** | Explicit conversions: `int()`, `float()`, `str()`. |
| **Data Structures** | List (sequences), Tuple (routes & schedules), Set (available seats), Dict (fast ID lookups), Frozenset (city network). |
| **Control Flow** | `while True:`, `for`, `if`/`elif`/`else`, `break`, `continue`. |
| **Functions** | Modularity across menu display and ticket calculation routines. |
| **Modules & Packages** | Multi-file organization with standard `import` statements. |
| **Array Data Structure** | `array('i', ...)` for storing physical seat numbers in the bus. |
| **Object-Oriented Programming** | `Bus`, `Passenger`, `Booking`, and `BusReservationSystem` classes. |

---

## 6. Project Structure

```text
bus_ticket_reservation/
│
├── data.py                 # City network frozenset, amenity bitmasks, and seed bus data
├── bus.py                  # Bus class with seat array and available seat set
├── booking.py              # Passenger and Booking classes
├── system.py               # BusReservationSystem controller class
├── main.py                 # Menu loop and CLI interaction
│
├── tests/
│   └── test_project.py     # Assert-based test suite (no external test framework)
│
├── test_cases.md           # Manual testing scenarios and results
├── report.md               # Academic project report for viva and submission
└── README.md               # Project documentation
```

---

## 7. Requirements
* Python 3.8+ installed on your system.
* No additional packages or dependencies needed.

---

## 8. Installation & Setup
1. Clone or copy the project folder to your local machine:
   ```bash
   cd C:\Users\vlogs\.gemini\antigravity\scratch\bus_ticket_reservation
   ```
2. Verify Python is installed:
   ```bash
   python --version
   ```

---

## 9. How to Run the Project from Terminal

### Running the Application:
From the `bus_ticket_reservation` directory, execute:
```bash
python main.py
```

### Running the Automated Tests:
Execute the assertion test suite directly using standard Python:
```bash
python tests/test_project.py
```

---

## 10. Sample Menu

```text
==================================================
          BUS TICKET RESERVATION SYSTEM          
==================================================
1. Display All Buses
2. Search Bus by Route
3. View Bus Details & Available Seats
4. Book a Ticket
5. Cancel a Booking
6. View All Bookings
7. Check Seat Position (Row/Col Calculator)
8. View Serviced Cities (Network Info)
9. Exit
==================================================
Enter your choice (1-9):
```

---

## 11. Example Usage Walkthrough

### 1. View Available Buses (Option 1)
```text
Enter your choice (1-9): 1

--- AVAILABLE BUS SERVICES ---
--------------------------------------------------
Bus ID         : BUS101
Bus Name       : Rajdhani Express
Route          : Delhi -> Jaipur
Departure/Arr  : 06:00 AM - 11:30 AM
Base Fare      : Rs. 450.0
Available Seats: 20 / 20
Amenities      : AC, WiFi
--------------------------------------------------
```

### 2. Book a Ticket (Option 4)
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

### 3. Cancel a Booking (Option 5)
```text
Enter your choice (1-9): 5

--- CANCEL A BOOKING ---
Enter Booking ID to cancel (e.g., B001): B001
Success: Booking ID 'B001' has been cancelled and seat released.
```

---

## 12. Limitations
* **In-Memory Storage:** Bookings and seat status reside in memory during runtime and reset when the terminal session ends.
* **Single User:** Designed for sequential terminal interactions, not concurrent multi-user environments.

---

## 13. Future Scope
* Adding basic file handling (`open()`, `.txt`) to persist bookings to disk.
* Administrative mode to add new routes and modify ticket pricing dynamically.
* Visual ASCII representation of occupied and vacant seats on a 2D bus layout.
