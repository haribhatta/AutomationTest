from TestActionLibrary import A
from TestActionLibrary import GSV

# front desk user login
adminuser = GSV.adminUserID
adminpswd = GSV.adminUserPwD



addEmp= A()
addEmp.openBrowser()
addEmp.login(adminuser, adminpswd)
addEmp.Setting_add_employee()
addEmp.logout()
addEmp.login(adminuser, adminpswd)
addEmp.Setting_Adding_User()
