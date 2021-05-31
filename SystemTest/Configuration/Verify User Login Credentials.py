from TestActionLibrary import A
from GlobalShareVariables import GSV

# admin user desk user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

# lab desk user login
labUserId = GSV.labUserID
labUserPwd = GSV.labUserPwD

# radiologist desk user login
radUserId = GSV.radioUserID
radUserPwd = GSV.radioUserPwD

# pharmacy desk user login
phaUserId = GSV.pharmacyUserID
phaUserPwd = GSV.pharmacyUserPwD

# nurse desk user login
nurUserId = GSV.nurseUserID
nurUserPwd = GSV.nurseUserPwD

# store desk user login
stoUserId = GSV.storeUserID
stoUserPwd = GSV.storeUserPwD

config = A()

config.openBrowser()
config.login(admUserId, admUserPwd)
config.logout()
config.login(foUserId, foUserPwd)
config.logout()
config.login(labUserId, labUserPwd)
config.logout()
config.login(radUserId, radUserPwd)
config.logout()
config.login(phaUserId, phaUserPwd)
config.logout()
config.login(nurUserId, nurUserPwd)
config.logout()
config.login(stoUserId, stoUserPwd)
config.logout()
config.closeBrowser()
print("Status:Passed - > TC00 Verify User Login Credentials")
