from typing import List
from models.employee import Employee
from reports.base import Report
from collections import defaultdict


class PayoutReport(Report):

    def generate(self, employees: List[Employee]) -> None:

        data = defaultdict(list)
        for emp in employees:
            data[emp.department].append(emp)

        print(f"{'':<16}{'name':<20} {'hours':<10} {'rate':<5} {'payout'}")
        for dept, emps in data.items():
            print(f"{dept}")
            total_hours = 0
            total_payout = 0
            for emp in emps:
                payout = emp.hours_worked * emp.hourly_rate
                total_hours += emp.hours_worked
                total_payout += payout
                print(f"{'-' * 15} {emp.name:<20} {emp.hours_worked:<10} {emp.hourly_rate:<5} ${payout:<7}")
            print(f"{'':<37}{total_hours:<10}{'':<7}${total_payout:<10}")
