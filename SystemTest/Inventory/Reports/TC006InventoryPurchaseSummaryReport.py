import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI
import Library.LibModuleProcurement as LP

# front desk user login
storeUserId = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD

item = "Pencil"
rate = 5
qty = 1
store1 = "Main Store"
store2 = "Accounting Store"
########
EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
LI.activateInventory(EMR, 'General Inventory')
LI.getPurchaseSummaryReport(EMR)
LI.prePurchaseSummaryReport()
BillNo = LI.createInventoryGoodReceipt(EMR, qty, item, rate)
print("Bill Number of created Good Receipt is ", BillNo)
LI.getPurchaseSummaryReport(EMR)
LI.verifyPurchaseSummaryReportAfterGR(qty, rate)
LP.cancelInventoryGoodsReceipt(EMR, BillNo)
LI.getPurchaseSummaryReport(EMR)
LI.verifyPurchaseSummaryReportAfterGRCancellation()
AC.logout()
AC.closeBrowser()
