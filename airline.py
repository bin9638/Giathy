class Flight:
    def __init__(self, flight_number, departure, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.passengers = []

    def display_flight_info(self):
        print(f"Flight {self.flight_number} from {self.departure} to {self.destination}")
        print(f"Departure: {self.departure_time}, Arrival: {self.arrival_time}")

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
        else:
            print(f"{passenger.name} is not on this flight.")

class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def display_passenger_info(self):
        print(f"Passenger: {self.name}")
        print(f"Passport Number: {self.passport_number}")

class Ticket:
    def __init__(self, flight, passenger, seat_number):
        self.flight = flight
        self.passenger = passenger
        self.seat_number = seat_number

    def display_ticket_info(self):
        print("Ticket Information:")
        self.flight.display_flight_info()
        self.passenger.display_passenger_info()
        print(f"Seat Number: {self.seat_number}")

# Create some flights and passengers
flight1 = Flight("F123", "New York", "Los Angeles", "08:00 AM", "10:00 AM")
flight2 = Flight("F456", "Chicago", "Miami", "09:30 AM", "12:30 PM")

passenger1 = Passenger("Alice", "A12345")
passenger2 = Passenger("Bob", "B54321")

# Book tickets for passengers on flights
ticket1 = Ticket(flight1, passenger1, "A1")
ticket2 = Ticket(flight2, passenger2, "B2")

# Display ticket information
ticket1.display_ticket_info()
ticket2.display_ticket_info()

# Tadd and remove the passenger from the flight
flight1.add_passenger(passenger1)
flight2.add_passenger(passenger2)

flight1.remove_passenger(passenger2)