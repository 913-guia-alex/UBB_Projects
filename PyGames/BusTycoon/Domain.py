#class for a route that stores the route route code and lenght in kilometers
class Route:
    def __init__(self, route_code, route_length):
        self.route_code = int(route_code)
        self.route_length = int(route_length)
        self.route_list = []

    def __str__(self):
        return "Route code: " + str(self.route_code) + " Route length: " + str(self.route_length)

    def get_route_code(self):
        return self.route_code

    def get_route_length(self):
        return self.route_length

    def set_route_code(self, route_code):
        self.route_code = route_code

    def set_route_length(self, route_length):
        self.route_length = route_length

#class for a bus that stores bus id unique to the bus , route code , model and time used for the route in minutes
class Bus:
    def __init__(self, bus_id, route_code, model, time):
        self.bus_id = int(bus_id)
        self.route_code = int(route_code)
        self.model = model
        self.time = int(time)
        self.bus_list = []

    def __str__(self):
        return "Bus id: " + str(self.bus_id) + " Route code: " + str(self.route_code) + " Model: " + str(self.model) + " Time: " + str(self.time)

    def get_bus_id(self):
        return self.bus_id

    def get_route_code(self):
        return self.route_code

    def get_model(self):
        return self.model

    def get_time(self):
        return self.time

    def set_bus_id(self, bus_id):
        self.bus_id = bus_id

    def set_route_code(self, route_code):
        self.route_code = route_code

    def set_model(self, model):
        self.model = model

    def set_time(self, time):
        self.time = time
