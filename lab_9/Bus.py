from Vehicles import Vehicle


class Bus(Vehicle):
    def __init__(self, type: str, model: str, fuel: str, num_of_passengers: int, route: str):
        super(Bus, self).__init__(type, model, fuel, num_of_passengers)
        self.route = route

    def __str__(self):
        return super(Bus, self).__str__() \
            + f"Daily route: {self.route}"
