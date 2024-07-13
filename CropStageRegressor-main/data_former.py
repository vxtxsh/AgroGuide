import numpy as np
import pandas as pd
import os
import json

def new_plant_creator(name, path):
    print(f"Creating a new file called {name}.xlsx...")
    dataset_creator(name, path)
    print(f"Checking if the file {name}.xlsx exists...")
    if os.path.exists(path):
        print(f"The file {name}.xlsx exists!")
    else:
        print(f"The file {name}.xlsx does not exist!")
    return 0

def dataset_creator(name, path):
    growth_stage = ['Budding Stage', 'Seedling Stage', 'Vegetative Stage',
                    'Flowering Stage', 'Fruit Development', 'Ripe Stage']
    
    predefined_ranges = {
        'temperature_range': {
            'Budding Stage': [20, 25],
            'Seedling Stage': [22, 28],
            'Vegetative Stage': [25, 30],
            'Flowering Stage': [28, 35],
            'Fruit Development': [25, 32],
            'Ripe Stage': [22, 28]
        },
        'humidity_range': {
            'Budding Stage': [50, 60],
            'Seedling Stage': [55, 70],
            'Vegetative Stage': [60, 75],
            'Flowering Stage': [70, 85],
            'Fruit Development': [65, 80],
            'Ripe Stage': [60, 75]
        },
        'light_range': {
            'Budding Stage': [1000, 5000],
            'Seedling Stage': [2000, 8000],
            'Vegetative Stage': [5000, 12000],
            'Flowering Stage': [8000, 15000],
            'Fruit Development': [6000, 12000],
            'Ripe Stage': [5000, 10000]
        },
        'co2_levels': {
            'Budding Stage': [300, 500],
            'Seedling Stage': [400, 600],
            'Vegetative Stage': [500, 800],
            'Flowering Stage': [600, 1000],
            'Fruit Development': [500, 900],
            'Ripe Stage': [400, 700]
        },
        'ec_values': {
            'Budding Stage': [1.0, 1.5],
            'Seedling Stage': [1.2, 1.8],
            'Vegetative Stage': [1.5, 2.0],
            'Flowering Stage': [1.8, 2.5],
            'Fruit Development': [1.5, 2.2],
            'Ripe Stage': [1.2, 1.8]
        },
        'ph_values': {
            'Budding Stage': [5.5, 6.5],
            'Seedling Stage': [6.0, 7.0],
            'Vegetative Stage': [5.8, 6.8],
            'Flowering Stage': [6.0, 7.5],
            'Fruit Development': [6.0, 7.0],
            'Ripe Stage': [5.5, 6.5]
        },
        'plant_height_range': {
            'Budding Stage': [10, 20],
            'Seedling Stage': [20, 30],
            'Vegetative Stage': [30, 60],
            'Flowering Stage': [60, 100],
            'Fruit Development': [40, 80],
            'Ripe Stage': [20, 40]
        },
        'leaf_count_range': {
            'Budding Stage': [5, 10],
            'Seedling Stage': [8, 15],
            'Vegetative Stage': [10, 20],
            'Flowering Stage': [15, 25],
            'Fruit Development': [10, 20],
            'Ripe Stage': [5, 15]
        },
    }

    temperature_range = [predefined_ranges['temperature_range'][stage] for stage in growth_stage]
    humidity_range = [predefined_ranges['humidity_range'][stage] for stage in growth_stage]
    light_range = [predefined_ranges['light_range'][stage] for stage in growth_stage]
    co2_levels = [predefined_ranges['co2_levels'][stage] for stage in growth_stage]
    ec_values = [predefined_ranges['ec_values'][stage] for stage in growth_stage]
    ph_values = [predefined_ranges['ph_values'][stage] for stage in growth_stage]
    plant_height_range = [predefined_ranges['plant_height_range'][stage] for stage in growth_stage]
    leaf_count_range = [predefined_ranges['leaf_count_range'][stage] for stage in growth_stage]

    ranges_data = {
        'temperature_range': temperature_range,
        'humidity_range': humidity_range,
        'light_range': light_range,
        'co2_levels': co2_levels,
        'ec_values': ec_values,
        'ph_values': ph_values,
        'plant_height_range': plant_height_range,
        'leaf_count_range': leaf_count_range
    }

    with open(f'json/{name}.json', 'w') as file:
        json.dump(ranges_data, file)

    data = []

    for i in range(len(growth_stage)):
        temperature = np.random.uniform(temperature_range[i][0], temperature_range[i][1], size=1500)
        humidity = np.random.uniform(humidity_range[i][0], humidity_range[i][1], size=1500)
        light = np.random.uniform(light_range[i][0], light_range[i][1], size=1500)
        co2 = np.random.uniform(co2_levels[i][0], co2_levels[i][1], size=1500)
        ec = np.random.uniform(ec_values[i][0], ec_values[i][1], size=1500)
        pH = np.random.uniform(ph_values[i][0], ph_values[i][1], size=1500)
        plant_height = np.random.uniform(plant_height_range[i][0], plant_height_range[i][1], size=1500)
        leaf_count = np.random.randint(leaf_count_range[i][0], leaf_count_range[i][1]+1, size=1500)
        stage = [growth_stage[i]] * 1500

        stage_data = list(zip(temperature, humidity, light, co2, ec, pH, plant_height, leaf_count, stage))
        data.extend(stage_data)

    df = pd.DataFrame(data, columns=['temperature', 'humidity', 'light',
                                    'co2', 'ec', 'pH', 'plantheight', 'leafcount', 'stage'])
    df = df.sample(frac=1).reset_index(drop=True)
    df.to_excel(path, str(name) + ".xlsx")

if __name__ == '__main__':
    name = 'example_plant'
    path = 'workbooks/example_plant.xlsx'
    new_plant_creator(name, path)

