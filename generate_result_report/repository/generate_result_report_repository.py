from abc import ABC, abstractmethod


class GenerateResultReportRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass