import os
import re
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from meeting_recording_summary.controller.request_form.meeting_recording_summary_request_form import \
    MeetingRecordingSummaryRequestForm
from meeting_recording_summary.service.meeting_recording_summary_service_impl import MeetingRecordingSummaryServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))


meetingRecordingSummaryRouter = APIRouter()

async def injectMeetingRecordingSummaryService() -> MeetingRecordingSummaryServiceImpl:
    return MeetingRecordingSummaryServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@meetingRecordingSummaryRouter.post('/meeting-recording-summary-result')
async def requestMeetingRecordingSummaryResult(meetingRecordingSummaryRequestForm: MeetingRecordingSummaryRequestForm,
                                            meetingRecordingSummaryService: MeetingRecordingSummaryServiceImpl =
                                            Depends(injectMeetingRecordingSummaryService)):
    ColorPrinter.print_important_message("requestMeetingRecordingSummaryResult()")

    generatedMeetingRecordingSummary = await meetingRecordingSummaryService.requestMeetingRecordingSummaryResult(
        meetingRecordingSummaryRequestForm.toMeetingRecordingSummaryRequest())

    return JSONResponse(content=generatedMeetingRecordingSummary, status_code=status.HTTP_200_OK)
