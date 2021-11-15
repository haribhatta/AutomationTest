from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
def counteractivation():
   print(">>Activate Billing Counter: START")
   time.sleep(8)
   danpheEMR.find_element_by_link_text("Billing").click()
   time.sleep(5)
   danpheEMR.find_element_by_xpath("(//a[contains(@href, '#/Billing/CounterActivate')])[2]").click()
   danpheEMR.find_element_by_css_selector(".col-md-2:nth-child(1) img").click()
   print("Activate Billing Counter: END<<")

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

