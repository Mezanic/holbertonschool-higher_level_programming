#!/usr/bin/python3
"""Script to fetch posts from JSONPlaceholde"""


import csv
import requests


def fetch_and_print_posts():
    """ Function to print title of post in jsonplaceholder """

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Function for structure the data into a list of dictionaries
    and write in a csv files
    """

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        data = [{
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        } for post in posts]

    with open("post.csv", mode="w", newline="") as csvfile:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
