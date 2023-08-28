from src.data_base.db_worker import DBWorker
from src.helpers.consts import (
    POSTGRES_SELECT_FROM_CASES_QUERY,
    POSTGRES_SELECT_FROM_COMPANIES_QUERY,
)


db_worker = DBWorker(
    user="Your user",
    host="localhost",
    port="Your port",
    password="Your password",
    database="Your database",
)

cursor = db_worker.connection.cursor()

cursor.execute(POSTGRES_SELECT_FROM_COMPANIES_QUERY)
for row_index, row in enumerate(cursor.fetchall()):
    print(f"[{row_index}] ---- {row}\n")

cursor.execute(POSTGRES_SELECT_FROM_CASES_QUERY)
for row_index, row in enumerate(cursor.fetchall()):
    print(f"[{row_index}] ---- {row}\n")

db_worker.finish()
