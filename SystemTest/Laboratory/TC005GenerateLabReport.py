from TestActionLibrary import A

glr = A()

labitem = "TFT(T3,T4,TSH)"
#imagingtest ="XRAY-3155"
imagingtest = "CHEST APICAL VIEW 10*12 -1F1V"

glr.openBrowser()
glr.login("billing1", "pass123")
glr.counteractivation()
glr.patientquickentry(0, 'Cash')
glr.createlabxrayinvoice(labitem, imagingtest)
glr.verifylabxrayinvoice()
glr.logout()

glr.login("labs", "pass123")
glr.collectLabSample("sample collected")
glr.addLabResult()
glr.printLabReport("2.23", "15.0", "4.05")
glr.logout()
glr.closeBrowser()