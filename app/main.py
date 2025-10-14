from fastapi import FastAPI
from app.utils.season import current_season
from app.utils.data_cleaner import clean_anime_data
from app.api.anilist_client import fetch_all_current_season_anime

app = FastAPI(title="Anime Seasonal API")

@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/seasonal")
async def seasonal():
    # Determine current season and year
    season_info = current_season()
    year = season_info["year"]
    season = season_info["season"]

    # Fetch raw data from AniList
    raw_anime = fetch_all_current_season_anime()

    # Clean and normalize the data
    cleaned_data = clean_anime_data(raw_anime)

    # Return structured response
    return {
        "season_year": year,
        "season": season,
        "total": len(cleaned_data),
        "data": cleaned_data
    }
