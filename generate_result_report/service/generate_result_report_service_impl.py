import os
import sys

from generate_result_report.repository.generate_result_report_repository_impl import GenerateResultReportRepositoryImpl
from generate_result_report.service.generate_result_report_service import GenerateResultReportService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class GenerateResultReportServiceImpl(GenerateResultReportService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__generateResultReportRepository = GenerateResultReportRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def requestGenerateResultReportResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__generateResultReportRepository.getResult(userDefinedReceiverFastAPIChannel)

