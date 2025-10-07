import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils.season import current_season
from datetime import date

def test_current_season_returns_expected_values():
    assert current_season(date(2026, 1, 1)) == {
        "season": "Winter",
        "year": 2026,
        "label": "Winter 2026"
    }

def test_default_today_runs_without_error():
    result = current_season()
    assert isinstance(result, dict)
    assert "year" in result and "label" in result

def test_current_season_returns_dict():
    assert isinstance(current_season(), dict)
