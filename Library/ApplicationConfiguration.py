from selenium import webdriver
import time
from Library.LocalShareVariables import LSV

appName = input("Please enter project/application name:\n"
            "SNCH\n"
            "MMH\n"
            "LPH\n")
ChromePath = LSV.ChromeDriverPath
danpheEMR = webdriver.Chrome(executable_path=ChromePath)

def applicationSelection():
      global appURL
      if appName == "SNCH":
         appURL = "http://202.51.74.168:168/"
      if appName == "MMH":
         appURL = "http://202.51.74.168:170/"
      if appName == "LPH":
         appURL = "http://202.51.74.168:453/"

def openBrowser():
      print(">>Open Browser: START")
      danpheEMR.set_window_position(-2000, 0)
      danpheEMR.maximize_window()
      danpheEMR.get(appURL)
      print("Open Browser: END<<")
def closeBrowser():
      print(">>Close Browser: START")
      danpheEMR.close()
      print("Close Browser: END<<")
def login(userid, pwd):
      print(">>LogIn: START")
      time.sleep(5)
      danpheEMR.find_element_by_id("username_id").send_keys(userid)
      danpheEMR.find_element_by_id("password").send_keys(pwd)
      danpheEMR.find_element_by_id("login").submit()
      print("LogIn: END<<")
def logout():
      print(">>LogOut: START")
      time.sleep(1)
      danpheEMR.find_element_by_css_selector(".dropdown-toggle:nth-child(1) > .fa").click()
      time.sleep(1)
      danpheEMR.find_element_by_link_text("Log Out").click()
      print("LogOut: END<<")
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

