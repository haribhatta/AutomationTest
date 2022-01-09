''''
The objective of this test case is to test below scenarios:
1. Create an appointment for new patient.
2. Create an appointment for old patient.
'''
########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleVaccination as LV
EMR = AC.openBrowser()
#############
# front desk user login
vaccineUserId = GSV.vaccineUserID
vaccineUserPwd = GSV.vaccineUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
#############
AC.login(vaccineUserId, vaccineUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
LV.VaccinationPatientRegistration(EMR)
LV.verifyVaccinationPatientRegistration(EMR)
AC.logout()
AC.closeBrowser()
print("Status:Passed - > TC001 oldPatientAppointment")


