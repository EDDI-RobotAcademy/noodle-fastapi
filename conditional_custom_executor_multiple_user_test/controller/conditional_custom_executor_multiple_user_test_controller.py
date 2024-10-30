from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from conditional_custom_executor_multiple_user_test.controller.request_form.conditional_custom_executor_multiple_user_test_request_form import \
    ConditionalCustomExecutorMultipleUserTestRequestForm
from conditional_custom_executor_multiple_user_test.service.conditional_custom_executor_multiple_user_test_service_impl import \
    ConditionalCustomExecutorMultipleUserTestServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

conditionalCustomExecutorMultipleUserTestRouter = APIRouter()

async def injectConditionalCustomExecutorMultipleUserTestService() -> ConditionalCustomExecutorMultipleUserTestServiceImpl:
    return ConditionalCustomExecutorMultipleUserTestServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@conditionalCustomExecutorMultipleUserTestRouter.post("/check-conditional-custom-executor")
async def requestToCheckMultipleUserTest(conditionalCustomExecutorMultipleUserTestRequestForm: ConditionalCustomExecutorMultipleUserTestRequestForm,
                                         conditionalCustomExecutorMultipleUserTestService: ConditionalCustomExecutorMultipleUserTestServiceImpl =
                                         Depends(injectConditionalCustomExecutorMultipleUserTestService)):

    isIdle = await conditionalCustomExecutorMultipleUserTestService.requestToCheckConditionalCustomExecutor(
        conditionalCustomExecutorMultipleUserTestRequestForm.toUserTestPointRequest())

    return JSONResponse(content={"isIdle": isIdle}, status_code=status.HTTP_200_OK)
