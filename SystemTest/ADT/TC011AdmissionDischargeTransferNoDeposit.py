#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD
# front desk user login
nurseUserId = A.nurseUserID
nurseUserPwd = A.nurseUserPwD

#------------Local Veriables-------------------
labitem = "Urine RE/ME"
imagingitem ="USG ABDOMEN & PELVIS"
deposit = 0

#-------------Script Owner: Hari----------------
#Scripted on: 10.05.2077

ADT = A()

ADT.openBrowser()
ADT.login(foUserId, foUserPwd)
ADT.patientRegistration()
ADT.counteractivation()
ADT.createlabxrayinvoice(labitem, imagingitem)
ADT.logout()

ADT.login(nurseUserId, nurseUserPwd)
ADT.counteractivation()
ADT.admitDisTrans(1, 0, 0, deposit)
ADT.logout()

ADT.login(foUserId, foUserPwd)
ADT.counteractivation()
ADT.billingIP(deposit)
ADT.logout()
ADT.closeBrowser()
