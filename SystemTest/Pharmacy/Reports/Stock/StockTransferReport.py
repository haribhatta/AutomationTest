import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LMPR
import Library.LibModuleDispensary as LD


# pharmacy desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName


qty = 1

########
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LMPR.getStockTransferReport(EMR)
LMPR.preStockTransferReport()
LP.transferMainStore2MainDispensary(danpheEMR=EMR, drugname=GSV.drug1BrandName, qty=1)
LMPR.getStockTransferReport(EMR)
LMPR.verifyStockSummaryReportBeforeReceiving(qty=1)
LD.activateDispensaryCounter(EMR, "MainDispensary")
LD.receiveItem(EMR, qty)
LMPR.getStockTransferReport(EMR)
LMPR.verifyStockSummaryReportAfterReceiving(qty=1)
# LP.transferMainDispensary2MainStore(danpheEMR=EMR, drugname="Niko", qty=qty)
AC.logout()
AC.closeBrowser()

# Transfer to Main dispensary is fail due to issue EMR-4824

