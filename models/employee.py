from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    department: str
    hours_worked: int
    hourly_rate: int
