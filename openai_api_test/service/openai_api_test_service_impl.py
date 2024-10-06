import os
import sys

from openai_api_test.repository.openai_api_test_repository_impl import OpenAIAPITestRepositoryImpl
from openai_api_test.service.openai_api_test_service import OpenAIAPITestService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class OpenAIAPITestServiceImpl(OpenAIAPITestService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__generateBacklogRepository = OpenAIAPITestRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def requestGenerateBacklogResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__generateBacklogRepository.getResult(userDefinedReceiverFastAPIChannel)

