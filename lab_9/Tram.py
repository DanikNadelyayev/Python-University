from Vehicles import Vehicle

class Tram(Vehicle):
    def __init__(self, type: str, model: str, fuel: str, num_of_passengers: int, route: str) -> None:
        super(Tram, self).__init__(type, model, fuel, num_of_passengers)
        self.route = route

    def __str__(self):
        return super(Tram, self).__str__() \
            + f"Daily route: {self.route}"
