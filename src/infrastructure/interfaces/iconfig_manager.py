from abc import ABC, abstractmethod

class IConfigManager(ABC):

    @abstractmethod
    def read_config(self, configPath):
        pass