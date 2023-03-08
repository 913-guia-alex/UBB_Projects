from Domain import *


class Service:
    def __init__(self):
        self.domain_bus = Bus("0", "0", "0", "0")
        self.domain_route = Route("0", "0")

    def read_bus_file(self):
        bus_list = []
        file = open("bus.txt", "r")
        for line in file:
            line = line.strip()
            bus = line.split(",")
            bus_list.append(Bus(bus[0], bus[1], bus[2], bus[3]))
        file.close()
        return bus_list

    def read_route_file(self):
        route_list = []
        file = open("routes.txt", "r")
        for line in file:
            line = line.strip()
            route = line.split(",")
            route_list.append(Route(route[0], route[1]))
        file.close()
        return route_list

    def store_bus_list(self):
        self.domain_bus.bus_list = self.read_bus_file()

    def store_route_list(self):
        self.domain_route.route_list = self.read_route_file()

    def start(self):
        self.store_bus_list()
        self.store_route_list()
