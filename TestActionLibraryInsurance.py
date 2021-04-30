from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
import winsound
class B:

   def verifyIncentivePatientVsServiceReport(self, amount):
       calcIncentive = amount * .60
       calcTDS = calcIncentive * .15
       print("IncentiveAmt", IncentiveAmt)
       print("xIncentiveAmt", xIncentiveAmt)
       print("calcIncentive", calcIncentive)
       assert float(IncentiveAmt) == xIncentiveAmt + calcIncentive   # incentive %
       assert float(TDSAmt) == xTDSAmt + calcTDS         # TDS 15%
       print("xNetPayable", xNetPayable)
       print("NetPayable", NetPayable)
       print("TDSAmt", TDSAmt)
       assert  float(NetPayable) == float(IncentiveAmt) - float(TDSAmt)
       assert float(NetPayable) == xNetPayable + float(calcIncentive) - float(calcTDS) # incentive after deducting TDS

   def wait_for_window(self, timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = self.danpheEMR.window_handles
      wh_then = self.vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

   def __str__(self):
      return

