import Bus
import Passenger_car
import Tram
import Trolley
import Truck


def main():
    bus = Bus("Bus", "Bogdan", "Gas", 50, "Lviv - Solonka")
    passenger_car = Passenger_car("Car", "BMW", "Diesel", 5, 3.0)
    tram = Tram("Tram", "Elektron", "Electro", 100, "Vokzal - Pogulyanka")
    trolley = Trolley("Trolley", "Elektron", "Electro", 100, "King-Cross - Centrum")
    truck = Truck("Truck", "MAN", "Diesel", 2, "30000KG")

    print(bus)
    print(passenger_car)
    print(tram)
    print(trolley)
    print(truck)


 if __name__ == '__main__':
    main()
