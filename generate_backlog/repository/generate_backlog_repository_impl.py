import json
import queue

from generate_backlog.repository.generate_backlog_repository import GenerateBacklogRepository


class GenerateBacklogRepositoryImpl(GenerateBacklogRepository):
    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"OpenaiApiRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"
