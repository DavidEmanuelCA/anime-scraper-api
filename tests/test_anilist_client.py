from app.api.anilist_client import fetch_all_current_season_anime

def test_fetch_all_current_season_anime_returns_valid_list():
    results = fetch_all_current_season_anime()
    assert isinstance(results, list)
    assert len(results) > 0  # There should always be anime this season
    first = results[0]
    assert "title" in first and "siteUrl" in first
    assert "romaji" in first["title"]
