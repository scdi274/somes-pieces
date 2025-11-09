from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import pandas as pd
from pydantic import BaseModel

class InputModel(BaseModel):
    data_path: str
    model_out: str
    log_out: str

class OutputModel(BaseModel):
    message: str
    model_file: str
    training_log: str

def evaluate(model_path, test_data_path):
    model = joblib.load(model_path)
    df = pd.read_csv(test_data_path)
    X_test = df.drop(columns=['PVOUT'])
    y_test = df['PVOUT']
    
    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    
    return {"MAE": mae, "R2": r2}