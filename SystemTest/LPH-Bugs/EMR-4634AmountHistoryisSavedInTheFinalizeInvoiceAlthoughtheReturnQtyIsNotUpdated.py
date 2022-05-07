'''
Amount History is Saved in the Finalized Invoice altough the return quantity is not updated.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleDispensary as LD
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
paymode = "CREDIT"
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LD.activateDispensaryCounter(EMR, dispensaryName='MainDispensary')
LD.createDispensaryProvisionalSlip(EMR, HospitalNo=HospitalNo, drugName=GSV.drug1BrandName, qty=2)
LD.checkProvisionalFinalizeInvoice(EMR, HospitalNo=HospitalNo)
AC.logout()
AC.closeBrowser()
