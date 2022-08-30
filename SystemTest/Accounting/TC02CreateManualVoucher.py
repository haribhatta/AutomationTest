''''
The objective of this test case is to test below scenarios:
1. Check manual voucher entry

'''
########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAccounting as LA
#############
# admin user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
ledger1 = GSV.Ledger_1
ledger2 = GSV.Ledger_2
#discountScheme = GSV.discountSchemeName
#############
EMR = AC.openBrowser()
AC.login(admUserId, admUserPwd)
voucherNo = LA.createManualVoucher(danpheEMR=EMR, ledger1=ledger1, ledger2=ledger2)
LA.verifyVoucherReport(danpheEMR=EMR, voucherNo=voucherNo)
AC.logout()
AC.closeBrowser()