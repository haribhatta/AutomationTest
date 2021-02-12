from TestActionLibrary import A

# admin user desk user login
admUserId = A.adminUserID
admUserPwd = A.adminUserPwD

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

# lab desk user login
labUserId = A.labUserID
labUserPwd = A.labUserPwD

# radiologist desk user login
radUserId = A.radioUserID
radUserPwd = A.radioUserPwD

# pharmacy desk user login
phaUserId = A.pharmacyUserID
phaUserPwd = A.pharmacyUserPwD

# nurse desk user login
nurUserId = A.nurseUserID
nurUserPwd = A.nurseUserPwD

# store desk user login
stoUserId = A.storeUserID
stoUserPwd = A.storeUserPwD

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
