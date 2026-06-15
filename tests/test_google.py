from pages.google_page import GooglePage
from utils.json_reader import read_json


def test_google_title(page):
    test_data = read_json("test_data/google_data.json")

    google = GooglePage(page)

    google.open()

    assert test_data["expected_title"] in google.get_title()