import os
from taalbot import Taalbot


if __name__ == '__main__':
    token = os.environ['TOKEN']
    taalbot = Taalbot()
    taalbot.run(token)
