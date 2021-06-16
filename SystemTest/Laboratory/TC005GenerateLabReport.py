from TestActionLibrary import A
from GlobalShareVariables import GSV
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

# lab user login
labUserId = GSV.labUserID
labUserPwd = GSV.labUserPwD

glr = A()

labitem = GSV.TFT
imagingtest = GSV.USG

glr.openBrowser()
glr.login(foUserId, foUserPwd)
glr.counteractivation()
glr.patientquickentry(0, 'Cash')
glr.createlabxrayinvoice(labitem, imagingtest)
#glr.verifylabxrayinvoice()
glr.logout()

glr.login(labUserId, labUserPwd)
glr.collectLabSample("sample collected")
glr.addLabResult()
#glr.verifyLabReport()
glr.printLabReport("2.23", "15.0", "4.05")
glr.logout()
glr.closeBrowser()