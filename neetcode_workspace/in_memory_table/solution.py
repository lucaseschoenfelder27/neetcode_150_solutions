from dataclasses import dataclass, field
from typing import Any, Optional

@dataclass
class Row:
    data: dict[str, Any]

class InMemoryTable:
    
    def __init__(self, name: str, columns: list[str]) -> None:
        self.name = name
        self.columns = columns
        self._rows: list[Row] = []
        
    def insert(self, values: dict[str, Any]) -> None:
        missing = set(self.columns) - set(values)
        if missing:
            raise ValueError(f"Missing columns: {missing}")
        else:
            self._rows.append(Row(data = {c: values[c] for c in self.columns}))
    
    def select(self, condition: Optional[callable] = None) -> list[dict]:
        rows = self._rows
        if condition:
            rows = [row for row in rows if condition(row.data)]
        return [r.data.copy() for r in rows]
    
    #def upate
    
#table = Table()

patients = InMemoryTable("patients", ["id", "name", "age"])
patients.insert({"id": 1, "name": "Alice", "age": 34})
patients.insert({"id": 2, "name": "Bob",   "age": 29})
print(patients.select())
print(patients.select(condition=lambda r: r["age"] > 30))
# create table
# insert
# select
# select where