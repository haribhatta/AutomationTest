from Library.ApplicationConfiguration import openBrowser, login
import Library.LibModulePatientPortal as LP
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

#openBrowser()
login(foUserId, foUserPwd)
LB.counteractivation()
LP.patientRegistration()
#pr.logout()
#pr.closeBrowser()
print("Status:Passed -> TC001 PatientRegistrationPrintHealthCard")

