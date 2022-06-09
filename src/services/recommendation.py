from typing import Dict, List

import requests

from src.settings.config import settings
from src.utils.base64 import convert_string_base64


class TrackRecommendationAPI:
    """
    Class to Spotify API, According to the temperature requested by the task,
    class returns a specific music style
    """

    def __init__(self) -> None:
        self.client_id = settings.spotify_client_id
        self.client_secret = settings.spotify_client_secret
        self.spotify_token = ""
        self.spotify_url = settings.spotify_url
        self.spotify_url_token = settings.spotify_url_token
        self.spotify_headers: Dict[str, str] = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.spotify_token}",
        }

    def search_recommendation(self, track_type: str) -> List[str]:

        self._spotify_get_token()
        recommendations: List[str] = []

        params: Dict = {
            "q": track_type,
            "type": "track",
            "market": "ES",
            "limit": "10",
            "offset": "10",
        }

        search_data = self._search_spotify_api(params=params)
        items = search_data.get("tracks", {}).get("items", [])
        for item in items:
            recommendations.append(item.get("name"))

        return recommendations

    def _search_spotify_api(self, params: Dict) -> Dict:
        """Get requests to spotify search API"""

        response_json: Dict = {}
        response = requests.get(
            self.spotify_url, headers=self.spotify_headers, params=params
        )
        if response.status_code == 200:
            response_json = response.json()

        return response_json

    def _spotify_get_token(self) -> None:
        """Get New Token from spotify API"""

        response_json: Dict = {}

        token64: str = convert_string_base64(f"{self.client_id}:{self.client_secret}")
        headers: Dict = {"Authorization": f"Basic {token64}"}
        data: Dict = {"grant_type": "client_credentials"}
        response = requests.post(self.spotify_url_token, headers=headers, data=data)
        if response.status_code == 200:
            response_json = response.json()

        self.spotify_token = response_json.get("access_token")

        self.spotify_headers["Authorization"] = f"Bearer {self.spotify_token}"
