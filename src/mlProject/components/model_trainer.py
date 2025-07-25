from mlProject import logger
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        model.fit(train_x, train_y)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))

        logger.info("Model training completed")
        logger.info(f"Model is saved at {self.config.root_dir}/{self.config.model_name}")