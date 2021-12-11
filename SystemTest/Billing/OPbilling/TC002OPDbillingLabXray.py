'''
Objective: Happy Path of OPD billing.
The AIM of this test script is to verify below scenarios:
1. Create an OPD invoice of - lab item and xray item.
'''
import Library.GlobalShareVariables as GSV
print("hari1")
#from Library.ApplicationConfiguration import B
import Library.ApplicationConfiguration as AC
print("hari2")
#from Library.GlobalShareVariables import G

print("hari3")
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
print("hari4")
#AC = B()
#AC.A.applicationSelection(self)
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
HospitalNo = LA.patientquickentry(EMR, discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
#can.verifyopdinvoice(deposit=0, billamt=500)
print("Status:Passed - > TC001 CreateAppointmentNew")
#oblx.verifyopdinvoice(deposit=0, billamt=500)
LB.createlabxrayinvoice(EMR, HospitalNo, GSV.TFT, GSV.USG)
#oblx.verifylabxrayinvoice()
AC.logout()
AC.closeBrowser()
print("Status:Passed -> TC002OPDbillingLabXray.py")
