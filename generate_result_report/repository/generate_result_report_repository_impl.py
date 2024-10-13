import json
import queue

from generate_result_report.repository.generate_result_report_repository import GenerateResultReportRepository


class GenerateResultReportRepositoryImpl(GenerateResultReportRepository):
    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"GenerateResultReportRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"
