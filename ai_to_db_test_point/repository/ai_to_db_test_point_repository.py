from abc import ABC, abstractmethod

class AiToDbTestPointRepository(ABC):
    @abstractmethod
    async def requestAiResult(self, userDefinedReceiverFastAPIChannel, userToken, intermediateData):
        pass