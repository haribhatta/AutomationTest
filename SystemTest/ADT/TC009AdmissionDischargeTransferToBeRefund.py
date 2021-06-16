#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

# admin  user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD

#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
deposit = 1000
admitCharge = GSV.admitRate

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
ADT.billingIP(admitCharge, deposit)
ADT.verifyDuplicateBill()
ADT.logout()
ADT.closeBrowser()

print("There is an existing bug for this test case: EMR-2547")
