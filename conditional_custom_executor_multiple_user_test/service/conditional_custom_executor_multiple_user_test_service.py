from abc import ABC, abstractmethod
from typing import List, Optional


class ConditionalCustomExecutorMultipleUserTestService(ABC):
    @abstractmethod
    def requestToCheckConditionalCustomExecutor(self, conditionalCustomExecutorTestRequest):
        pass

