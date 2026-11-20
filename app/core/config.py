from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # 自动从 .env 或环境变量读取
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # 应用
    APP_NAME: str = "Insurance Agent"
    APP_ENV: str = "dev"
    DEBUG: bool = True

    # 数据库
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = ""
    DB_NAME: str = "insurance"

    # 模型 API（Day05 用）
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = ""

    @property
    def database_url(self) -> str:
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?charset=utf8mb4"
        )


# 单例：整个项目 import 这一个
settings = Settings()





