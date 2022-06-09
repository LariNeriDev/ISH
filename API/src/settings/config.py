from pydantic import BaseSettings


class Settings(BaseSettings):
    spotify_client_id: str
    spotify_client_secret: str
    spotify_url: str
    spotify_url_token: str
    weather_url: str
    weather_app_id: str

    class Config:
        env_file = "../.env"


settings = Settings()
