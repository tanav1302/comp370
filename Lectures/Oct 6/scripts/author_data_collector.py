import requests
import json
import os.path
import argparse


script_dir = os.path.dirname(__file__)
raw_path = os.path.join(script_dir, '../data/raw')
def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("author")
    args = parse.parse_args()
    author_name = args.author.replace(" ", "%20")

    

    # get the author key
    query_url = f"https://openlibrary.org/search/authors.json?q={author_name}"
    r = requests.get(query_url)

    author = r.json()
    author_key = author['docs'][0]['key']
    print(f"Author Key: {author_key}")



    # query for the books
    books_url = f"https://openlibrary.org/authors/{author_key}/works.json"
    r = requests.get(books_url)

    books_data = r.json()
    # write out the raw data
    fname = f"author_{author_key}_books.json"
    with open(os.path.join(raw_path, fname), "w") as f:
        json.dump(books_data, f, indent=4)

if __name__ == "__main__":
    main()