# data.py
# Predefined constants and seed data for the Bus Ticket Reservation System.

# Bitwise Amenity Flags (Legitimate feature flags for bus services)
# Bit 0 (1): Air Conditioning
# Bit 1 (2): WiFi
# Bit 2 (4): Sleeper Berth
AMENITY_AC = 1
AMENITY_WIFI = 2
AMENITY_SLEEPER = 4

# Frozen set of supported network cities (Immutable core data structure)
SERVICED_CITIES = frozenset(["Delhi", "Jaipur", "Agra", "Chandigarh", "Shimla"])

# Initial bus records stored as a list of dictionaries
INITIAL_BUSES = [
    {
        "bus_id": "BUS101",
        "bus_name": "Rajdhani Express",
        "route": ("Delhi", "Jaipur"),  # Tuple for fixed route pair
        "schedule": ("06:00 AM", "11:30 AM"),  # Tuple for fixed departure/arrival
        "base_fare": 450.0,
        "total_seats": 20,
        "amenities": AMENITY_AC | AMENITY_WIFI,  # Bitwise OR: 1 | 2 = 3
    },
    {
        "bus_id": "BUS102",
        "bus_name": "Pink City Deluxe",
        "route": ("Jaipur", "Delhi"),
        "schedule": ("02:00 PM", "07:30 PM"),
        "base_fare": 450.0,
        "total_seats": 20,
        "amenities": AMENITY_AC,  # Bitwise flag: 1
    },
    {
        "bus_id": "BUS103",
        "bus_name": "Taj Superfast",
        "route": ("Delhi", "Agra"),
        "schedule": ("07:00 AM", "10:30 AM"),
        "base_fare": 320.0,
        "total_seats": 16,
        "amenities": AMENITY_AC | AMENITY_WIFI | AMENITY_SLEEPER,  # 1 | 2 | 4 = 7
    },
    {
        "bus_id": "BUS104",
        "bus_name": "Himalayan Queen",
        "route": ("Chandigarh", "Shimla"),
        "schedule": ("08:00 AM", "01:00 PM"),
        "base_fare": 280.0,
        "total_seats": 16,
        "amenities": AMENITY_WIFI,  # Bitwise flag: 2
    },
]
