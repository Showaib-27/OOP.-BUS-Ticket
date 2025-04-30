class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    
    def available_seats(self):
        available_seats = self.total_seats - self.booked_seats
        return available_seats
    
    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False

class Passenger:
    def __init__(self,name,phone, bus):
        self.name = name
        self.bus = bus
        self.phone = phone
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password
           
class BusSystem:
    def __init__(self):
        self.buses = []
        self.passenger = []
        self.admin = Admin("admin", "1234")
        
    def add_bus(self,number, route, seats):
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print(f"Bus{number} added successfully....!")
    

    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None       

    def book_ticket(self,bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if bus and bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.passenger.append(passenger)
            print(f"Ticket purchase successfully for {name}! Price:500 tk")
        else:
            print("Booking Failed..! Try again letter")

    def show_buses(self):
        if not self.buses:
            print("NO Buses available..!")
            return
        for bus in self.buses:
            print("f Bus: {bus.number} - Route: {bus.route} - Available Seats: {bus.available_seats()}")
    def user_menu(self):
                print("\n**********User Menu**********")
                print("1. Admin Login")
                print("2. Book Ticket")
                print("3. View Buses")
                print("4. Exit")  
   

    def admin_menu(self):
        print("\n-----------Admin Menu-------------")
        print("1. Add Bus")
        print("2. View All Bus")
        print("3. LogOut")
 
def main():
    system = BusSystem()

    while True:
        system.user_menu()
        choice = input("Enter Your  choice: ")
        if choice == "1":
            username = input("Admin Username: ")
            password = input("Admin password: ")

            if system.admin.login(username, password):
                print("Login successfully...!")
                while True:
                    system.admin_menu()
                    admin_choice = input("Hello Admin..! Enter Your choice: ")
                    if admin_choice == "1":   #add bus
                        number = input("Bus Number: ")
                        route = input("Bus route: ")
                        seats = input("Total seats: ")

                        if seats.isdigit():
                            system.add_bus(number,route,int(seats)) # str teke int e convert korteci
                        else:
                            print("Invalid... Try again later")
                    elif admin_choice == "2":
                        system.show_buses()
                    elif admin_choice =="3":
                        print("Logged Out.")
                        break
                    else:
                        ("Invalid Choice.. choose valid option..")
            else:
                print("invalid infO..")
        elif choice == "2":  
            # book ticket
            bus_number = input("Bus Number: ")
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            system.book_ticket(bus_number,name,phone)
        elif choice =="3":
            system.show_buses()
        elif choice == "4":
            print("Thanks you for belive us")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()