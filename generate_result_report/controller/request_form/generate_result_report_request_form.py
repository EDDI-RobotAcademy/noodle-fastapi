from pydantic import BaseModel

from generate_result_report.service.service.generate_result_report_request import GenerateResultReportRequest


class GenerateResultReportRequestForm(BaseModel):
    userToken: str

    def toGenerateResultReportRequest(self) -> GenerateResultReportRequest:
        return GenerateResultReportRequest(userToken=self.userToken)
