from pydantic import BaseModel


class GenerateResultReportRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
