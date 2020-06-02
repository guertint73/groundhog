import util.constants as Constants
import pandas as pd
from util.errors import Error


def get_covid_by_state_csv(state=None):
    '''
    Get COVID-19 cases by state
    '''

    # capitalize first letter of state
    state = state.title()

    state_df = pd.read_csv(f'src/resources/{Constants.STATES_FILENAME}')

    state_dict = state_df[(state_df.state == state)].to_dict("records")

    if len(state_dict) == 0:
        return Error.NOT_FOUND

    return state_dict


def get_covid_by_county_csv(state, county):
    '''
    Get COVID-19 cases by county
    '''
    county_df = pd.read_csv(f'src/resources/{Constants.COUNTIES_FILENAME}')
    covid_data = county_df[(county_df['state'] == state) & (county_df['county'] == county)].to_dict("records")
    
    if covid_data == []:
        return Error.NOT_FOUND

    return covid_data


def get_total_covid_cases_csv():
    '''
    Get COVID-19 cases in the US
    '''
    pass


def get_state_county_info():
    '''
    Get all counties for every state 
    '''

    # get a list of all states
    county_df = pd.read_csv(f'src/resources/{Constants.COUNTIES_FILENAME}')
    states = list(county_df['state'].unique())

    # get a list of the counties in a state
    counties_by_state = dict()
    for state in states:
        counties = list(county_df[county_df['state'] == state]['county'].unique())
        if counties == ['Unknown']:
            # happens for US territories that don't have counties
            counties_by_state[state] = []
        else:
            counties_by_state[state] = counties

    return counties_by_state

