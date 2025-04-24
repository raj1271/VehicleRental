class Vehicle:
    def __init__(self, brand, model, year, price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
    
    def display_details(self):
        return f"{self.year} {self.brand} {self.model}, Price per day: Rs{self.price_per_day}"

class Car(Vehicle):
    def __init__(self, brand, model, year, price_per_day, fuel_type, seating_capacity):
        super().__init__(brand, model, year, price_per_day)
        self.fuel_type = fuel_type
        self.seating_capacity = seating_capacity
    
    def display_details(self):
        return super().display_details() + f", Fuel Type: {self.fuel_type}, Seating Capacity: {self.seating_capacity}"

class Bike(Vehicle):
    def __init__(self, brand, model, year, price_per_day, engine_capacity, bike_type):
        super().__init__(brand, model, year, price_per_day)
        self.engine_capacity = engine_capacity
        self.bike_type = bike_type
    
    def display_details(self):
        return super().display_details() + f", Engine Capacity: {self.engine_capacity}cc, Type: {self.bike_type}"

class Truck(Vehicle):
    def __init__(self, brand, model, year, price_per_day, load_capacity):
        super().__init__(brand, model, year, price_per_day)
        self.load_capacity = load_capacity
    
    def display_details(self):
        return super().display_details() + f", Load Capacity: {self.load_capacity} tons"

class Bus(Vehicle):
    def __init__(self, brand, model, year, price_per_day, passenger_capacity):
        super().__init__(brand, model, year, price_per_day)
        self.passenger_capacity = passenger_capacity
    
    def display_details(self):
        return super().display_details() + f", Passenger Capacity: {self.passenger_capacity}"

# Creating instances
cars = [
    Car("Maruti Suzuki", "Swift", 2022, 3000, "Petrol", 5),
    Car("Hyundai", "Creta", 2023, 4000, "Diesel", 5),
    Car("Tata", "Harrier", 2024, 5000, "Diesel", 7),
    Car("Mahindra", "XUV700", 2023, 5500, "Petrol", 7),
    Car("Honda", "City", 2022, 3500, "Hybrid", 5)
]

bikes = [
    Bike("Bajaj", "Pulsar 220F", 2021, 800, 220, "Sport"),
    Bike("Royal Enfield", "Himalayan", 2022, 1000, 411, "Adventure"),
    Bike("TVS", "Apache RTR 160", 2023, 600, 160, "Sport"),
    Bike("Hero", "Splendor Plus", 2021, 400, 100, "Commuter"),
    Bike("KTM", "Duke 390", 2022, 1200, 373, "Sport")
]

trucks = [
    Truck("Tata", "Prima 4928", 2020, 7000, 28),
    Truck("Ashok Leyland", "Boss 1920", 2021, 7500, 20),
    Truck("Eicher", "Pro 3015", 2022, 6000, 15),
    Truck("Mahindra", "Blazo X 35", 2023, 8500, 35),
    Truck("BharatBenz", "2823R", 2022, 9000, 30)
]

buses = [
    Bus("Tata", "Starbus Ultra", 2019, 5000, 35),
    Bus("Ashok Leyland", "Viking", 2020, 6000, 40),
    Bus("Eicher", "Skyline Pro", 2021, 6500, 45),
    Bus("Volvo", "9400 B8R", 2022, 10000, 50),
    Bus("SML Isuzu", "Executive LX", 2023, 5500, 30)
]



print('Hello,')
a=input('Which type of Vehical you Want \n [CAR🚗 , BIKE🏍️  , TRUCK🚚 , BUS🚌 ]\n ===>  ')
ans=a.lower()
if ans=='car':
    print('...GOOD CHOISE...')
    print('*-*-*-CAR-*-*-* \nA comfortable and fuel-efficient ride, perfect for city and highway travel...\n\n')
    for vehicle_list in [cars]:
        for vehicle in vehicle_list:
            print(vehicle.display_details())
        print('🚗...🚗...🚗...🚗...🚗...🚗...🚗...🚗...🚗...🚗')
elif ans=='bike':
    print('...GOOD CHOISE...')
    print('*-*-*-BICK-*-*-* \nA swift and economical two-wheeler, ideal for daily commuting...\n\n')
    for vehicle_list in [bikes]:
        for vehicle in vehicle_list:
            print(vehicle.display_details())
        print('🏍️....🏍️....🏍️....🏍️....🏍️....🏍️....🏍️....🏍️....🏍️....🏍️')
elif ans=='truck':
    print('...GOOD CHOISE...')
    print('*-*-*-TRUCK-*-*-* \nA heavy-duty vehicle designed for transporting goods over long distances...\n\n')
    for vehicle_list in [trucks]:
        for vehicle in vehicle_list:
            print(vehicle.display_details())
        print('🚚....🚚....🚚....🚚....🚚....🚚....🚚....🚚....🚚....🚚')
elif ans=='bus':
    print('...GOOD CHOISE...')
    print('*-*-*-BUS-*-*-* \nA spacious and reliable transport solution for group travel and public transport...\n\n')
    for vehicle_list in [buses]:
        for vehicle in vehicle_list:
            print(vehicle.display_details())
        print('🚌....🚌....🚌....🚌....🚌....🚌....🚌....🚌....🚌....🚌')
else:
    print('pleas enter given type')
