import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModulePatientPortal as LPP
########
AC.applicationSelection()
AC.openBrowser()

#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
#############
AC.login(foUserId, foUserPwd)
ContactNo = LPP.patientRegistrationMultipleClick()
LPP.verifyMultipleRegistration(ContactNo)
#LPP.patientRegistrationMultipleClick()
AC.logout()
#pr.logout()
#pr.closeBrowser()


