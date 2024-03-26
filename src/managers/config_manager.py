from src.infrastructure.interfaces.iconfig_manager import IConfigManager
import json

class ConfigManager(IConfigManager):

    def __init__(self, configPath="config/config.json"):
        self.configPath = configPath


    def read_config(self):
        with open(self.configPath) as f:
            data = json.load(f)

        return data