'''
Test Case Senario
1. Item Billing
2. Pharmacy Billing
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleInsurance as LI
import Library.LibModuleBilling as LB
import Library.LibModuleDispensary  as LD
#AC.applicationSelection()
EMR = AC.openBrowser()

# front desk user login
foUserId = GSV.itUserID
foUserPwd = GSV.itUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
labTestTFT = GSV.TFT
radioTestUSG = GSV.USG
foUserId1 = GSV.pharmacyUserID
foUserPwd1 = GSV.pharmacyUserPwD
Dispensary1 = "InsuranceDispensary"
dispensaryName = "InsuranceDispensary"
drug1GenericName = 'PANTOPRAZOLE 40 MG TAB'
drug1Rate = 5
drug1BrandName = 'PETOR 40 MG'
priceCategoryType = "Normal"
#############

AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new Insurance patient.
NSHINO = LI.insurancePatientRegistration(danpheEMR=EMR)
LI.insuranceNewVisit(danpheEMR=EMR, NSHI=NSHINO)
PreInvoiceNo = LI.NewInsurancePatientBilling(danpheEMR=EMR, NSHI=NSHINO, lab=labTestTFT)
LI.PatientWiseClaimReport(danpheEMR=EMR, HospitalNo=NSHINO, PreInvoiceNo=PreInvoiceNo)
AC.logout()

# 1. To Create INSPharmacy Billing. #
AC.login(foUserId1, foUserPwd1)
LD.activatePharmacyCounter(EMR, dispensaryName='InsuranceDispensary')
PreInvoice = LI.insuranceDispensarySell(danpheEMR=EMR, NSHINO=NSHINO , genericname=drug1GenericName, drugname=drug1BrandName)
AC.logout()

AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LI.PatientWiseClaimReport(danpheEMR=EMR, HospitalNo=NSHINO, PreInvoiceNo=PreInvoice)
AC.logout()
AC.closeBrowser()





