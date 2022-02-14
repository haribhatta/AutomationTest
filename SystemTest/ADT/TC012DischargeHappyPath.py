#-------------Objective of this script----------
# To verify successful discharge of already admitted patient.

import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC

import Library.LibModuleBilling as LB
import Library.LibModuleADT as ADT

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

#------------Local Veriables-------------------
#labitem = "Urine RE/ME"
#imagingitem ="USG ABDOMEN & PELVIS"
deposit = 0

#-------------Script Owner: Hari----------------
#Scripted on: 12.05.2077

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
for x in range(6):
    ADT.admitDisTrans(danpheEMR=EMR, admit=0, discharge=1, trasfer=0, HospitalNo='Auto Test', deposit=0, doctor=0, department=0)
AC.logout()
AC.closeBrowser()
print("TC012 DischargeHappyPath: Passed")
