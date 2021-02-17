#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

# admin  user login
admUserId = A.adminUserID
admUserPwd = A.adminUserPwD

#------------Local Veriables-------------------
labitem = "Urine RE/ME"
imagingitem ="USG ABDOMEN & PELVIS"
deposit = 5000

#-------------Script Owner: Hari----------------
#Scripted on: 10.05.2077

ADT = A()
ADT.openBrowser()
#Check application default added items for admitted patient
ADT.login(admUserId, admUserPwd)
ADT.checkAutoAddItems()
ADT.logout()

ADT.login(foUserId, foUserPwd)
ADT.patientRegistration()
ADT.counteractivation()
ADT.createlabxrayinvoice(labitem, imagingitem)
ADT.admitDisTrans(1, 0, 0, deposit)
ADT.billingIP(deposit)
ADT.verifyDuplicateBill()
ADT.logout()
ADT.closeBrowser()

print("There is an existing bug for this test case: EMR-2547")
