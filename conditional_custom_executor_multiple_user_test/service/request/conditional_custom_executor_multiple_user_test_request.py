from pydantic import BaseModel


class ConditionalCustomExecutorMultipleUserTestRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
