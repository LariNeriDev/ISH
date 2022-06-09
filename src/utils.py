"""Utils Modules"""

import requests
import base64
import json
from typing import Union, List, Dict


class TemperatureAPI:
    """
    Class to OpenWeatherMaps API, the class brings the temperature from the api,
    passing as a parameter the name of the city or the latitude and longitude
    """

    def __init__(self) -> None:
        self.weather_units = 'metric'
        self.weather_url = 'http://api.openweathermap.org/data/2.5/weather'
        self.weather_app_id: str = 'b77e07f479efe92156376a8b07640ced'

    def _get_temperature_by_city(self, city: str) -> float:
        params: Dict = {
            'q': city
        }
        response_json: Dict = self._request_get(params)
        temperature: float = float(response_json.get('main', {}).get('temp', 30.0))
        return temperature

    def _get_temperature_by_coordinates(self, lat: float, lon: float) -> float:
        params: Dict = {
            'lat': lat,
            'lon': lon,
        }
        response_json: Dict = self._request_get(params)
        temperature: float = float(response_json.get('main', {}).get('temp', 30.0))
        return temperature

    def get_type_of_track_by_temperature(
        self,
        city: Union[str, None] = None,
        lat: Union[float, None] = None,
        lon: Union[float, None] = None,
    ) -> str:
        temperature: float = 30.0
        
        if city:
            temperature = self._get_temperature_by_city(city)
        elif lat and lon:
            temperature = self._get_temperature_by_coordinates(lat, lon)

        if temperature <= 30:
            return 'party'
        elif temperature <= 15 and temperature > 30:
            return 'pop'
        elif temperature < 10 and temperature >= 14:
            return 'rock'
        else:
            return 'classical'

    def _request_get(self, params: Dict) -> Dict:

        response_json: Dict = {}

        url: str = f'{self.weather_url}?units={self.weather_units}&appid={self.weather_app_id}'
        response = requests.get(url, params)

        if response.status_code == 200:
            response_json = response.json()

        return response_json

class TrackRecommendationAPI:
    """
    Class to Spotify API, According to the temperature requested by the task,
    class returns a specific music style
    """

    def __init__(self) -> None:
        self.client_id = 'b348ab6945ce439c86d951313c6af5b6'
        self.client_secret = '1d9e09fc2e524c58b735b1d457476b5c'
        self.spotify_token = ""
        self.spotify_url = 'https://api.spotify.com/v1/search'
        self.spotify_url_token = 'https://accounts.spotify.com/api/token'
        self.spotify_headers: Dict[str, str] = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.spotify_token}',
        }

    def search_recommendation(self, track_type: str) -> List[str]:

        self._spotify_get_token()
        recommendations: List[str] = []
       
        params: Dict = {
            'q': track_type,
            'type': 'track',
            'market': 'ES',
            'limit': '10',
            'offset': '10',
        }
        
        search_data = self._search_spotify_api(params=params)
        items = search_data.get('tracks', {}).get('items', [])
        for item in items:
            recommendations.append(item.get('name'))

        return recommendations

    def _search_spotify_api(self, params: Dict) -> Dict:
        """Get requests to spotify search API"""

        response_json: Dict = {}
        response = requests.get(self.spotify_url, headers=self.spotify_headers, params=params)
        if response.status_code == 200:
            response_json = response.json()

        return response_json
    
    def _spotify_get_token(self)-> None:
        """Get New Token from spotify API"""
        
        response_json: Dict = {}
        
        token64: str = convert_string_base64(f"{self.client_id}:{self.client_secret}")
        headers: Dict = {
            'Authorization': f'Basic {token64}'
        }
        data: Dict = {
            'grant_type': 'client_credentials'
        }
        response = requests.post(self.spotify_url_token, headers=headers, data=data)
        if response.status_code == 200:
            response_json = response.json()

        self.spotify_token = response_json.get("access_token")

        self.spotify_headers['Authorization'] = f'Bearer {self.spotify_token}'


def convert_string_base64(value: str) -> str:
    """Convert string to base64"""

    value64Encode= value.encode('ascii')
    base64Bytes = base64.b64encode(value64Encode)
    base64Decode = base64Bytes.decode('ascii')
    return base64Decode
