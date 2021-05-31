#-------------Objective of this script----------
# To verify successful admission of newly registered patient.

from TestActionLibrary import A
from GlobalShareVariables import GSV

# nurse user
nurseUserID = GSV.nurseUserID
nurseUserPwD = GSV.nurseUserPwD

#------------Local Veriables-------------------
#labitem = "Urine RE/ME"
#imagingitem ="USG ABDOMEN & PELVIS"
deposit = 0

#-------------Script Owner: Hari----------------
#Scripted on: 12.05.2077

ADT = A()

ADT.openBrowser()
ADT.login(nurseUserID, nurseUserPwD)
ADT.counteractivation()
ADT.admitDisTrans(0, 0, 1, deposit)
ADT.logout()
ADT.closeBrowser()
print("TC014 TransferHappyPath: Passed")
