from typing import Union

from fastapi import FastAPI

from src.services.recommendation import TrackRecommendationAPI
from src.services.temperature import TemperatureAPI

app = FastAPI()

api_spotify = TrackRecommendationAPI()
api_weather = TemperatureAPI()

@app.get("/get_music_recommendations/")
def read_item(
    city: Union[str, None] = None,
    lat: Union[str, None] = None,
    lon: Union[str, None] = None,
):
    """Return list of tracks"""

    tracks = []
    suggest_track = api_weather.get_type_of_track_by_temperature(city, lat, lon)
    tracks = api_spotify.search_recommendation(suggest_track)

    return {"tracks": tracks}
