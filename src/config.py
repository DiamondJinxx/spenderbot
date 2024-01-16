from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILES = ("dev.env", "prod.env")

class BotSettings(BaseSettings):
    """Bot config settings"""
    TOKEN: SecretStr

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=ENV_FILES,
        extra="ignore",
    )
    
class DBSettings(BaseSettings):
    """Data base config settings"""
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    NAME: str

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=ENV_FILES,
        env_prefix="DB_",
        extra="ignore",
    )

    @property
    def mongo_uri(self) -> str:
        return f"mongodb://{self.HOST}:{self.PORT}"


bot_config = BotSettings()
db_config = DBSettings()
