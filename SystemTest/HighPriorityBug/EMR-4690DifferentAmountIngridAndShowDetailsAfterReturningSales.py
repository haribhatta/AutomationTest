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
creditOrganization = GSV.creditOrganization
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
pInvoiceNo, tender = LD.createDispensarySaleMultipleItems(danpheEMR=EMR, HospitalNo=HospitalNo, drugname=drug1Name, drugname1=GSV.drug2BrandName, qty1=5, qty2=4, creditOrganization=creditOrganization, paymentmode=paymentMode)
print(pInvoiceNo)
print(tender)
totalamount = LD.getDetailsFromSalesList(danpheEMR=EMR, invoiceNumber=pInvoiceNo)
LD.getgridAndViewDetailsCreditSettelment(danpheEMR=EMR, creditOrganization=creditOrganization, HospitalNo=HospitalNo, creditamount=totalamount)
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo, qty=1, returnremark="Wrong entry")
LD.getgridAndViewDetailsCreditSettlementAfterPartialReturn(danpheEMR=EMR, creditOrganization=creditOrganization, HospitalNo=HospitalNo, creditamount=totalamount)
LD.settleDispensaryCreditInvoice(danpheEMR=EMR, creditOrganization=creditOrganization, HospitalNo=HospitalNo)
pInvoiceNo2, tender2 = LD.createDispensarySaleMultipleItems(danpheEMR=EMR, HospitalNo=HospitalNo, drugname=drug1Name, drugname1=GSV.drug2BrandName, qty1=4, qty2=2, creditOrganization=creditOrganization, paymentmode=paymentMode)
print(pInvoiceNo2)
print(tender2)
totalamount2 = LD.getDetailsFromSalesList(danpheEMR=EMR, invoiceNumber=pInvoiceNo2)
LD.getgridAndViewDetailsCreditSettelment(danpheEMR=EMR, creditOrganization=creditOrganization, HospitalNo=HospitalNo, creditamount=totalamount2)
LD.returnDispensaryInvoice(danpheEMR=EMR, pInvoiceNo=pInvoiceNo2, qty=1, returnremark="Wrong entry")
LD.getgridAndViewDetailsCreditSettlementAfterPartialReturn(danpheEMR=EMR, creditOrganization=creditOrganization, HospitalNo=HospitalNo, creditamount=totalamount2)
AC.logout()
AC.closeBrowser()
