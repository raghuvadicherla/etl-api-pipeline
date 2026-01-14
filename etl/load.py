from sqlalchemy import create_engine, text

def load(users_clean, posts_clean, summary):
    engine = create_engine("sqlite:///warehouse.db")

    with engine.begin() as conn:
        # Create tables first time (if not exists)
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS dim_users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            city TEXT
        );
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS fact_posts (
            post_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            post_title TEXT,
            post_body TEXT
        );
        """))

    # Incremental insert for dim_users (avoid duplicates by primary key)
    existing_users = set()
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT user_id FROM dim_users")).fetchall()
        existing_users = {r[0] for r in rows}

    new_users = users_clean[~users_clean["user_id"].isin(existing_users)]
    if not new_users.empty:
        new_users.to_sql("dim_users", engine, if_exists="append", index=False)

    # Incremental insert for fact_posts
    existing_posts = set()
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT post_id FROM fact_posts")).fetchall()
        existing_posts = {r[0] for r in rows}

    new_posts = posts_clean[~posts_clean["post_id"].isin(existing_posts)]
    if not new_posts.empty:
        new_posts.to_sql("fact_posts", engine, if_exists="append", index=False)

    # Summary table is derived → safe to replace each run
    summary.to_sql("user_post_summary", engine, if_exists="replace", index=False)
