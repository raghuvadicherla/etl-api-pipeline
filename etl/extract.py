import requests
import pandas as pd

def extract():
    users_url = "https://jsonplaceholder.typicode.com/users"
    posts_url = "https://jsonplaceholder.typicode.com/posts"

    users_response = requests.get(users_url)
    posts_response = requests.get(posts_url)

    users = pd.DataFrame(users_response.json())
    posts = pd.DataFrame(posts_response.json())

    return users, posts
