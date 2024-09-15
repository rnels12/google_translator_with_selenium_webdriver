
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

BROWSER = "firefox"
from selenium import webdriver

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

HOMEPAGE_URL = "https://translate.google.com"

class WebPage(webdriver.Firefox):
  """Class for a translator page"""

  def __init__(self, options=None, teardown=False):
    self.teardown = teardown
    self.translation: str = ''
    self.options = options
    super(WebPage, self).__init__(options=self.options)


  def __exit__(self, exc_type, exc, traceback):
    if self.teardown:
      self.quit()


  def open_home_page(self):
    logger.debug("opening the page...")
    self.get(HOMEPAGE_URL)
    is_cookie_page_displayed = self.find_element(By.TAG_NAME, 'c-wiz').is_displayed()
    if is_cookie_page_displayed:
      self.find_element(By.XPATH,"//button[@aria-label='Accept all']").click()


  def choose_dict_type(self, sl: str, tl: str):
    logger.debug("choosing the dict...")
    self.set_source_lang('English' if sl == '' or not sl else sl)
    self.set_target_lang('German' if tl == '' or not tl else tl)


  def set_source_lang(self, src_lang: str):
    self.find_element(By.XPATH,"//button[@aria-label='More source languages']").click()
    input_field = self.find_element(By.XPATH,"//input[@aria-label='Search languages']")
    self.fillout_input_file(input_field, src_lang)


  def set_target_lang(self, target_lang: str):
    button_lang = self.find_element(By.XPATH,"//button[@aria-label='More target languages']")
    button_lang.click()

    dialog_box = self.find_element(By.CLASS_NAME,"pEyuac.X4hZJc")
    if not dialog_box.is_displayed():
      button_lang.click()

    input_field = dialog_box.find_element(By.CLASS_NAME,"yFQBKb")

    try:
      self.fillout_input_file(input_field, target_lang)
    except:
      logger.debug('setting the target language failed...')


  def fillout_input_file(self, input_field: WebElement, text: str):
    logger.debug(f'entering the input {text}...')
    input_field.send_keys(text)
    input_field.send_keys(Keys.ENTER)


  def enter_words(self, words: str | None = ''):
    logger.debug(f'entering words {words}')
    text_input = self.find_element(By.XPATH,"//textarea[@aria-label='Source text']")
    text_input.send_keys(words)
    text_input.send_keys(Keys.ESCAPE)
    text_output = self.find_element(By.CSS_SELECTOR, "c-wiz.sciAJc div.KkbLmb")

    self.translation = text_output.text

