from config.config import BASE_URL
from utils.logger import get_logger

logger = get_logger()


class GooglePage:

    def __init__(self, page):
        self.page = page

    def open(self):
        logger.info(f"Opening URL: {BASE_URL}")
        self.page.goto(BASE_URL)

    def get_title(self):
        title = self.page.title()
        logger.info(f"Page Title: {title}")
        return title