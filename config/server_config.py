# Third Library
from pydantic_settings import BaseSettings, SettingsConfigDict


class LDAPServer(BaseSettings):
    model_config = SettingsConfigDict()
    LDAP_SERVER: str = "192.168.20.11"
    LDAP_DOMAIN: str = "RAFA-GROUP.com"


ldap_settings = LDAPServer()
