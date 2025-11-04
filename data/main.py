import yaml, os
import polars as pl
from pathlib import Path










if __name__ == "__main__":
    # execute this main.py via "uv run data/main.py" based on the root directory of this project
    with open("data/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    
    # present statistics of train data config["data"]["input_train_data_path"] using polars
    train_data_path = Path(__file__).parents[1] / config["data"]["root_data_path"] / config["data"]["input_train_data_path"]
    df = pl.read_csv(train_data_path)
    print(df.describe())
    print(df.head())