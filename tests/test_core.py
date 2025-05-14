import tempfile
from pathlib import Path

import pytest

from models.employee import Employee
from reader.csv_reader import read_employees
from reports.avg_rate_report import AvgRateReport
from reports.payout_report import PayoutReport
from reports.top_earners_report import TopEarnersReport


def test_read_employees_valid_csv():
    csv_content = (
        "id,email,name,department,hours_worked,salary\n"
        "1,alice@example.com,Alice Johnson,Marketing,160,50\n"
        "2,bob@example.com,Bob Smith,Design,150,40\n"
    )
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
        tmp.write(csv_content)
        tmp_path = Path(tmp.name)

    employees = read_employees(tmp_path)
    assert len(employees) == 2
    assert employees[0].name == "Alice Johnson"
    assert employees[1].hourly_rate == 40

    tmp_path.unlink()


def test_read_employees_invalid_csv():
    csv_content = (
        "id,email,name,department,hours_worked,unknown_rate\n"
        "1,alice@example.com,Alice Johnson,Marketing,160,50\n"
    )
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
        tmp.write(csv_content)
        tmp_path = Path(tmp.name)

    try:
        read_employees(tmp_path)
    except ValueError as e:
        assert "No known hourly rate column" in str(e)
    else:
        assert False, "Expected ValueError for missing rate column"

    tmp_path.unlink()


def test_payout_report_output(capsys):
    employees = [
        Employee(name="Test One", department="Dev", hours_worked=100, hourly_rate=30),
        Employee(name="Test Two", department="Dev", hours_worked=120, hourly_rate=35),
    ]
    report = PayoutReport()
    report.generate(employees)

    captured = capsys.readouterr()
    assert "Test One" in captured.out
    assert "Dev" in captured.out
    assert "$3000" in captured.out
    assert "$4200" in captured.out


def test_avg_rate_report_not_implemented():
    with pytest.raises(NotImplementedError):
        AvgRateReport().generate([])


def test_top_earners_report_not_implemented():
    with pytest.raises(NotImplementedError):
        TopEarnersReport().generate([])


@pytest.mark.parametrize("colname", ["hourly_rate", "rate", "salary"])
def test_read_employees_rate_column_variants(colname):
    csv_content = (
        f"id,email,name,department,hours_worked,{colname}\n"
        f"1,test@example.com,Test User,Dev,160,45\n"
    )
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
        tmp.write(csv_content)
        tmp_path = Path(tmp.name)

    employees = read_employees(tmp_path)
    assert len(employees) == 1
    assert employees[0].hourly_rate == 45

    tmp_path.unlink()


@pytest.mark.parametrize("colname", ["pay", "hour_rate", "amount", "wage"])
def test_read_employees_unsupported_rate_column(colname):
    csv_content = (
        f"id,email,name,department,hours_worked,{colname}\n"
        f"1,test@example.com,Test User,Dev,160,45\n"
    )
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
        tmp.write(csv_content)
        tmp_path = Path(tmp.name)

    with pytest.raises(ValueError, match="No known hourly rate column"):
        read_employees(tmp_path)

    tmp_path.unlink()
