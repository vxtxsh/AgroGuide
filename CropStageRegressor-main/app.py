from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

model = joblib.load('predict.joblib')

data_file = 'example_plant.xlsx'

if not os.path.exists(data_file):
    df = pd.DataFrame({
        'Height': [10.5],
        'Leaf Count': [20],
        'Stage': ['Budding Stage']
    })
    df.to_excel(data_file, index=False)
    print(f"Creating a new file called {data_file}...")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        height = float(request.form['height'])
        leaf_count = int(request.form['leaf_count'])

        temperature = np.random.randint(20, 30)
        humidity = np.random.randint(50, 70)

        prediction = model.predict([[height, leaf_count]])

        stage_mapping = {
            0: 'Budding Stage',
            1: 'Seedling Stage',
            2: 'Vegetative Stage',
            3: 'Flowering Stage',
            4: 'Fruit Development',
            5: 'Ripe Stage'
        }
        predicted_stage = stage_mapping[int(prediction[0])]

        result = {
            'Growth Stage': predicted_stage,
            'Temperature': temperature,
            'Humidity': humidity
        }

        return render_template('result.html', result=result)

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


