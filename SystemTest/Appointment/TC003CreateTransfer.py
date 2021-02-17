from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

af = A()

af.openBrowser()
af.login(foUserId, foUserPwd)
af.counteractivation()