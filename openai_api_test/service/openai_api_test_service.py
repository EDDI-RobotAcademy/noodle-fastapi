from abc import ABC, abstractmethod


class OpenAIAPITestService(ABC):
    @abstractmethod
    def requestGenerateBacklogResult(self):
        pass