# Third Library
from pydantic_settings import BaseSettings, SettingsConfigDict


class LDAPServer(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    LDAP_SERVER: str
    LDAP_DOMAIN: str
    LDAP_USER: str
    LDAP_PASSWORD: str


ldap_settings = LDAPServer()
