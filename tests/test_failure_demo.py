from pages.google_page import GooglePage

def test_failure_demo(page):
    google = GooglePage(page)
    
    google.open()
    
    assert "Facebook" in google.get_title()  # This assertion is intentionally incorrect to demonstrate a test failure