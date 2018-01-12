# Base class for all vehicles whose emissions are roughly dependent on distance traveled
class Auto:
    def __init__(self, co2_per_km, embodied):
        self.co2_per_km = co2_per_km
        self.embodied = embodied

    def use(self, km):
        return self.co2_per_km * km
    
    def calc_total_co2(self, km):
        return self.embodied + self.use(km)

# Generic electric vehicle, using average values for this class
class GenericEV(Auto):

    # co2_per_km should be given in kg
    def __init__(self, co2_per_km):
        # kg of CO2-equivalent, from DOI: 10.1111/j.1530-9290.2012.00532.x
        # (taken as average of high and low estimates)
        embodied = 13650
        Auto.__init__(self, co2_per_km, embodied)


# Generic internal combustion vehicle, using average values for the class
class GenericICEV(Auto):

    def __init__(self, co2_per_km):
        # kg of CO2-equivalent, from DOI: 10.1111/j.1530-9290.2012.00532.x
        embodied = 6450
        Auto.__init__(self, co2_per_km, embodied)
