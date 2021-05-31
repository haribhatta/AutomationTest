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
class GSV:

   #defining global veriables for login users

   #admin user
   adminUserID = 'admin'
   adminUserPwD = 'pass123'

   #billing user
   foUserID = 'billing'
   foUserPwD = 'pass123'

   #Lab user
   labUserID = 'labs'
   labUserPwD = 'pass123'

   #radiologist user
   radioUserID = 'radio'
   radioUserPwD = 'pass123'

   #pharmacy user
   pharmacyUserID = 'pharmacy'
   pharmacyUserPwD = 'pass123'

   #nurse user
   nurseUserID = 'nurse'
   nurseUserPwD = 'pass123'

   #store user
   storeUserID = 'inventory'
   storeUserPwD = 'pass123'

   # Doctor Name List
   Doctor1 = "Dr. Doctor Doctor"

   # User Name List
   UserBilling = 'Ms. Billing Billing'

   # Bill Items Name variables for LPH Hospital
   '''
   opdRate = 30
   CBC = "CBC"
   TFT = "TFT"
   LDH = "LDH"
   USG = "USG (Abdomen / pelvis)"
   usgRate = 700
   admitRate = 30
   '''

   # Bill Items Name variables for Charak Hospital
   opdRate = 500
   CBC = "CBC"
   TFT = "TFT"
   LDH = "LDH"
   UrineRE = "Urine RE/ME"
   BTCT = "BT/CT"
   btctRate = 200
   USG = "USG (Abdomen / pelvis)"
   usgRate = 1050
   admitRate = 1500

   #Drug name for charak pharmacy billing
   Asthalin = "ASTHALIN ROTACAPS"
   Generic_Asthalin = "SALBUTAMOL"
   asthalinRate = 1.14

   Asthalin2MG = 'ASTHALIN 2 MG TAB'
   asthalin2mgRate = 1.14

   Sinex = "Sinex tab"
   Syringe = "10 ML DIS.SYRINGE"
   syringeRate = 6.49
   Monotrate20MG = 'MONOTRATE-20MG TAB'
   monotrate20mgRate = 4.86
   Testdrug = "testdrugreport"


   #Inventory Item name list
   A4Paper = 'Paper A4'
   PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
   photocopypaperRate = 2300
   Pencil = "PENCIL"

   #Drug name for Lumbini pharmacy billing
   '''
   Asthalin = "ASTHALIN 2 MG TAB"
   Generic_Asthalin = "SALBUTAMOL 2 MG TAB"
   '''

   #def __str__(self):
    #  return