import pandas as pd


def load_data(debug=False):
    # for this class's purpose
    # in realize this would be a connection to some database
    train_2017 = pd.read_csv('/Users/tianyixia/Downloads/data/train_2017.csv')
    property_2017 = pd.read_csv('/Users/tianyixia/Downloads/data/properties_2017.csv', nrows=1000 if debug else None)
    return train_2017.merge(property_2017, how='inner', on='parcelid')


def get_feature_from_parcelid_and_date(pracel_id, trasnaction_date, data):
    return data[(data['parcelid'] == pracel_id) & (data['transactiondate'] == trasnaction_date)].head(1)