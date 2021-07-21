#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
nurseUserId = GSV.nurseUserID
nurseUserPwd = GSV.nurseUserPwD

#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
deposit = 0
admitcharge = GSV.admitRate
doctor = GSV.doctor1
department = GSV.department1

#-------------Script Owner: Hari----------------
#Scripted on: 10.05.2077

ADT = A()

ADT.openBrowser()
ADT.login(foUserId, foUserPwd)
ADT.patientRegistration()
ADT.counteractivation()
ADT.createlabxrayinvoice(labitem, imagingitem)
#ADT.logout()

#ADT.login(nurseUserId, nurseUserPwd)
#ADT.counteractivation()
ADT.admitDisTrans(1, 0, 0, deposit, doctor=doctor, department=department)
#ADT.logout()

#ADT.login(foUserId, foUserPwd)
#ADT.counteractivation()
ADT.billingIP(admitcharge, deposit)
ADT.logout()
ADT.closeBrowser()
