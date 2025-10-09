import requests
from app.utils.season import current_season

ANILIST_API_URL = "https://graphql.anilist.co"

def fetch_all_current_season_anime():
    """Fetch all anime for the current season from AniList."""
    season_info = current_season()
    year = season_info["year"]
    season = season_info["season"].upper()

    query = """
    query ($season: MediaSeason, $seasonYear: Int, $page: Int, $perPage: Int) {
      Page(page: $page, perPage: $perPage) {
        pageInfo {
          currentPage
          hasNextPage
        }
        media(season: $season, seasonYear: $seasonYear, type: ANIME, sort: START_DATE_DESC) {
          id
          title {
            romaji
            english
          }
          coverImage {
            large
          }
          episodes
          status
          siteUrl
        }
      }
    }
    """

    results = []
    page = 1

    while True:
        variables = {"season": season, "seasonYear": year, "page": page, "perPage": 50}
        response = requests.post(ANILIST_API_URL, json={"query": query, "variables": variables})
        response.raise_for_status()
        data = response.json()["data"]["Page"]

        results.extend(data["media"])

        if not data["pageInfo"]["hasNextPage"]:
            break
        page += 1

    return results
