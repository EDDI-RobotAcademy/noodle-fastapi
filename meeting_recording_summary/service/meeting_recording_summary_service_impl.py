import os
import sys

from meeting_recording_summary.repository.meeting_recording_summary_repository_impl import \
    MeetingRecordingSummaryRepositoryImpl
from meeting_recording_summary.service.meeting_recording_summary_service import MeetingRecordingSummaryService
from meeting_recording_summary.service.request.meeting_recording_request import MeetingRecordingSummaryRequest
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class MeetingRecordingSummaryServiceImpl(MeetingRecordingSummaryService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__meetingRecordingSummaryRepository = MeetingRecordingSummaryRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestMeetingRecordingSummaryResult(self, meetingRecordingSummaryRequest: MeetingRecordingSummaryRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return await self.__meetingRecordingSummaryRepository.getResult(userDefinedReceiverFastAPIChannel,
                                                               meetingRecordingSummaryRequest.toUserToken())

