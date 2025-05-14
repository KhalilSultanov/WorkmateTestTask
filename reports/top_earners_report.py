from typing import List

from models.employee import Employee
from reports.base import Report


class TopEarnersReport(Report):
    def generate(self, employees: List[Employee]) -> None:
        # TODO here you can implement top employee by salary report
        raise NotImplementedError("TopEarnersReport is not implemented yet.")
