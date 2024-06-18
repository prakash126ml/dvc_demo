import numpy as np
import pandas as pd

import os

import yaml
import logging

from sklearn.model_selection import train_test_split


# logging configuration
logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

def load_params(params_path: str) -> float:
    test_size = yaml.safe_load(open(params_path, 'r'))['data_ingestion']['test_size']
    return test_size

url = 'https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv'

def read_data(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    return df

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df.drop(columns=['tweet_id'],inplace=True)

    final_df = df[df['sentiment'].isin(['neutral','sadness'])]

    final_df['sentiment'].replace({'neutral':1, 'sadness':0},inplace=True)

    return final_df


def save_data(data_path: str, train_data: str, test_data: str) -> None:
    
    os.makedirs(data_path)

    train_data.to_csv(os.path.join(data_path,"train.csv"))
    test_data.to_csv(os.path.join(data_path,"test.csv"))


def main():
    logger.debug('main file called!!')
    test_size = load_params('params.yaml')
    df = read_data(url)
    final_df = process_data(df)

    train_data, test_data = train_test_split(final_df, test_size=test_size, random_state=42)
    
    data_path = os.path.join("data","raw")
    save_data(data_path, train_data, test_data)

if __name__ == "__main__":
    main()






# dvc stage add -n data_preprocessing -d src/data_preprocesing.py -d data/raw -o data/processed python src/data_preprocesing.py
# dvc stage add -n feature_engineering -d src/feature_engineering.py -d data/processed -o data/features python src/feature_engineering.py