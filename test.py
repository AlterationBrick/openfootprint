from automobile import GenericEV, GenericICEV
import electricity_source

## Test generic vehicle classes
ev = GenericEV(0.2)
icev = GenericICEV(0.4)
print(ev.calc_total_co2_distance(1000))
print(icev.calc_total_co2_distance(1000))

## Test functionality of yaml retrievage of state info
print(electricity_source.get_emissions_rate_US("mt"))
