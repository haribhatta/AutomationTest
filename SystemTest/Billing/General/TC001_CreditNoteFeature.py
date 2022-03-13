"""
Description:
1. Credit not is used to return items partially from a whole bill. eg: Out of 3 items, user should be able to return only 1 or two or all three.
2. User can enter the invoice number and search to see all available items of that invoice. Note: If an item is already returned then that item will not be seen in this list anymore.
3. ReturnQty should be filled correctly in order to return that item. i.e: ReturnQty should be NON-ZERO, NON-NEGATIVE, and shouldn’t be more than AvailableQty.
4. Remarks is compulsory for the Credit Note.
5. Once a creditnote is submitted, it should be printable from the popup above the same page.
6. User can generate multiple Credit Notes of a same Invoice. Given that there are still one or more items left to be returned.
7. Duplicate print of credit note should be available (its covered in separate Jira story)
8. ReturnRestrictionRules (Parameterized) can be applied to restrict the return of eg: Lab-Tests after sample is collected, or Result is added. Similarly for ImagingItems.

Impacts On features:
1. Cash Collection
2. Sales

Impact on Pages:
1. Billing Dashboard > User/Counter Collection.
2. Handover > Counter.
3. User Collection Report.
4. Income Segregation Report.
"""

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

opdticket = GSV.opdRate
returnamount = opdticket
labtest1 = GSV.TFT
usgtest1 = GSV.USG

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType="Normal")
InvoiceNo1 = LB.createlabxrayinvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=labtest1, imagingtest= usgtest1)
LB.returnBillingInvoicePartial(danpheEMR=EMR, InvoiceNo=InvoiceNo, returnmsg='Cash P Return') # Scenario: 1
LB.verifyCreditNoteDuplicateInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo1)    # Scenario: 2





