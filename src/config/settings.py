from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env')
    )
    employee_commission:float = 0.1
    marketing_commission:float = 0.2
    manager_commission:float = 0.1
    min_manager_commission:float = 1500
    
    

@lru_cache()
def get_settings():
    return Settings()