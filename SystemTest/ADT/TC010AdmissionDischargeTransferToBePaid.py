#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
deposit = 1000

#-------------Script Owner: Hari----------------
#Scripted on: 10.05.2077

ADT = A()

ADT.openBrowser()
ADT.login(foUserId, foUserPwd)
ADT.patientRegistration()
ADT.counteractivation()
ADT.createlabxrayinvoice(labitem, imagingitem)
ADT.admitDisTrans(1, 0, 0, deposit)
ADT.billingIP(deposit)
ADT.logout()
ADT.closeBrowser()