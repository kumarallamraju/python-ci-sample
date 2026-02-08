from app.utils import Person, full_name

def test_full_name():
    p = Person("Kumar", "Allamraju")
    assert full_name(p) == "Kumar Allamraju"
