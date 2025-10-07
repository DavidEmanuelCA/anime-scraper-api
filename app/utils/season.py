from datetime import date
from typing import Optional

def current_season(today: Optional[date] = None) -> dict:
    if today is None:
        today = date.today()

    year = today.year
    month = today.month

    if month in (12, 1, 2):
        season = "Winter"
    elif month in (3, 4, 5):
        season = "Spring"
    elif month in (6, 7, 8):
        season = "Summer"
    else:
        season = "Fall"

    return {
        "season": season,
        "year": year,
        "label": f"{season} {year}",
    }
