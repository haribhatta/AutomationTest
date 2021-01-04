from TestActionLibrary import A

#------------Local Variables --------------
labitem = "TFT(T3,T4,TSH)"
imagingitem = "XRAY-3155"

oblx = A()
oblx.openBrowser()
oblx.login("billing1", "pass123")
oblx.counteractivation()
oblx.patientquickentry(0, 'Cash')
oblx.verifyopdinvoice(deposit=0, billamt=500)
oblx.createlabxrayinvoice(labitem, imagingitem)
oblx.verifylabxrayinvoice()
oblx.logout()
oblx.closeBrowser()
print("Status:Passed -> TC002OPDbillingLabXray.py")
