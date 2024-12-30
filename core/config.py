from pydantic import BaseModel
from typing import Dict
import yaml


class ServiceConfig(BaseModel):
    API_KEY: str

class Config(BaseModel):
    LLM: Dict[str, ServiceConfig]

def load_config(file_path: str) -> Config:
    with open(file_path, 'r') as file:
        config_dict = yaml.safe_load(file)
    return Config(**config_dict)

config = load_config('secrets.yaml')

