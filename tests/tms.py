from sys import path as sys_path
from os.path import abspath

sys_path.insert(0, abspath("../src"))

from main_service.main import app as main_app
from user_service.main import app as user_app
from auth_service.main import app as auth_app
