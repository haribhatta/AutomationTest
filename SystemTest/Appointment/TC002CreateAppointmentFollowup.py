''''
The objective of this test case is to test below scenarios:
1. Create a followup appointment
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA

#AC.applicationSelection()
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
LA.followUpAppointment(EMR)
AC.logout()
AC.closeBrowser()

