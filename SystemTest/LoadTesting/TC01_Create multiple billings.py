# Scenarios to cover:
# 1. Create multiple visits
# 2. Create multiple OP lab billing
# 3. Create multiple OP radio billing
# 4. Create multiple IP lab billing
# 5. Create multiple OP radio billing

from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

LPT = A()

LPT.openBrowser()
LPT.login(foUserId, foUserPwd)
LPT.counteractivation()
i = 0
# Scenario-1
for number in range(20):
    LPT.patientquickentry(0, 'Cash')
    i = i+1
    print("$$$$$ We are in number#######", i)

LPT.logout()
LPT.closeBrowser()

