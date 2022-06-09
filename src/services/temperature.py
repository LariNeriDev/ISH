from typing import Dict, Union

import requests

from src.settings.config import settings


class TemperatureAPI:
    """
    Class to OpenWeatherMaps API, the class brings the temperature from the api,
    passing as a parameter the name of the city or the latitude and longitude
    """

    def __init__(self) -> None:
        self.weather_units = "metric"
        self.weather_url = settings.weather_url
        self.weather_app_id: str = settings.weather_app_id

    def _get_temperature_by_city(self, city: str) -> float:
        params: Dict = {"q": city}
        response_json: Dict = self._request_get(params)
        temperature: float = float(response_json.get("main", {}).get("temp", 30.0))
        return temperature

    def _get_temperature_by_coordinates(self, lat: float, lon: float) -> float:
        params: Dict = {
            "lat": lat,
            "lon": lon,
        }
        response_json: Dict = self._request_get(params)
        temperature: float = float(response_json.get("main", {}).get("temp", 30.0))
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

        if temperature > 30:
            return "party"
        elif temperature >= 15 and temperature < 30:
            return "pop"
        elif temperature >= 10 and temperature <= 14:
            return "rock"
        else:
            return "classical"

    def _request_get(self, params: Dict) -> Dict:

        response_json: Dict = {}

        url: str = (
            f"{self.weather_url}?units={self.weather_units}&appid={self.weather_app_id}"
        )
        response = requests.get(url, params)

        if response.status_code == 200:
            response_json = response.json()

        return response_json
