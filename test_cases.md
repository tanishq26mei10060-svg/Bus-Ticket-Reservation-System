# Test Cases: Bus Ticket Reservation System

This document outlines the manual test scenarios designed to verify all functional requirements and validation checks of the Bus Ticket Reservation System.

---

## Test Suite Summary

| Test ID | Test Scenario | Input Data | Expected Output | Status |
| :---: | :--- | :--- | :--- | :---: |
| **TC-01** | Display All Buses | Menu Option: `1` | Displays list of all 4 registered buses with IDs, routes, timings, fares, and amenities. | PASS |
| **TC-02** | Search Bus (Valid Route) | Menu Option: `2`<br>Source: `Delhi`<br>Destination: `Jaipur` | Displays bus `BUS101` (Rajdhani Express) matching Delhi to Jaipur. | PASS |
| **TC-03** | Search Bus (Invalid / Unserviced Route) | Menu Option: `2`<br>Source: `Mumbai`<br>Destination: `Goa` | Displays: `No buses found running from 'Mumbai' to 'Goa'.` | PASS |
| **TC-04** | View Bus Details & Seats | Menu Option: `3`<br>Bus ID: `BUS101` | Displays complete bus specifications, amenities (AC, WiFi), seat layout matrix, and occupancy rate. | PASS |
| **TC-05** | View Bus Details (Invalid Bus ID) | Menu Option: `3`<br>Bus ID: `BUS999` | Displays: `Error: No bus found with ID 'BUS999'.` | PASS |
| **TC-06** | Book Ticket (Valid Information) | Menu Option: `4`<br>Bus ID: `BUS101`<br>Name: `Aman Sharma`<br>Age: `20`<br>Gender: `M`<br>Seat: `5` | Ticket confirmed with Booking ID `B001`, Total Fare: `Rs. 450.0`, Seat `5` marked reserved. | PASS |
| **TC-07** | Book Ticket (Already Occupied Seat) | Menu Option: `4`<br>Bus ID: `BUS101`<br>Name: `Pooja Rao`<br>Age: `22`<br>Gender: `F`<br>Seat: `5` | Displays: `Error: Seat 5 is already occupied. Please select an open seat.` | PASS |
| **TC-08** | Book Ticket (Invalid Non-numeric Seat) | Menu Option: `4`<br>Bus ID: `BUS101`<br>Name: `Rohan`<br>Age: `25`<br>Gender: `M`<br>Seat: `ABC` | Displays: `Error: Seat number must be a valid integer.` (No program crash) | PASS |
| **TC-09** | Book Ticket (Out-of-range Age) | Menu Option: `4`<br>Bus ID: `BUS101`<br>Name: `Rohan`<br>Age: `150`<br>Gender: `M` | Displays: `Error: Age must be between 1 and 120.` | PASS |
| **TC-10** | Cancel Booking (Valid Booking ID) | Menu Option: `5`<br>Booking ID: `B001` | Displays: `Success: Booking ID 'B001' has been cancelled and seat released.` Seat 5 is restored. | PASS |
| **TC-11** | Cancel Booking (Non-existent ID) | Menu Option: `5`<br>Booking ID: `B999` | Displays: `Error: Booking ID 'B999' was not found in active records.` | PASS |
| **TC-12** | View All Bookings | Menu Option: `6` | Displays confirmed tickets list or `No bookings found in the system.` | PASS |
| **TC-13** | Seat Position Calculator | Menu Option: `7`<br>Seat Number: `7` | Computes via integer floor division and modulus: `Seat 7 is located at Row 2, Column 3 [Right Side].` | PASS |
| **TC-14** | View Serviced Cities | Menu Option: `8` | Displays all 5 frozen network hubs (Agra, Chandigarh, Delhi, Jaipur, Shimla). | PASS |
| **TC-15** | Invalid Menu Input | Menu Option: `99` or `abc` | Displays: `Invalid choice! Please enter a number between 1 and 9.` | PASS |
| **TC-16** | Clean Exit | Menu Option: `9` | Displays goodbye message and exits the program cleanly. | PASS |
