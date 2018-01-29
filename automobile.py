# Base class for all vehicles whose emissions are roughly dependent on distance traveled
class Vehicle:
    def __init__(self, co2_per_km, embodied):
        self.co2_per_km = co2_per_km
        self.embodied = embodied

    def calc_total_co2_distance(self, km):
        return self.embodied + self.co2_per_km * km

    def calc_total_co2_time(self, yrs, km_per_yr):
        return self.embodied + self.co2_per_km * yrs * km_per_yr

# Generic electric vehicle, using average values for this class
class GenericEV(Vehicle):

    # co2_per_km should be given in kg
    def __init__(self, co2_per_km):
        # kg of CO2-equivalent, from DOI: 10.1111/j.1530-9290.2012.00532.x
        # (taken as average of high and low estimates)
        embodied = 13650
        Vehicle.__init__(self, co2_per_km, embodied)


# Generic internal combustion vehicle, using average values for the class
class GenericICEV(Vehicle):

    def __init__(self, co2_per_km):
        # kg of CO2-equivalent, from DOI: 10.1111/j.1530-9290.2012.00532.x
        embodied = 6450
        Vehicle.__init__(self, co2_per_km, embodied)

class EV(Vehicle):

    def __init__(self, location, make, model):
        co2_per_km = model.mwh_per_km * get_emissions(location)
        Vehicle.__init__(sel, co2_per_km, model.embodied)
