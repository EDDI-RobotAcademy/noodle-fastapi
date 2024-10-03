from abc import ABC, abstractmethod


class GenerateBacklogRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass