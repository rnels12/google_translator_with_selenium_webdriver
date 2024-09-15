import argparse

class ArgsParser(argparse.ArgumentParser):
  def __init__(self) -> None:
    super(ArgsParser, self).__init__()

  def add_all_args(self) -> None:
    self.add_argument("--source", help="set source language")
    self.add_argument("--target", help="set target language")
    self.add_argument("--logLevel", help="set logging level")
    self.add_argument("--words", help="entered words")
