from pydantic import BaseModel


class MeetingRecordingSummaryRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
