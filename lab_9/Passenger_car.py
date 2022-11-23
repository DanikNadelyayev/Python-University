from Vehicles import Vehicle


class Passenger_car(Vehicle):
    def __init__(self, type, model, fuel, num_of_passengers, engine: float):
        super(Passenger_car, self).__init__(
            type, model, fuel, num_of_passengers)
        self.engine = engine

    def __str__(self):
        return super(Passenger_car, self).__str__() \
            + f"Engine: {self.engine}"
