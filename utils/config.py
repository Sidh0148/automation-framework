import json
import os


class Config:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            self.data = json.load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)


# Usage Example:
# from utils.config import config
# url = config.get("base_url")

config = Config()
