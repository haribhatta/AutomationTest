''''
Objective:
To test EMR-904: Pharmacy | Good Receipt | Failed to add Good receipt.

Steps:
1. Navigate to Billing Module
2. Register patient with shortcut key (ALT+N)
3. Add lab item for billing request and print the invoice.
4. Then go to Lab Module -> Sample Collection
5. Duplicate requisition is created for same patient.
6. Verify and view details for Sample collection process.

Issue:
LAB | Duplicate lab requisition is created after billing.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB
import Library.LibModuleBilling as LB
import Library.LibModuleLaboratory as LL

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

# lab user login
labUserId = GSV.labUserID
labUserPwd = GSV.labUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
paymentmode = "Cash"
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymentmode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
labitem = GSV.TFT
imagingtest = GSV.USG
LB.createlabxrayinvoice(EMR, HospitalNo, labitem, imagingtest)
#glr.verifylabxrayinvoice()
AC.logout()

AC.login(labUserId, labUserPwd)
LB.verifySampleCollectionDuplicateEntry()
LL.collectLabSample(EMR, HospitalNo, labitem)
LL.checkLabDuplicateRequisition(danpheEMR=EMR, HospitalNo=HospitalNo, ItemName=imagingtest)
AC.logout()
AC.closeBrowser()
print("LPH-904 Passed")
