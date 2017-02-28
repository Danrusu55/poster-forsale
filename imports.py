import os
import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import sqlite3
import platform
import logging
import smtplib
import random
from datetime import datetime

if 'Windows' in platform.system():
    imgPath = 'C:\\images\\'
else:
    imgPath = '/Users/danrusu/Dropbox/campaign-images/for_sale_images/'

today = datetime.now().date()
path = os.path.dirname(os.path.abspath(__file__))
logFile = path + '/log.txt'
logging.basicConfig(filename=logFile,level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class MyException(Exception):
    pass
