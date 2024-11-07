from conditional_custom_executor_multiple_user_test.repository.conditional_custom_executor_multiple_user_test_repository_impl import \
    ConditionalCustomExecutorMultipleUserTestRepositoryImpl
from conditional_custom_executor_multiple_user_test.service.conditional_custom_executor_multiple_user_test_service import \
    ConditionalCustomExecutorMultipleUserTestService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class ConditionalCustomExecutorMultipleUserTestServiceImpl(ConditionalCustomExecutorMultipleUserTestService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__conditionalCustomExecutorMultipleUserTestRepository = ConditionalCustomExecutorMultipleUserTestRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestToCheckConditionalCustomExecutor(self, conditionalCustomExecutorTestRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()

        ColorPrinter.print_important_message("requestToCheckConditionalCustomExecutor()")

        return await self.__conditionalCustomExecutorMultipleUserTestRepository.checkTestPointIdle(
            userDefinedReceiverFastAPIChannel,
            conditionalCustomExecutorTestRequest.toUserToken()
        )

