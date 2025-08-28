import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    # Database settings
    mongodb_uri: str = os.getenv(
        "MONGODB_URI",
        "mongodb://admin:password123@localhost:27017/runbooks_db?authSource=admin",
    )
    db_name: str = os.getenv("DB_NAME", "runbooks_db")

    # JWT settings
    jwt_secret: str = os.getenv(
        "JWT_SECRET", "your-super-secret-jwt-key-change-in-production"
    )
    access_token_ttl_min: int = int(os.getenv("ACCESS_TOKEN_TTL_MIN", "15"))
    refresh_token_ttl_min: int = int(
        os.getenv("REFRESH_TOKEN_TTL_MIN", "43200")
    )  # 30 days

    # Bootstrap settings
    editor_bootstrap_email: str = os.getenv(
        "EDITOR_BOOTSTRAP_EMAIL", "editor@example.com"
    )
    editor_bootstrap_password: str = os.getenv(
        "EDITOR_BOOTSTRAP_PASSWORD", "password123"
    )

    # API settings
    api_url: str = os.getenv("API_URL", "http://localhost:8000")
    frontend_url: str = os.getenv("FRONTEND_URL", "http://localhost:3000")

    class Config:
        env_file = ".env"


settings = Settings()
