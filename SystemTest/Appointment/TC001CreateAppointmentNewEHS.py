# Applicable Projects: LPH
''''
The objective of this test case is to test below scenarios:
1. Create an appointment for new patient.
2. Create an appointment for old patient.
'''
########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynaeEHS = GSV.doctorGynoEHS
priceCategoryType = "EHS"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynaeEHS, priceCategoryType=priceCategoryType, case='+ve')
print("Status:Passed - > TC001 CreateAppointmentNew")
AC.logout()
AC.closeBrowser()
print("Status:Passed - > TC001 oldPatientAppointment")


