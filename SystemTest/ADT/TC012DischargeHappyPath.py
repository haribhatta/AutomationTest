#-------------Objective of this script----------
# To verify successful discharge of already admitted patient.

from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

#------------Local Veriables-------------------
#labitem = "Urine RE/ME"
#imagingitem ="USG ABDOMEN & PELVIS"
deposit = 0

#-------------Script Owner: Hari----------------
#Scripted on: 12.05.2077

ADT = A()
ADT.openBrowser()
ADT.login(foUserId, foUserPwd)
ADT.counteractivation()
for x in range(6):
    ADT.admitDisTrans(0, 1, 0, deposit)
ADT.logout()
ADT.closeBrowser()
print("TC012 DischargeHappyPath: Passed")
