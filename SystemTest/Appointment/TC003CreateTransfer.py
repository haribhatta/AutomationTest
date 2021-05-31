from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

af = A()

af.openBrowser()
af.login(foUserId, foUserPwd)
af.counteractivation()