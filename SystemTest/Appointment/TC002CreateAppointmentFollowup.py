from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

can = A()

can.openBrowser()
can.login(foUserId, foUserPwd)
can.counteractivation()
can.followUpAppointment()
can.logout()
can.closeBrowser()

