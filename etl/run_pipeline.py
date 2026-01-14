from extract import extract
from transform import transform
from load import load

def main():
    users, posts = extract()
    users_clean, posts_clean, summary = transform(users, posts)
    load(users_clean, posts_clean, summary)
    print("✅ Done! Data saved into warehouse.db")

if __name__ == "__main__":
    main()
