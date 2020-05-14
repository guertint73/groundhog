import util.constants as Constants
import pandas as pd


def get_covid_states_csv(state=None):
    '''
    Get COVID-19 cases by state
    '''

    state_df = pd.read_csv(f'src/resources/{Constants.STATES_FILENAME}')

    state_dict = state_df[(state_df.state == state)].to_dict("records")

    if state_dict == []:
        return None

    return state_dict


def get_covid_counties_csv():
    '''
    Get COVID-19 cases by county
    '''
    pass


def get_total_covid_cases_csv():
    '''
    Get COVID-19 cases in the US
    '''
    pass
