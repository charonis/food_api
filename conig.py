from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    URL_MAIN_COMPONENT: str
    URL_MAIN_FOOD: str
    
    model_config = SettingsConfigDict(env_file=".env")
      
settings = Settings()