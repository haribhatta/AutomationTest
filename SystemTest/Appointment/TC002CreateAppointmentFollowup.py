from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

can = A()

can.openBrowser()
can.login(foUserId, foUserPwd)
can.counteractivation()
can.followUpAppointment()
can.logout()
can.closeBrowser()

