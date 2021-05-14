#-------------Objective of this script----------
# To verify Accounting-Reports-Trial Balance Report: Transaction amount should be on both Dr and Cr side for each Ledgers

from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

# admin  user login
admUserId = A.adminUserID
admUserPwd = A.adminUserPwD

#-------------Script Owner: Hari---------------- Log-log-log (333)
#Scripted on: 29.01.2078

Acc = A()
Acc.openBrowser()
#add voucher in ledger
Acc.login(admUserId, admUserPwd)
Acc.createManualVoucher()