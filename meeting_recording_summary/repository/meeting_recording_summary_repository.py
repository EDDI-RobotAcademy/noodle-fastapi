from abc import ABC, abstractmethod


class MeetingRecordingSummaryRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel, userToken):
        pass