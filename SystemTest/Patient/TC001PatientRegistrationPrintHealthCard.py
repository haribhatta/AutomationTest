from TestActionLibrary import A

pr = A()

pr.openBrowser()
pr.login("billing1", "pass123")
pr.counteractivation()
pr.patientRegistration()
#pr.logout()
#pr.closeBrowser()
print("Status:Passed -> TC001 PatientRegistrationPrintHealthCard")

