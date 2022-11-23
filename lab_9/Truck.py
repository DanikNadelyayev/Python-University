from Vehicles import Vehicle

class Truck(Vehicle):
    def __init__(self, type: str, model: str, fuel: str, num_of_passengers: int, max_weight: str) -> None:
        super(Truck, self).__init__(type, model, fuel, num_of_passengers)
        self.max_weight = max_weight

    def __str__(self):
        return super(Truck, self).__str__() \
            + f"Max weight that can bring: {self.max_weight}"
