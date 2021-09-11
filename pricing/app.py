from flask import Flask
import pickle
from pricing.model import *

from pricing.utils import get_feature_from_parcelid_and_date, load_data



def creat_app():
    app = Flask(__name__)
    app.data = load_data(debug=True)
    app.model = pickle.load(open('/Users/tianyixia/Downloads/mfe_model.pkl', 'rb'))
    return app


app = creat_app()


@app.route('/')
def hello():
    return 'Hello, World! 1+1'


@app.route('/ping')
def ping():
    return 'pong'

# This is REST
@app.route('/ping/<name>')
def ping1(name):
    # look up in the DB ...
    return name


@app.route('/get_logerror/<int:parcel_id>/<date_str>')
def predict_log_error(parcel_id, date_str):

    feature = get_feature_from_parcelid_and_date(parcel_id, date_str, app.data)
    if len(feature) == 0:
        return "bad input data, please check again", 400
    log_error = app.model.predict(feature)

    return {
        "parcel_id": parcel_id,
        "date_str": date_str,
        # "feature": feature.to_dict(),
        "log_error": log_error[0],
    }


if __name__ == '__main__':
    app.run("localhost", port=5000)


