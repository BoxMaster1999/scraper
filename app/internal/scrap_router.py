from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import UploadFile, File, status
from pydantic import BaseModel

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Input(BaseModel):
    url: str


class Output(BaseModel):
    html: str


scrap_router = APIRouter(prefix="/v1")


@scrap_router.post('/scrap',
             description='Scrap endpoint',
             tags=['Process endpoints'],
             status_code=status.HTTP_200_OK,
             response_model=Output)
def process_image(input_: Input) -> Output:
    scraper = Scraper()
    return Output(html=scraper.scrap(input_.url))


class Scraper:

    def __init__(self):
        # configure webdriver
        self.options = Options()
        self.options.headless = True  # hide GUI
        self.options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
        self.options.add_argument("start-maximized")  # ensure window is full-screen

    def scrap(self, url):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)
        driver.get(url)
        html = driver.page_source
        driver.quit()
        return html


