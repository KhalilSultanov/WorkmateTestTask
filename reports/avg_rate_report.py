from typing import List
from models.employee import Employee
from reports.base import Report


class AvgRateReport(Report):
    def generate(self, employees: List[Employee]) -> None:
        # TODO here you can implement avg salary per hour for example
        raise NotImplementedError("AvgRateReport is not implemented yet.")
