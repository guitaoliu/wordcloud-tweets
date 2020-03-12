import pymysql
from .crawler import tweets

from .config import (
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_PASSWORD,
    MYSQL_USER,
    MYSQL_DB_NAME,
    ENABLE_MYSQL,
)


tweet_text = tweets