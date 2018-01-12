from automobile import GenericEV, GenericICEV

ev = GenericEV(0.2)
icev = GenericICEV(0.4)
print(ev.calc_total_co2(1000))
print(icev.calc_total_co2(1000))
