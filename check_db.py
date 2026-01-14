import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///warehouse.db")

print("\n--- dim_users (first 5 rows) ---")
print(pd.read_sql("SELECT * FROM dim_users LIMIT 5", engine))

print("\n--- user_post_summary (first 5 rows) ---")
print(pd.read_sql("SELECT * FROM user_post_summary LIMIT 5", engine))

print("\n--- Join (users + total posts) ---")
query = """
SELECT u.name, u.city, s.total_posts
FROM dim_users u
JOIN user_post_summary s
ON u.user_id = s.user_id
ORDER BY s.total_posts DESC
LIMIT 5;
"""
print(pd.read_sql(query, engine))
