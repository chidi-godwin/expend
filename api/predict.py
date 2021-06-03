import pandas as pd
from prophet import Prophet


def prepare_data(json_data: str) -> pd.DataFrame:
    df = pd.read_json(json_data, convert_dates=['TransactionDate']).fillna(0)
    df = df.groupby('TransactionDate').sum().resample('W').sum().reset_index()
    df.columns = ['ds', 'y']
    return df


def predict(data: pd.DataFrame, weeks: int = 1) -> dict:
    model = Prophet(weekly_seasonality=True)
    model.fit(data)
    future = model.make_future_dataframe(periods=weeks, freq='W')
    pred = model.predict(future)
    tail = pred[['ds', 'yhat']].tail(weeks)
    tail['ds'] = tail['ds'].dt.strftime('%Y-%m-%d')
    dates = tail.ds.values.tolist()
    predicted_amounts = tail.yhat.values.tolist()
    return {'dates': dates, 'predicted_amounts': predicted_amounts}
