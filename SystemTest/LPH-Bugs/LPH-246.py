# ADT -> failed to admit the patient.
from TestActionLibrary import A
from GlobalShareVariables import GSV


adminId = GSV.adminUserID
adminPwd = GSV.adminUserPwD

deposit = 0
ADT = A()

ADT.openBrowser()
ADT.login(adminId, adminPwd)
ADT.patientRegistration()
ADT.counteractivation()
ADT.admitDisTrans(1, 0, 0, deposit=0, doctor=GSV.doctor1, department=GSV.department1)
ADT.logout()
ADT.closeBrowser()
print("patient has been add successfully")