from abc import ABC, abstractmethod
from typing import List, Optional


class ConditionalCustomExecutorMultipleUserTestRepository(ABC):
    @abstractmethod
    async def checkTestPointIdle(self, userDefinedReceiverFastAPIChannel, userToken):
        pass

