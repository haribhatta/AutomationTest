from TestActionLibrary import A

GUSGR = A()

labitem = "LDH"
imagingtest ="USG ABDOMEN & PELVIS"

GUSGR.openBrowser()
GUSGR.login('billing1', 'pass123')
GUSGR.counteractivation()
GUSGR.patientRegistration()
GUSGR.createlabxrayinvoice(labitem, imagingtest)
GUSGR.logout()
GUSGR.login('radio1', 'pass123')
GUSGR.generateUSGReport(imagingtest)
#GUSGR.logout()
GUSGR.closeBrowser()
