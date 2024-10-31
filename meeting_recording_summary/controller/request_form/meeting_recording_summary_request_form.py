from pydantic import BaseModel

from meeting_recording_summary.service.request.meeting_recording_request import MeetingRecordingSummaryRequest


class MeetingRecordingSummaryRequestForm(BaseModel):
    userToken: str

    def toMeetingRecordingSummaryRequest(self) -> MeetingRecordingSummaryRequest:
        return MeetingRecordingSummaryRequest(userToken=self.userToken)
