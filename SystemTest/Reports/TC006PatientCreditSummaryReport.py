#Tested Scenarios:
#  Same Day
# 1.Cash Invoice,
# 2.Return Cash Invoice,
# 3.Credit Invoice,
# 4.Return Credit Invoice,
# 5. Credit Payment,
# 6.Provisional billing,
# 7.Cancel Provisional bill,
# 8.Deposit,
# 9.Deduct Deposit,
# 10.Refund Deposit.
# 11.Repeat Scenarios 1-10 for different date.

from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

pcsr = A()

pcsr.openBrowser()
pcsr.login(foUserId, foUserPwd)
pcsr.counteractivation()
pcsr.patientquickentry(0, "CREDIT")
pcsr.getPatientCreditSummary()
#pcsr.logout()
#pcsr.closeBrowser()