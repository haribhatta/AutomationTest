''''
LAB | Duplicate lab requisition is created after billing.

Steps:
1. Navigate to Billing Module
2. Register patient with shortcut key (ALT+N)
3. Add lab item for billing request and print the invoice.
4. Then go to Lab Module -> Sample Collection
5. Duplicate requisition is created for same patient.
6. Verify and view details for Sample collection process.

'''
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
glr.verifySampleCollectionDuplicateEntry()
glr.collectLabSample("sample collected")
glr.checkLabDuplicateRequisition(ItemName=imagingtest)
glr.logout()
glr.closeBrowser()
print("LPH-904 Passed")
