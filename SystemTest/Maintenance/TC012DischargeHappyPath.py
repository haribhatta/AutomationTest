#-------------Objective of this script----------
# To verify successful discharge of already admitted patient.

import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC

import Library.LibModuleBilling as LB
import Library.LibModuleADT as ADT
import Library.LibModuleSettings as LS
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
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
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
LB.counteractivation(EMR)
for x in range(2):
    ADT.admitDisTrans(danpheEMR=EMR, admit=0, discharge=1, trasfer=0, deposit=0, HospitalNo='Auto Test',
                      department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)

AC.logout()
AC.closeBrowser()
print("TC012 DischargeHappyPath: Passed")
