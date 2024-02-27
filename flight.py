class airline:
    def __init__(self, name):
      self.name = name
      self.ticket = []
      self.passenger = []
      self.flight = []
      self.count_ticket = 0
    
    def add_flight(self):
      id_flight = input("Input flight ID: ")
      plane = input("Input plane's name: ")
      departure = input("Input departure: ")
      destination = input("Input destination: ")
      time = input("Input depart time: ")
      capacity = input("Input capacity: ")
      new_flight = flight(id_flight, plane, departure, destination, time, capacity)
      print(f"add flight successfully.")

    def add_passenger(self):
      name = input("Input passenger's name:")
      id_passenger = input("Input passenger ID:")
      nationality = input("Input passenger's nationality:")
      age = input("Input passenger's age")
      new_passenger = passenger(name, id_passenger, nationality, age)
      self.passenger.append(new_passenger)
      print(f"add passenger successfully.")
   
    def check_infor(self):
        id_flight = input("Input your flight ID: ")
        for i in range(self.flight.__len__()):
           if self.flight[i].id_flight == id_flight:
              self.flight[i].information()
              return True
        print(f"Your flight is unavailable")

    def book_ticket(self):
        id_flight = input("Input your flight ID: ")
        id_passenger = input("Input your passenger ID: ")
        for i in range(self.flight.__len__()):
           if self.flight[i].id_flight == id_flight:
                if self.flight[i].add_passenger == True:
                  new_tic = ticket(self.count_ticket, id_passenger, id_flight)
                  self.ticket.append(new_tic)
                  self.count_ticket+=1
                  print(f"You have booked ticket successfully, your ticket ID is {new_tic.id_ticket}")
                  return True
        print(f"You have booked ticket unsuccessfully")

    def cancel_ticket(self):
      id_ticket= input("Input your ticket ID: ")
      for i in range(self.ticket.__len__()):
        if self.ticket[i].id_ticket == id_ticket:
            for j in range(self.flight.__len__()):
                if self.flight[j].id_flight == self.ticket[i].id_flight:
                  self.flight[j].remove_passenger()
            print(f"You have cancelled ticket successfully")
            self.ticket.pop(i)
            return True
      print(f"You have cancelled ticket unsuccessfully")

class flight:
   
    def __init__(self, id_flight, plane, departure, destination, time, max_passenger):
      self.id_flight = id_flight
      self.plane = plane
      self.departure = departure
      self.destination = destination
      self.time = time
      self.max_passenger = max_passenger
      self.current_passenger = 0

    def information(self):
      print(f"Plane {self.plane} will take off from {self.departure} at {self.time} and land in {self.destination}, ID of flight is {self.id_flight}")

    def add_passenger(self):
      if self.current_passenger < self.max_passenger:
        self.current_passenger+=1
        return True
      return False
   
    def remove_passenger(self):
      self.current_passenger-=1
    

class ticket:

    def __init__(self, id_ticket, id_passenger, id_flight):
        self.id_ticket = id_ticket
        self.id_flight = id_flight
        self.id_passenger = id_passenger

class passenger:
   
    def __init__(self, name, id_passenger, nationality, age):
      self.name = name
      self.id_passenger = id_passenger
      self.age = age
      self.nationality = nationality

VN = airline("VietNam airline")

while True:
    print(f"Choose your operation:")
    print(f"1: Add new flight")
    print(f"2: Add new passenger")
    print(f"3: Book ticket")
    print(f"4: Cancel ticket")
    print(f"5: check flight information")
    print(f"6: End")
    type =int(input("Input your operation: "))
    if type == 1:
      VN.add_flight()
    if type == 2:
       VN.add_passenger()
    if type == 3:
       VN.book_ticket()
    if type == 4:
        VN.cancel_ticket
    if type == 5:
        VN.check_infor()
    if(type == 6):
        break

    
