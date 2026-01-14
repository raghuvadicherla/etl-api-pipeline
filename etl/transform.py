import pandas as pd

def transform(users: pd.DataFrame, posts: pd.DataFrame):
    users_clean = pd.DataFrame({
        "user_id": users["id"],
        "name": users["name"],
        "email": users["email"].str.lower().str.strip(),
        "city": users["address"].apply(lambda x: x["city"])
    })

    posts_clean = posts.rename(columns={
        "id": "post_id",
        "userId": "user_id",
        "title": "post_title",
        "body": "post_body"
    })

    summary = (
        posts_clean.groupby("user_id")
        .agg(total_posts=("post_id", "count"))
        .reset_index()
    )

    return users_clean, posts_clean, summary
