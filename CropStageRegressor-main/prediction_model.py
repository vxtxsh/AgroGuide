import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os
from data_former import new_plant_creator

def train_and_save_model(data_path, model_path):
    
    data = pd.read_excel(data_path)

    features = ['plantheight', 'leafcount']
    target = 'stage'

    X = data[features]
    y = data[target]

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, model_path)
    print(f"Model trained and saved as {model_path}")

if __name__ == "__main__":
    data_path = 'workbooks/example_plant.xlsx'
    model_path = 'predict.joblib'
    
    if not os.path.exists(data_path):
        print(f"Data file {data_path} does not exist. Creating the file...")
        new_plant_creator('example_plant', data_path)
    
    if os.path.exists(data_path):
        train_and_save_model(data_path, model_path)
    else:
        print(f"Failed to create the data file {data_path}.")
