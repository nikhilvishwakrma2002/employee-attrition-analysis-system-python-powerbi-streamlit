import pandas as pd

from utils.load_model import (
    model,
    scaler,
    feature_columns
)

def predict_attrition(input_data):

    input_df = pd.DataFrame([input_data])

    input_df = input_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    scaled_data = scaler.transform(input_df)

    prediction = model.predict(scaled_data)

    probability = model.predict_proba(scaled_data)

    return prediction[0], probability[0]
