from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

# radiologist user login
radioUserId = GSV.radioUserID
radioUserPwd = GSV.radioUserPwD

# calling billing item name
usgtest = GSV.USG

GUSGR = A()

GUSGR.openBrowser()
GUSGR.login(foUserId, foUserPwd)
GUSGR.counteractivation()
GUSGR.patientRegistration()
GUSGR.createUSGinvoice(USGtest=usgtest)
GUSGR.logout()
GUSGR.login(radioUserId, radioUserPwd)
GUSGR.doRadioScan()
GUSGR.logout()
GUSGR.closeBrowser()
