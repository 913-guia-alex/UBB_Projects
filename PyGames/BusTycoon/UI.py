from Domain import *
from Service import *


def check_int(cond):
    try:
        int(cond)
        return True
    except ValueError:
        return False


class UI:
    def __init__(self):
        self.service = Service()
        self.service.start()
        self.domain_bus = self.service.domain_bus
        self.domain_route = self.service.domain_route
        self.bus_list = self.service.read_bus_file()
        self.route_list = self.service.read_route_file()

    def print_menu(self):
        print("1. Display all buses on a route")
        print("2. Increase usage")
        print("3. Display buses by decreasing kilometers traveled")
        print("4. Display all buses")
        print("5 Display all routes")
        print("6. Exit")

    # display all buses across a sertain route given by the user
    def display_buses(self):
        while True:
            route_code = input("Enter route code: ")
            if not check_int(route_code):
                print('Invalid type!')
                continue
            route_code = int(route_code)
            found = False
            for bus in self.domain_bus.bus_list:
                if bus.get_route_code() == route_code:
                    print(bus)
                    found = True
            if found == False:
                print("No buses found!")
            break

    # display buses by decreasing kilometers traveled , to do this we multiply the time with the route length
    def display_buses_by_kilometers(self):
        for bus in self.domain_bus.bus_list:
            for route in self.domain_route.route_list:
                if bus.get_route_code() == route.get_route_code():
                    bus.set_time(bus.get_time() * route.get_route_length())
        self.domain_bus.bus_list.sort(key=lambda x: x.get_time(), reverse=True)
        for bus in self.domain_bus.bus_list:
            print(bus)

    def increase_usage(self):
        while True:
            bus_id = input("Enter bus id: ")
            route_code = input("Enter route code: ")
            if check_int(route_code) == False or check_int(bus_id) == False:
                print('Invalid type!')
                continue
            route_code = int(route_code)
            bus_id = int(bus_id)
            found_route = False
            found_bus = False
            for route in self.route_list:
                if route.get_route_code() == route_code:
                    found_route = True
            for bus in self.bus_list:
                if bus.get_bus_id() == bus_id and found_route == True and bus.get_route_code() == route_code:
                    found_bus = True
                    bus.set_time(bus.get_time() + 1)
                    print("Bus usage increased")
                    break
            if found_bus == False and found_route == True:
                print("Bus not found")
                break
            elif found_route == False and found_bus == True:
                print("Route not found")
                break
            elif found_bus == False and found_route == False:
                print("Neither bus nor route found")
                break
            break

    def print_list_of_buses(self):
        for bus in self.bus_list:
            print(bus)

    def print_list_of_routes(self):
        for route in self.route_list:
            print(route)

    def start(self):
        while True:
            self.print_menu()
            command = input("Enter command: ")
            if not check_int(command):
                print('Invalid type!')
                continue
            if command == "1":
                self.display_buses()
            elif command == "2":
                self.increase_usage()
            elif command == "3":
                self.display_buses_by_kilometers()
            elif command == "4":
                self.print_list_of_buses()
            elif command == "5":
                self.print_list_of_routes()
            elif command == "6":
                break
            else:
                print("Invalid command")
