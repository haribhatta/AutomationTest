import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
# pharmacy user login
phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD
drug1Name = GSV.drug1BrandName
drug1Rate = GSV.drug1Rate
paymentMode = 'Credit'
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
pInvoiceNo, tender = LD.createDispensarySaleMultipleItems(danpheEMR=EMR, HospitalNo=HospitalNo, drugname=drug1Name, drugname1=GSV.drug2BrandName, qty1=5, qty2=4, paymentmode=paymentMode)
print(pInvoiceNo)
print(tender)
totalamount = LD.getDetailsFromSalesList(danpheEMR=EMR, invoiceNumber=pInvoiceNo)
LD.getgridAndViewDetailsCreditSettelment(danpheEMR=EMR, HospitalNo=HospitalNo, creditamount=totalamount)
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo, qty=1, returnremark="Wrong entry")
LD.getgridAndViewDetailsCreditSettlementAfterPartialReturn(danpheEMR=EMR, HospitalNo=HospitalNo, creditamount=totalamount)
AC.logout()
AC.closeBrowser()