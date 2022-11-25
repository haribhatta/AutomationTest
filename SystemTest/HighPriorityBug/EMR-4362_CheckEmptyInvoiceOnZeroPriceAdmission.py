#-------------Objective of this script----------
''' Scripted By: Hari P. Bhatta
Headline:
Billing>IP: Empty invoice is generating during admission (when admission charge is null).
Description:
Test Data:      URL: http://202.51.74.168:170/      Version: MMH_V2.1.7

Scenario: Do admission and check duplicate invoice.

Issue: Even there is no admission charge in MMH but empty invoice is getting generated.
Solution:
Restrict save admission if no billing item is there.

'''
from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
from Library import LibModulePatientPortal as LPP
from Library import LibModuleADT as ADT
from Library import LibModuleAppointment as LA
from Library import GlobalShareVariables as GSV
import Library.LibModuleSettings as LS

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# admin  user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
###
doctor = GSV.doctorGyno
department = GSV.departmentGyno

#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
deposit = 1000
admitCharge = GSV.admitRate

#-------------Script Owner: Hari----------------
#Scripted on: 10.05.2077

EMR = AC.openBrowser()
#Check application default added items for admitted patient
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
LS.checkAutoAddItems(danpheEMR=EMR)
AC.logout()
AC.login(foUserId, foUserPwd)
HospitalNo = LPP.patientRegistration(danpheEMR=EMR)
LB.counteractivation(danpheEMR=EMR)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, transfer=0, deposit=deposit, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
#AC.logout()
#AC.closeBrowser()