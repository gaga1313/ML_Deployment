import os
import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_cols = [col.replace(" ", "_") for col in all_cols]

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Pandas column validation status: {validation_status}")
                    break
                
                
                if self.config.all_schema.get(col) != data[col.replace("_", " ")].dtype:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"All schema validation status: {validation_status}")
                    break     

            if validation_status:
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Complete Validation status: {validation_status}")
        
            return validation_status
        
        except Exception as e:
            raise e

