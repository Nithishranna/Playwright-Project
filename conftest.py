import pytest
from playwright.sync_api import sync_playwright
from pathlib import Path


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       
       page = browser.new_page()
       
       yield page
       
       if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
           screenshot_dir = Path("screenshots")
           screenshot_dir.mkdir(exist_ok=True)
           screenshot_path = screenshot_dir / f"{request.node.name}.png"
           page.screenshot(path=str(screenshot_path))
       browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)    
         
           
        