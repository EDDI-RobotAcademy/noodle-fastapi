from abc import ABC, abstractmethod


class GenerateResultReportService(ABC):
    @abstractmethod
    def requestGenerateResultReportResult(self, generateResultReportRequest):
        pass