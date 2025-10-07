from fastapi import FastAPI
from app.utils.season import current_season

app = FastAPI(title="Anime Seasonal API")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/seasonal")
async def seasonal():
    year, season = current_season()
    return {"season_year": year, "season": season, "data": []}
