import asyncio
import json
import queue

from generate_result_report.repository.generate_result_report_repository import GenerateResultReportRepository
from template.include.socket_server.utility.color_print import ColorPrinter


class GenerateResultReportRepositoryImpl(GenerateResultReportRepository):
    async def getResult(self, userDefinedReceiverFastAPIChannel, userToken):
        print(f"GenerateResultReportRepositoryImpl getResult()")

        temporaryQueueList = []
        result = None

        # userDefinedReceiverFastAPIChannel.put(json.dumps({"userToken": userToken}))

        loop = asyncio.get_event_loop()

        try:
            while True:
                receivedResponseFromSocketClient = await loop.run_in_executor(
                    None, userDefinedReceiverFastAPIChannel.get, False
                )
                data = json.loads(receivedResponseFromSocketClient)

                if data.get("userToken") == userToken:
                    result = data.get("message")
                    break

                temporaryQueueList.append(receivedResponseFromSocketClient)

        except queue.Empty:
            ColorPrinter.print_important_message("아직 데이터를 처리 중이거나 요청한 데이터가 없습니다")
            return result

        for item in temporaryQueueList:
            await loop.run_in_executor(None, userDefinedReceiverFastAPIChannel.put, item)

        return result
