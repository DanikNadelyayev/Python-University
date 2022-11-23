class Vehicle(object):
    def __init__(self, type: str, model: str, fuel: str, num_of_passengers: int) -> None:
        self.type = type
        self.model = model
        self.fuel = fuel
        self.num_of_passengers = num_of_passengers


    def __str__(self):
        return f"Type: {self.type}, Model: {self.model}, Fuel: {self.fuel}, Number of passengers: {self.num_of_passengers}"