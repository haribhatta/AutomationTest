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
   labUserID = 'lab'
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
   #Doctor1 = "Dr. Doctor Doctor"

   # User Name List
   UserBilling = 'Billing Billing'

   # Bill Items Name variables for LPH Hospital
   #'''
   opdRate = 30
   CBC = "CBC"
   TFT = "TFT"
   TFTRate = 800
   LDH = "LDH"
   USG = "USG ABDOMEN/PELVIS"
   usgRate = 700
   admitRate = 30
   UrineRE = "URINE R/E"
   BTCT = "BT/CT"
   btctRate = 100
   
   #Drug name
   drug1BrandName = 'ASTHALIN 2 MG TAB'
   drug1GenericName = 'SALBUTAMOL 2 MG TAB'
   drug1Rate = 2.1

   drug2BrandName = "MACLAR 500MG TAB"
   drug2GenericName = "CLARITHROMYCIN"
   drug2Rate = 563.5

   drug3BrandName = "Sinex tab"

   drug4BrandName = "10 ML DIS.SYRINGE"
   drug4BrandRate = 6.49

   drug5BrandName = 'MONOTRATE-20MG TAB'
   drug5BrandRate = 4.86

   Testdrug = "testdrugreport"

   #Inventory Item name list
   Inventory1 = "General Inventory"
   Dispensary1 = "MainDispensary"
   A4Paper = 'Paper A4'
   PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
   photocopypaperRate = 2300
   stationaryItem1 = "DOTPEN"

   #Sub Store Name list
   SubStore1 = "General"
   SubStore2 = "PostOps"

   #Doctor/Department List
   doctor1 = "Dr. doctor doctor"
   department1 = "Medicine"

   # User Name List
   UserBilling = 'Mr. Bhagawati Pandey'

   deposit = 100
   #'''

   '''
   # Bill Items Name variables for Charak Hospital
   opdRate = 500
   CBC = "CBC"
   TFT = "TFT"   #TFT(FT3,FT4,TSH) CLLEA
   TFTRate = 1100
   LDH = "LDH"
   #UrineRE = "Urine RE/ME"
   UrineRE = "URINE R/E,M/E" # this gets changed on V1.49.3
   BTCT = "BT/CT"
   btctRate = 200
   USG = "USG (Abdomen / pelvis)"
   usgRate = 1050
   admitRate = 1500

   #Drug name for charak pharmacy billing
   drug1BrandName = "SINEX TAB"
   drug1GenericName = "quinapril"
   drug1Rate = 1.15

   drug2BrandName = 'ASTHALIN 2 MG TAB'
   drug2BrandRate = 1.14

   drug3BrandName = "Sinex tab"

   drug4BrandName = "10 ML DIS.SYRINGE"
   drug4BrandRate = 6.49

   drug5BrandName = 'MONOTRATE-20MG TAB'
   drug5BrandRate = 4.86

   Testdrug = "Testdrugreport"

   #Inventory Item name list
   Inventory1 = "General Inventory"
   Dispensary1 = "General Inventory"

   A4Paper = 'Paper A4'
   PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
   photocopypaperRate = 2300
   stationaryItem1 = "PENCIL"
   
   #Sub Store Name list
   SubStore1 = "General"
   SubStore2 = "PostOps"

   #Doctor/Department List
   doctor1 = "Dr. doctor doctor"
   department1 = "Medicine"
   
   # User Name List
   UserBilling = 'Billing Billing'
   
   deposit = 200
'''

   #def __str__(self):
    #  return