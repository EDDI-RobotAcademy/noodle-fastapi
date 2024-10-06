from abc import ABC, abstractmethod


class OpenAIAPITestRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass