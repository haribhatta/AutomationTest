from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

# radiologist user login
radioUserId = A.radioUserID
radioUserPwd = A.radioUserPwD

GUSGR = A()

labitem = "LDH"
usgtest ="USG (Abdomen / pelvis)"

#GUSGR.applicationSelection()
GUSGR.openBrowser()
GUSGR.login(foUserId, foUserPwd)
GUSGR.counteractivation()
GUSGR.patientRegistration()
GUSGR.createUSGinvoice(usgtest)
GUSGR.logout()
GUSGR.login(radioUserId, radioUserPwd)
GUSGR.generateUSGReport(usgtest)
#GUSGR.logout()
GUSGR.closeBrowser()
