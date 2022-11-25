#-------------Objective of this script----------
# To verify Accounting-Reports-Trial Balance Report:
# Transaction amount should be on both Dr and Cr side for each Ledgers

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB
import Library.LibModuleBilling as LB
import Library.LibModuleAccounting as LA

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

# admin  user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD

ledger1 = GSV.Ledger_1
ledger2 = GSV.Ledger_2

#-------------Script Owner: Hari---------------- Log-log-log (333)
#Scripted on: 29.01.2078

EMR = AC.openBrowser()
#add voucher in ledger
AC.login(admUserId, admUserPwd)
voucherNo = LA.createManualVoucher(danpheEMR=EMR, ledger1=ledger1, ledger2=ledger2)
LA.verifyVoucherReport(danpheEMR=EMR, voucherNo=voucherNo)
LA.getTrialBalanceReport(danpheEMR=EMR)
AC.logout()
AC.closeBrowser()