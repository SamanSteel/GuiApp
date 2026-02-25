# Third Library
from ldap3 import ALL, Connection, Server
from ldap3.core.exceptions import LDAPBindError

from config.server_config import ldap_settings


def authenticate(user: str, password: str):
    server = Server(ldap_settings.LDAP_SERVER, get_info=ALL)
    user_dn = f"{user}@{ldap_settings.LDAP_DOMAIN}"
    try:
        conn = Connection(server, user=user_dn, password=password, auto_bind=True)
        if not conn.bound:
            return False
    except LDAPBindError:
        return False
    return conn.extend.standard.who_am_i().split("\\")[-1]
