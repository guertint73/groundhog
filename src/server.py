from flask import Flask, Response
import json
import services.csv_service as CSVService
from util.errors import Error

'''Flask Setup'''
app = Flask(__name__)


@app.route('/groundhog/v1/state/<state>')
def get_covid_data_by_state(state):
    states_json = CSVService.get_covid_states_csv(state=state)

    if states_json is Error.NOT_FOUND:
        err_msg = {
            'error': 'Resource not found',
            'resource': state
        }
        response = Response(response=json.dumps(err_msg),
                            status=404,
                            mimetype='application/json')

    else:
        response = Response(response=json.dumps(states_json),
                            status=200,
                            mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
