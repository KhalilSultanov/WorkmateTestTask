import argparse
from pathlib import Path

from reader.csv_reader import read_employees
from reports.payout_report import PayoutReport
from reports.avg_rate_report import AvgRateReport
from reports.top_earners_report import TopEarnersReport

REPORTS = {
    "payout": PayoutReport,
    "avg_rate": AvgRateReport,
    "top_earners": TopEarnersReport
}


def parse_args():
    parser = argparse.ArgumentParser(description="Payroll Report Generator")
    parser.add_argument("files", nargs="+", help="Paths to CSV files with employee data")
    parser.add_argument("--report", required=True, help="Report type (e.g. payout)")
    return parser.parse_args()


def main():
    args = parse_args()

    report_class = REPORTS.get(args.report)
    if not report_class:
        print(f"Unsupported report type: {args.report}")
        return

    all_employees = []
    for file in args.files:
        path = Path("input_files") / file if not Path(file).exists() else Path(file)
        if not path.exists():
            print(f"File not found: {file}")
            continue
        employees = read_employees(path)
        all_employees.extend(employees)

    report = report_class()
    report.generate(all_employees)


if __name__ == "__main__":
    main()
