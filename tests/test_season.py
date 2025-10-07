from datetime import date
from app.utils.season import current_season

def test_seasons():
    assert current_season(date(2026, 1, 1)) == (2026, "WINTER")
    assert current_season(date(2026, 4, 30)) == (2026, "SPRING")
    assert current_season(date(2026, 7, 15)) == (2026, "SUMMER")
    assert current_season(date(2026, 10, 31)) == (2026, "FALL")
