import os.path
import sys
from fastapi.middleware.cors import CORSMiddleware

import colorama

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from ai_to_db_test_point.controller.ai_to_db_test_point_controller import aiToDbTestPointRouter
from conditional_custom_executor_multiple_user_test.controller.conditional_custom_executor_multiple_user_test_controller import \
    conditionalCustomExecutorMultipleUserTestRouter
from generate_backlog.controller.generate_backlog_controller import generateBacklogRouter
from generate_result_report.controller.generate_result_report_controller import generateResultReportRouter
from meeting_recording_summary.controller.meeting_recording_summary_controller import meetingRecordingSummaryRouter
from multiple_user_test_point.controller.multiple_user_test_point_controller import multipleUserTestPointRouter
from user_defined_initializer.init import UserDefinedInitializer

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.deep_learning.controller.deep_learning_controller import deepLearningRouter
from template.dice.controller.dice_controller import diceResultRouter
from template.system_initializer.init import SystemInitializer
from template.task_manager.manager import TaskManager
from template.include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()
SystemInitializer.initSystemDomain()
UserDefinedInitializer.initUserDefinedDomain()

app = FastAPI()

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deepLearningRouter)
app.include_router(diceResultRouter)

app.include_router(multipleUserTestPointRouter)

app.include_router(generateBacklogRouter)
app.include_router(aiToDbTestPointRouter)
app.include_router(generateResultReportRouter)
app.include_router(conditionalCustomExecutorMultipleUserTestRouter)
app.include_router(meetingRecordingSummaryRouter)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
