from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

# lab user login
labUserId = A.labUserID
labUserPwd = A.labUserPwD


glr = A()

labitem = "TFT"
#imagingtest ="XRAY-3155"
imagingtest = "CHEST APICAL VIEW 10*12 -1F1V"

#glr.applicationSelection()
glr.openBrowser()
glr.login(foUserId, foUserPwd)
glr.counteractivation()
glr.patientquickentry(0, 'Cash')
glr.createlabxrayinvoice(labitem, imagingtest)
glr.verifylabxrayinvoice()
glr.logout()

glr.login(labUserId, labUserPwd)
glr.collectLabSample("sample collected")
glr.addLabResult()
glr.verifyLabReport()
glr.printLabReport("2.23", "15.0", "4.05")
glr.logout()
glr.closeBrowser()