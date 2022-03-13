import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePatientPortal as LPP
########

EMR = AC.openBrowser()

#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
#############
AC.login(foUserId, foUserPwd)
ContactNo = LPP.patientRegistrationMultipleClick(EMR)
LPP.verifyMultipleRegistration(EMR, ContactNo)
#LPP.patientRegistrationMultipleClick()
AC.logout()
#pr.logout()
#pr.closeBrowser()


