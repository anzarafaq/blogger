import os
from config import Config

f = file(os.path.expanduser('~/blogger.cfg'))
cfg = Config(f)
