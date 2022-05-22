import databases

from .config import configurations

if configurations.testing:
    database = databases.Database(configurations.database_test_url, force_rollback=True)
else:
    database = databases.Database(configurations.database_url, min_size=1, max_size=20)
