# Anime Scraper API

A lightweight Python API for fetching all anime in the current season from AniList. Built with FastAPI, this project provides a minimal, open-source solution to access seasonal anime metadata locally.

---

## 🚀 Project Overview

The Anime Scraper API automatically retrieves information about **all anime airing in the current season** from AniList. It’s designed as a **locally runnable MVP** that developers or anime enthusiasts can use to access seasonal anime data without relying on an external service.

---

## ⚙️ Features

- Fetch all anime for the **current season** automatically  
- Structured JSON output containing titles, episodes, genres, and more  
- FastAPI-powered REST API, ready to run locally  
- Minimal setup; works with Python 3.8+  

> Future updates may include additional sources like MyAnimeList, Crunchyroll, or Netflix.

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip

### Steps

1. Clone the repository:

```bash
git clone https://github.com/DavidEmanuelCA/anime-scraper-api.git
cd anime-scraper-api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the API locally:

```bash
uvicorn app.main:app --reload
```

---

## 🧾 Usage

Currently, the API provides **one main endpoint**:

### Get Seasonal Anime

- **Endpoint**: `GET /seasonal`  
- **Description**: Retrieves all anime currently airing this season from AniList.  
- **Example Request**:

```bash
curl http://127.0.0.1:8000/seasonal
```

Example Response (simplified):

[
  {
    "id": 12345,
    "title": "Example Anime",
    "episodes": 12,
    "season": "Fall",
    "year": 2025,
    "genres": ["Action", "Adventure"],
    "status": "RELEASING",
    "description": "A brief synopsis of the anime."
  },
  {
    "id": 67890,
    "title": "Another Anime",
    "episodes": 24,
    "season": "Fall",
    "year": 2025,
    "genres": ["Comedy", "Slice of Life"],
    "status": "RELEASING",
    "description": "Another anime synopsis."
  }
]

Note: The API returns all seasonal anime at once, updated each time the endpoint is called.

---

## 🧪 Testing

To run tests (optional):

```bash
pytest
```

---

## 🤝 Contributing

Contributions are welcome! Ways you can help:

- Add support for more anime sources (MyAnimeList, Crunchyroll, etc.)  
- Improve the data structure or add caching  
- Add unit tests or enhance documentation  

**Steps to contribute:**

1. Fork the repository  
2. Create a new branch (`feature/…` or `fix/…`)  
3. Make your changes and commit with a clear message  
4. Open a pull request for review  

---

## 📄 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

---

## 💡 Notes

- The API currently **does not require an AniList account or API key**.  
- Designed for **local usage**; deploying to a public server may require rate-limiting considerations.  
- Data is retrieved live from AniList and **does not persist** unless caching is implemented.
