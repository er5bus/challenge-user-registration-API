from fastapi_mail import FastMail, ConnectionConfig

from .config import configurations

conf = ConnectionConfig(
    MAIL_USERNAME = configurations.mail_username,
    MAIL_PASSWORD = configurations.mail_password,
    MAIL_FROM = configurations.mail_from,
    MAIL_PORT = configurations.mail_port,
    MAIL_SERVER = configurations.mail_server,
    MAIL_FROM_NAME= configurations.mail_from_name,
    MAIL_TLS = configurations.mail_tls,
    MAIL_SSL = configurations.mail_ssl,
    USE_CREDENTIALS = configurations.use_credentials,
    VALIDATE_CERTS = configurations.validate_certs
)


fm = FastMail(conf)

fm.config.SUPPRESS_SEND = configurations.suppress_mail_send
