def clean_anime_data(raw_anime_list):
    """Normalize and clean raw AniList anime data."""
    cleaned = []

    for anime in raw_anime_list:
        title_romaji = anime.get("title", {}).get("romaji")
        title_english = anime.get("title", {}).get("english")

        cleaned.append({
            "id": anime.get("id"),
            "title": title_english or title_romaji or "Unknown Title",
            "romaji_title": title_romaji or "Unknown",
            "english_title": title_english or "Unknown",
            "cover_image": anime.get("coverImage", {}).get("large") or None,
            "episodes": anime.get("episodes") or None,
            "status": anime.get("status") or "Unknown",
            "site_url": anime.get("siteUrl") or None
        })

    return cleaned
