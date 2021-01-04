#Objective: To cover the OPD bill amount deduction from deposit balance where deposit balance < Total Amount and cash return from tender.

from TestActionLibrary import A

deposit = "300"
testname = "LDH"

bsddpt = A()
bsddpt.openBrowser()
bsddpt.login("billing1", "pass123")
bsddpt.counteractivation()
bsddpt.patientRegistration()
bsddpt.opDeposit(deposit)
bsddpt.opDepositDbilingTenderCashReturn(deposit, testname)
bsddpt.logout()
bsddpt.closeBrowser()


