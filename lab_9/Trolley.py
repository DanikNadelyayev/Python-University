from Vehicles import Vehicle

class Trolley(Vehicle):
    def __init__(self, type: str, model: str, fuel: str, num_of_passengers: int, route: str) -> None:
        super(Trolley, self).__init__(type, model, fuel, num_of_passengers)
        self.route = route

    def __str__(self):
        return super(Trolley, self).__str__() \
            + f"Route: {self.route}"

