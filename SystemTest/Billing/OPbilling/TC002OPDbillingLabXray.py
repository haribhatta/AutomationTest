'''
Objective: Happy Path of OPD billing.
The AIM of this test script is to verify below scenarios:
1. Create an OPD invoice of - lab item and xray item.
'''
import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA

AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
labTestTFT = GSV.TFT
radioTestUSG = GSV.USG
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
hospitalNo = LA.patientquickentry(0, 'Cash',department=departmentGynae, doctor=doctorGynae).HospitalNo
print("hospitalNo", hospitalNo)
#oblx.verifyopdinvoice(deposit=0, billamt=500)
LB.createlabxrayinvoice(hospitalNo, labTestTFT, radioTestUSG)
#oblx.verifylabxrayinvoice()
AC.logout()
AC.closeBrowser()
print("Status:Passed -> TC002OPDbillingLabXray.py")
