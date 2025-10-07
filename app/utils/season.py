from datetime import date
from typing import Tuple

def current_season(today: date = None) -> Tuple[int, str]:
    """Return (year, SEASON) where SEASON in {'WINTER','SPRING','SUMMER','FALL'}."""
    if today is None:
        today = date.today()
    m = today.month
    if m in (1, 2, 3):
        return today.year, "WINTER"
    if m in (4, 5, 6):
        return today.year, "SPRING"
    if m in (7, 8, 9):
        return today.year, "SUMMER"
    return today.year, "FALL"
