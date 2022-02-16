import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI
import Library.LibModuleProcurement as LP

# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
'''
item = "Pencil"
rate = 5
qty = 1
store1 = "Main Store"
store2 = "Accounting Store"
'''
item = GSV.storeItem1Name
print("Item:", item)
qty = 1
rate = GSV.storeItem1Rate
totalAmount = qty * rate
print("TotalAmount:", totalAmount)
print("Rate:", rate)
store1 = GSV.store1
store2 = GSV.SubStore2
Inventory1 = GSV.Inventory1
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LI.activateInventory(EMR, Inventory1)
LI.getPurchaseSummaryReport(EMR)
LI.prePurchaseSummaryReport()
########### Create Credit GR
BillNo = LI.createInventoryGoodReceipt(EMR, qty, item, rate, paymentMode='Credit')
print("Bill Number of created Good Receipt is ", BillNo)
LI.getPurchaseSummaryReport(EMR)
LI.verifyPurchaseSummaryReportAfterGR(qty, rate, amountCashEntryGR=0, amountCashCancelGR=0, amountCreditEntryGR=totalAmount, amountCreditCancelGR=0)
########### Cancel Credit GR
LP.cancelInventoryGoodsReceipt(EMR, BillNo)
LI.prePurchaseSummaryReport()
LI.getPurchaseSummaryReport(EMR)
LI.verifyPurchaseSummaryReportAfterGR(qty, rate, amountCashEntryGR=0, amountCashCancelGR=0, amountCreditEntryGR=0, amountCreditCancelGR=totalAmount)
########### Create Cash GR
BillNo1 = LI.createInventoryGoodReceipt(EMR, qty, item, rate, paymentMode='Cash')
print("Bill Number of created Good Receipt is ", BillNo)
LI.prePurchaseSummaryReport()
LI.getPurchaseSummaryReport(EMR)
LI.verifyPurchaseSummaryReportAfterGR(qty, rate, amountCashEntryGR=totalAmount, amountCashCancelGR=0, amountCreditEntryGR=0, amountCreditCancelGR=0)
########### Cancel Cash GR
LP.cancelInventoryGoodsReceipt(EMR, BillNo1)
LI.prePurchaseSummaryReport()
LI.getPurchaseSummaryReport(EMR)
LI.verifyPurchaseSummaryReportAfterGR(qty, rate, amountCashEntryGR=0, amountCashCancelGR=totalAmount, amountCreditEntryGR=0, amountCreditCancelGR=0)
AC.logout()
AC.closeBrowser()
