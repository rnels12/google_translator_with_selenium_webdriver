from WebPage.web_page import WebPage
from args_parser import ArgsParser
from Mics.logging import activate_logging
from selenium import webdriver


if __name__ == "__main__":
  parser = ArgsParser()
  parser.add_all_args()
  args = parser.parse_args()

  activate_logging(log_level=args.logLevel)

  options = webdriver.FirefoxOptions()
  options.add_argument('--headless')

  with WebPage(options=options, teardown=True) as gdict:
    gdict.implicitly_wait(15)
    gdict.maximize_window()
    gdict.open_home_page()
    gdict.choose_dict_type(sl=args.source , tl=args.target)
    gdict.enter_words(args.words)
    print(gdict.translation)

