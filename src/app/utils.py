from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    first_name: str
    last_name: str

def full_name(person: Person) -> str:
    return f"{person.first_name} {person.last_name}"
