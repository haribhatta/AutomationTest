# only Sales Report is included in this report , No any Return sales are included in this report
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleDispensary as LD
import Library.LibModulePatientPortal as LPP

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drugname = GSV.drug1BrandName
qty = 1
rate = GSV.drug1Rate
amount = qty*rate
totalamount = round(amount)
drug1Name = GSV.drug1BrandName

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
HospitalNo = LPP.getRandomPatient(EMR)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
LPR.getSystemPharmacyBillWiseSalesReport(danpheEMR=EMR)
LPR.preSystemPharmacyBillWiseSalesReport()
InvoiceNo = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=1, drugName=drug1Name, paymentmode='Cash')
LPR.getSystemPharmacyBillWiseSalesReport(danpheEMR=EMR)
LPR.verifySystemPharmacyBillWiseSalesReport(danpheEMR=EMR, invoiceNo=InvoiceNo, cash=totalamount, cashReturn=0, credit=0, creditReturn=0, totalAmount=totalamount, discountAmount=0)
AC.logout()
AC.closeBrowser()
