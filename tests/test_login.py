from pages.login_page import LoginPage
from utils.json_reader import read_json


def test_valid_login(page):
    data = read_json("test_data/login_data.json")
    
    login_page = LoginPage(page)
    
    login_page.open()
    
    login_page.login(
        data["username"],
        data["password"]            
    )
    
    assert "inventory" in page.url