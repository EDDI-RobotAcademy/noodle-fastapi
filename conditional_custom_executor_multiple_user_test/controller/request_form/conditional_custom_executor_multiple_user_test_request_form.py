from pydantic import BaseModel

from conditional_custom_executor_multiple_user_test.service.request.conditional_custom_executor_multiple_user_test_request import \
    ConditionalCustomExecutorMultipleUserTestRequest


class ConditionalCustomExecutorMultipleUserTestRequestForm(BaseModel):
    userToken: str

    def toUserTestPointRequest(self) -> ConditionalCustomExecutorMultipleUserTestRequest:
        return ConditionalCustomExecutorMultipleUserTestRequest(userToken=self.userToken)
