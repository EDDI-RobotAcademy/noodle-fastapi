import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from generate_backlog.service.generate_backlog_service_impl import GenerateBacklogServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))


generateBacklogRouter = APIRouter()

async def injectGenerateBacklogService() -> GenerateBacklogServiceImpl:
    return GenerateBacklogServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@generateBacklogRouter.get('/generate-backlog-result')
async def requestGenerateBacklogResult(generateBacklogService: GenerateBacklogServiceImpl =
                                       Depends(injectGenerateBacklogService)):
    ColorPrinter.print_important_message("requestGenerateBacklogResult()")

    generatedBacklogResult = generateBacklogService.requestGenerateBacklogResult()

    return JSONResponse(content=generatedBacklogResult, status_code=status.HTTP_200_OK)