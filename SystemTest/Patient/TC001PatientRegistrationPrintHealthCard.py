from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

pr = A()

pr.openBrowser()
pr.login(foUserId, foUserPwd)
pr.counteractivation()
pr.patientRegistration()
#pr.logout()
#pr.closeBrowser()
print("Status:Passed -> TC001 PatientRegistrationPrintHealthCard")

