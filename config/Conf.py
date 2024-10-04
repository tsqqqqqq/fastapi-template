from pydantic import computed_field, MySQLDsn
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_host: str
    app_port: int
    admin_email: str
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    log_path: str
    log_file_name: str
    log_level: str = "INFO"

    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_database: str

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> MySQLDsn:
        print(self.db_database)
        return MultiHostUrl.build(
            scheme="mysql+pymysql",
            host=self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_password,
            path=self.db_database,
        )
