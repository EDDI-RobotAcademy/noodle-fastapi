from abc import ABC, abstractmethod


class GenerateBacklogService(ABC):
    @abstractmethod
    def requestGenerateBacklogResult(self):
        pass