from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
#from webdriver_manager.chrome import ChromeDriverManager
import random
import decimal
import string
import winsound
class LSV:

    # local paths Bug path is added for excelpath so change in local accordingly
    ChromeDriverPath = 'C:/automationTest/AutomationTest/drivers/chromedriver.exe'
    SystemTestPath = 'C:/automationTest/AutomationTest/SystemTest'
    BugsPath = 'C:/automationTest/AutomationTest/SystemTest/HighPriorityBug'
