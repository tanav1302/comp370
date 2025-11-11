import requests
import json
import os.path

script_dir = os.path.dirname(__file__)
rawpath = os.path.join(script_dir, '..', 'data', 'raw')

def main():
    author_name = r"octavia%20butler" 

    # get the author's key
    query_url = f"https://openlibrary.org/search/authors.json?q={author_name}"
    r = requests.get(query_url)

    auhor_data = r.json()
    author_key = auhor_data['docs'][0]['key']
    print(f"Author Key: {author_key}")

    # query for the books
    books_url = f"https://openlibrary.org/authors/{author_key}/works.json"
    r = requests.get(books_url)
    books_data = r.json()

    # write the the raw data
    fname = f"author_{author_key}_works.json"
    with open(os.path.join(rawpath, fname), 'w') as f:
        json.dump(books_data, f, indent=4)


if __name__ == "__main__":
    main()

