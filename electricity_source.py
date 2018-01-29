from ruamel.yaml import YAML
import os

# return kg/WH CO2 from energy production
def get_emissions_rate_US(state_abbrev):
    #file e_data_file = open("e_emissions_US.yaml", r)
    #yaml = YAML(typ='safe')
    #e_data = yaml.load(e_data_file)
    #state_datum = e_data[state_abbrev]
    #e_data_file.close()
    #return state_datum / 2.2046 / 1000000
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, 'e_emissions_by_state.yaml'), 'r') as f:
        yaml = YAML(typ='safe')
        e_data = yaml.load(f)
        state_datum = e_data[state_abbrev]
        return state_datum / 2.2046 / 1000000
