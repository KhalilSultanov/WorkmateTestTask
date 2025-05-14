from pathlib import Path
from typing import List
from models.employee import Employee

def read_employees(path: Path) -> List[Employee]:
    with path.open(encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    header = lines[0].split(",")
    name_idx = header.index("name")
    dept_idx = header.index("department")
    hours_idx = header.index("hours_worked")

    for possible_rate_name in ["hourly_rate", "rate", "salary"]:
        if possible_rate_name in header:
            rate_idx = header.index(possible_rate_name)
            break
    else:
        raise ValueError(f"No known hourly rate column in file {path.name}")

    employees = []
    for line in lines[1:]:
        cols = line.split(",")
        employees.append(Employee(
            name=cols[name_idx],
            department=cols[dept_idx],
            hours_worked=int(cols[hours_idx]),
            hourly_rate=int(cols[rate_idx]),
        ))
    return employees
