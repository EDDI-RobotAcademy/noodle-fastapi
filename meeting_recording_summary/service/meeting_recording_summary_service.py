from abc import ABC, abstractmethod


class MeetingRecordingSummaryService(ABC):
    @abstractmethod
    def requestMeetingRecordingSummaryResult(self, meetingRecordingSummaryRequest):
        pass