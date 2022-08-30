########Defining Variables for LPH
#runEnv = 'free'
appName = input("Please enter project/application name:\n"
                "SNCH\n"
                "MMH\n"
                "LPH\n"
                "MPH\n"
                "RTM\n"
                "RCH\n"
                "Core\n"
                "Hope\n")

if appName == "LPH":
      appURL = "http://202.51.74.168:453/"
###TestAction>>LogIn:
      #admin user
      adminUserID = 'Admin'
      adminUserPwD = 'DanpheHIMS@123'    # '28A7hi0jvH0='
      #IT user
      itUserID = 'Admin' #'bhuwan'
      itUserPwD = 'DanpheHIMS@123'
      #billing user
      foUserID = 'Admin' #'ashmita' #LPH user
      foUserPwD = 'DanpheHIMS@123'
      foUserName = 'Mr. admin admin' #'Ms. Ashmita Karki'
      #Lab user
      labUserID = 'Admin' #'karuna'
      labUserPwD = 'DanpheHIMS@123'
      #ER Lab user
      ERlabUserID = 'Admin' #'erlab'
      ERlabUserPwD = 'DanpheHIMS@123'
      #radiologist user
      radioUserID = 'Admin' #'radiology'
      radioUserPwD = 'DanpheHIMS@123'
      #pharmacy user
      pharmacyUserID = 'Admin' #'padam'
      pharmacyUserPwD = 'DanpheHIMS@123'
      pharmacyUserName = 'admin admin'
      #pharmacyUserName = 'Ms. Debika'
      #nurse user
      nurseUserID = 'Admin'
      nurseUserPwD = 'DanpheHIMS@123'
      #store user
      storeUserID = 'Admin' #'shreeram'
      storeUserPwD = 'DanpheHIMS@123'
      #Medical Record user
      MRUserID = 'Admin'  #'mr'
      MRUserPwD = 'DanpheHIMS@123'
      #vaccination user
      vaccineUserID = 'Admin' #'surendra'
      vaccineUserPwD = 'DanpheHIMS@123'
###TestAction>>BillingItems:
      opdRate = 30
      deposit = 100
      CBC = "CBC"
      TFT = "TFT"
      TFTRate = 800
      LDH = "LDH"
      USG = "USG ABDOMEN/PELVIS"
      usgRate = 700
      admitRate = 30
      UrineRE = "URINE R/E"
      BTCT = "BT/CT"
      btctRate = 100
      erTest = "TC"
      LabType = "ER"
      #EHS Billing
      opdRateEHS = 400
      discountCommunityName = "SOCIAL SERVICE UNIT"
      discountSchemeName = "Helpless (50%)"
###TestAction>>Pharmacy/Store+DispensaryItems:
      drug1GenericName = 'PANTOPRAZOLE 40 MG TAB'
      drug1Rate = 5
      drug1BrandName = 'PETOR 40 MG'
      drug2BrandName = "MACLAR 500MG TAB"
      drug2GenericName = "CLARITHROMYCIN"
      drug2Rate = 563.5
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3
      insurancedrug = "AMFAST 5MG TAB"
      drug1NarcoticName = "MORFIUM 10 MG TAB"
      drug1NarcoticRate ="4"
      drugType = 'GASTRIC'
      drugCompany = 'HIMALAYA'
      dispensaryName1 = "MainDispensary"
      dispensaryName2 = "Insurance Dispensary"
      pharmacySupplierName1 = "ASHWANI PHARMACY"
      salesCategoyType = "Pharmacy Unit"
      supplier = "AAHANA PHARMA"
###TestAction>>Inventory+Procurement+SubStore:
      inventoryName1 = "General Inventory"
      inventoryName2 = "Medical Inventory"
      subStoreName1 = "ACCOUNT"
      subStoreName2 = "ADMINISTRATION"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      storeItem1Name = "PLANE SCISSOR 6"
      storeItem1Rate = 25
      stationaryItem2 = "DIAMOND PENCIL "
      stationaryItem1 = "USG PAPER"
      ###Suppliers Name list
      inventorySupplierName1 = "Shremad Tech."
###TestAction>>Doctor:

###TestAction>>ADT:
      generalWard = "Labour Ward"
      generalBedFeature = "General Bed"
      admitWard = "Labour Ward"
      admitBed = "General Bed"
      generalWard = "Labour Ward"
      generalBedFeature = "General Bed"
###TestAction>>Settings:
      UserBilling = 'Mr. Bhagawati Pandey'
      doctorGyno = "dr subash pokhrel"
      departmentGyno = "GYNAE & OBS"
      doctorGynoEHS = "Dr. Anupa Thapa"
      doctor2 = "Mr. admin admin"

# Dispensary Credit Organization
      creditOrganization = "LPH-Default Cr. Organization"
###############################################################################
########Defining Variables for SNCH
if appName == "SNCH":
      appURL = "http://202.51.74.168:168/"
###TestAction>>LogIn:
      # admin user
      adminUserID = 'Admin'
      adminUserPwD = 'DanpheHIMS@123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'Admin' #'sabitri'
      foUserPwD = 'DanpheHIMS@123'
      foUserName = 'Mr. admin admin' #'Ms. Sabitri Sharma Adhikari'
      #IT user
      itUserID = 'Admin' #'rn'
      itUserPwD = 'DanpheHIMS@123'
      #pharmacy user
      pharmacyUserID = 'Admin' #'shivraj'
      pharmacyUserPwD = 'DanpheHIMS@123'
      pharmacyUserName = 'admin admin' #'shiv raj'
      #laboratory user
      labUserID = 'Admin'
      labUserPwD = 'DanpheHIMS@123'
      # Radiology user
      radioUserID = 'Admin'
      radioUserPwD = 'DanpheHIMS@123'
      #Inventory user
      storeUserID = 'Admin'
      storeUserPwD = 'DanpheHIMS@123'
      #Medical Record user
      MRUserID = 'Admin' #'haris'
      MRUserPwD = 'DanpheHIMS@123'
###TestAction>>BillingItems:
      opdRate = 500
      deposit = 200
      CBC = "CBC"
      TFT = "FREE TFT"   #TFT(FT3,FT4,TSH) CLLEA
      T3 = "FT3"
      T4 = "FT4"
      TSH = "TSH"
      TFTRate = 1200
      LDH = "LDH"
      UrineRE = "URINE R/E" # this gets changed on V1.49.3
      BTCT = "BT/CT"
      btctRate = 300
      USG = "USG ABDOMIN AND PELVIS"
      usgRate = 1000
      admitRate = 1500
      discountCommunityName = "Hospital"
      discountSchemeName = "Referal (10%)"
      ReferredBy = "Dr. Amit Chaturbedi"
###TestAction>>Pharmacy/Store+DispensaryItems:
      drug1BrandName = "SINEX TAB"
      drug1GenericName = "PARACETAMOL"
      drug1Rate = float(3)
      drug2BrandName = 'ASTHALIN 2.5ml'
      drug2BrandRate = 1.14
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3
      drugAasma = 'AASMA 150 XR TAB'
      drug1NarcoticName = "MORFIUM 1ML ING"
      drug1NarcoticRate = 100
      drugType = 'SURGICALS'
      drugCompany = 'HIMALAYANS'
      dispensaryName1 = "MainDispensary"
      dispensaryName2 = "Insurance Dispensary"
      pharmacySupplierName1 = "AAKAR ENTERPRISES"
      supplier = "JOSHI TRADE CONCERN"
      ###TestAction>>Inventory+Procurement+SubStore:
      inventoryName1 = "General Inventory"
      inventoryName2 = "Medical Inventory"
      subStoreName1 = "ACCOUNT"
      subStoreName2 = "ADMINISTRATION"
      A4Paper = 'A4 PAPER'
      storeItem1Name = 'A4 PAPER'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      stationaryItem1 = "PENCIL"
      stationaryItem2 = "DOTPEN"
      File = "FILE"
      SubStore1 = "General"
      SubStore2 = "PostOps"
      inventorySupplierName1 = "Shremad Tech."
      salesCategoyType = "Pharmacy Unit"
###TestAction>>Doctor:

###TestAction>>ADT:
      generalWard = "General Ward"
      GeneralWard = "ICU"
      bedFeature = "BED CHARGE General Ward"
      admitWard = "Pediatric Ward"
      admitBed = "Pediatric Bed Charge"
###TestAction>>Settings:
      user = "admin"
      doctorGyno = "Dr. Jyoti Rana"
      departmentGyno = "Gynecology"
      departmentNephro = "Nephro"
# Dispensary Credit Organization
      creditOrganization = "SCH Staff Account"
###############################################################################
########Defining Variables for Medi Plus
if appName == "MPH":
      appURL = "http://202.51.74.168:129/"
###TestAction>>LogIn:
      #admin user
      adminUserID = 'admin'
      adminUserPwD = 'DanpheHIMS@123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'admin' #bandana
      foUserPwD = 'DanpheHIMS@123'
      foUserName = 'Ms. Bandana Harmel'
      #IT user
      itUserID = 'admin' #'alina'
      itUserPwD = 'DanpheHIMS@123'
      #Lab user
      labUserID = 'admin' #'supriya'
      labUserPwD = 'DanpheHIMS@123'
      #ER Lab user
      ERlabUserID = 'admin' #'erlab'
      ERlabUserPwD = 'DanpheHIMS@123'
      #radiologist user
      radioUserID = 'admin' #'basudev'
      radioUserPwD = 'DanpheHIMS@123'
      #pharmacy user
      pharmacyUserID = 'admin' #'kishor'
      pharmacyUserPwD = 'DanpheHIMS@123'
      #nurse user
      nurseUserID = 'admin'
      nurseUserPwD = 'DanpheHIMS@123'
      #store user
      storeUserID = 'admin' #'radha'
      storeUserPwD = 'DanpheHIMS@123'
###TestAction>>BillingItems:
      opdRate = 660
      deposit = 1000
      CBC = "COMPLETE BLOOD COUNT-CBC"
      CBCRate = 1100
      TFT = "TFT"
      T3 = "FT3"
      T4 = "FT4"
      TSH = "TSH"
      TFTRate = 500
      LDH = "LDH"
      LDHRate = 600
      USG = "USG ABDOMEN AND PELVIS"
      usgRate = 1300
      admitRate = 30
      UrineRE = "URINE R/E "
      UrineRERare = 125
      BTCT = "BT CT"
      btctRate = 200
      erTest = "TC, DC"
      LabType = "ER"
      discountCommunityName = "Hospital"
      discountSchemeName = "Staff Family (30%)"
      creditOrganization = "MEDIPLUS"
###TestAction>>Pharmacy/Store+DispensaryItems:
      drug1BrandName = 'NIKO DROP 15ML BOTTLE'
      drug1GenericName = 'PARACETAMOL 150MG/ML ORAL DROP 15ML BOTTLE'
      drug1Rate = 25
      drug2BrandName = "MACLAR 500MG TAB"
      drug2GenericName = "CLARITHROMYCIN"
      drug2Rate = 563.5
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX'
      drugSinexRate = 3
      drugType = 'GASTRIC'
      drugCompany = 'HIMALAYA'
      dispensaryName1 = "MainDispensary"
      dispensaryName2 = "Insurance Dispensary"
      pharmacySupplierName1 = "Arati Medical"
      salesCategoyType = "Pharmacy Unit"
###TestAction>>Inventory+Procurement+SubStore:
      inventoryName1 = "General Inventory"
      inventoryName2 = "Medical Inventory"
      subStoreName1 = "Administration Sub Store"
      subStoreName2 = "PostOps"
      inventorySupplierName1 = "Shremad Tech."
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      storeItem1Name = "Tumb Pin"
      storeItem1Rate = 10
      #stationaryItem1 = "DOTPEN"
      stationaryItem1 = "envelop print"
###TestAction>>Doctor:

###TestAction>>ADT:
      generalWard = "General Non-Covid Ward"
      bedFeature = "General Non-Covid Ward"
      admitWard = "General Non-Covid Ward"
      admitBed = "Pediatric Bed Charge"
###TestAction>>Settings:
      UserBilling = 'Mr. Bhagawati Pandey'
      doctorNephro = "Dr. Eva Gauchan"
      departmentNephro = "Pediatrics "
      doctor2 = "Dr. Junu Shrestha"
      doctorGyno = "Dr. Anjali Subedi"
      departmentGyno = "OBG Gynae"

###############################################################################
########Defining Variables for Rhythm
###############################################################################
if appName == "RTM":
      appURL = "http://202.51.74.168:85/"
###TestAction>>LogIn:
      # admin user
      adminUserID = 'admin'
      adminUserPwD = 'DanpheHIMS@123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'mamata'
      foUserPwD = 'DanpheHIMS@123'
      foUserName = 'Ms. Mamata Gartaula'
      #IT user
      itUserID = 'admin'
      itUserPwD = 'DanpheHIMS@123'
      #pharmacy user
      pharmacyUserID = 'admin'
      pharmacyUserPwD = 'DanpheHIMS@123'
      #pharmacyUserName = 'Ms. Prekshya Adhikari'
      pharmacyUserName = 'Prekshya Adhikari' # Ms. is removed due to Rhythm 'User Collection Report' not having salutation field.
      #laboratory user
      labUserID = 'muna'
      labUserPwD = 'DanpheHIMS@123'
      #Inventory user
      storeUserID = 'admin'
      storeUserPwD = 'DanpheHIMS@123'
###TestAction>>BillingItems:
      opdRate = 500
      deposit = 200
      CBC = "CBC(HB,TC,DC,PLT)"
      TFT = "TFT(T3,T4,TSH)"   #TFT(FT3,FT4,TSH) CLLEA
      T3 = "T3"
      T4 = "T4"
      TSH = "TSH"
      TFTRate = 1050
      LDH = "LACTIC DEHYDROGENASE(LDH)"
      UrineRE = "URINE RE/ME" # this gets changed on V1.49.3
      BTCT = "BT/CT"
      btctRate = 350
      USG = "ULTRA SOUND"
      usgRate = 1000
      admitRate = 1200
      discountCommunityName = ""
      discountSchemeName = "Staff (50%)"
      creditOrganization = "Arogin Care Home"
###TestAction>>Pharmacy/Store+DispensaryItems:
      drug1BrandName = "SAMCOBA 1500 MG"
      drug1GenericName = "mecobalamin"
      drug1Rate = 20
      drug2BrandName = 'ASTHALIN 2 MG TAB'
      drug2BrandRate = 1.14
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3
      drugAasma = 'AASMA 150 XR TAB'
      supplier = "AARATI MEDITCHA PVT"
      drug1NarcoticName = "LOZ 1 MG"
      drug1NarcoticRate ="2"
      drugType = 'ABDOMINAL'
      drugCompany = 'HIMALAYA'
      dispensaryName1 = "MainDispensary"
      dispensaryName2 = "Insurance Dispensary"
      pharmacySupplierName1 = "AARATI MEDITCHA PVT"
      ###TestAction>>Inventory+Procurement+SubStore:
      inventoryName1 = "General Inventory"
      inventoryName2 = "Medical Inventory"
      subStoreName1 = "General"
      subStoreName2 = "PostOps"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      storeItem1Name = "Tumb Pin"
      storeItem1Rate = 10
      # stationaryItem1 = "DOTPEN"
      stationaryItem1 = "Sanitizer"
      inventorySupplierName1 = "Shremad Tech."
      salesCategoyType = "Pharmacy"
###TestAction>>Doctor:

###TestAction>>ADT:
      generalWard = "General Ward"
      GeneralWard = "ICU"
      bedFeature = "General"
      admitWard = "General Ward"
      admitBed = "Pediatric Bed Charge"
###TestAction>>Settings:
      user = "admin"
      doctorGyno = "Dr. Lata Gautam"
      departmentGyno = "PSYCHIATRIC"
      departmentNephro = "Nephro"
###############################################################################
########Defining Variables for Radian Skin Care
###############################################################################
if appName == "RSC":
      appURL = "http://172.16.2.34:89/"
###TestAction>>LogIn:
      # admin user
      adminUserID = 'admin'
      adminUserPwD = 'DanpheHIMS@123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'admin'
      foUserPwD = 'DanpheHIMS@123'
      foUserName = 'Admin admin'
      #IT user
      itUserID = 'admin'
      itUserPwD = 'DanpheHIMS@123'
      #pharmacy user
      pharmacyUserID = 'admin'
      pharmacyUserPwD = 'DanpheHIMS@123'
      #pharmacyUserName = 'Ms. Prekshya Adhikari'
      pharmacyUserName = 'Admin admin'
      #laboratory user
      labUserID = 'admin'
      labUserPwD = 'DanpheHIMS@123'
      #Inventory user
      storeUserID = 'admin'
      storeUserPwD = 'DanpheHIMS@123'
###TestAction>>BillingItems:
      opdRate = 500
      deposit = 200
      CBC = "CBC(HB,TC,DC,PLT)"
      TFT = "TFT(T3,T4,TSH)"   #TFT(FT3,FT4,TSH) CLLEA
      T3 = "T3"
      T4 = "T4"
      TSH = "TSH"
      TFTRate = 1050
      LDH = "LACTIC DEHYDROGENASE(LDH)"
      UrineRE = "URINE RE/ME" # this gets changed on V1.49.3
      BTCT = "BT/CT"
      btctRate = 350
      USG = "ULTRA SOUND"
      usgRate = 1000
      admitRate = 1200
      discountCommunityName = ""
      discountSchemeName = "Staff (50%)"
###TestAction>>Pharmacy/Store+DispensaryItems:
      drug1BrandName = "SAMCOBA 1500 MG"
      drug1GenericName = "mecobalamin"
      drug1Rate = 20
      drug2BrandName = 'ASTHALIN 2 MG TAB'
      drug2BrandRate = 1.14
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'tafco 250 mg'
      drugSinexRate = 10.34
      drugAasma = 'AASMA 150 XR TAB'
      supplier = "AARATI MEDITCHA PVT"
      drug1NarcoticName = "LOZ 1 MG"
      drug1NarcoticRate ="2"
      drugType = 'ABDOMINAL'
      drugCompany = 'HIMALAYA'
      dispensaryName1 = "MainDispensary"
      dispensaryName2 = "Insurance Dispensary"
      pharmacySupplierName1 = "AARATI MEDITCHA PVT"
      ###TestAction>>Inventory+Procurement+SubStore:
      inventoryName1 = "General Inventory"
      inventoryName2 = "Medical Inventory"
      subStoreName1 = "General"
      subStoreName2 = "PostOps"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      storeItem1Name = "Tumb Pin"
      storeItem1Rate = 10
      # stationaryItem1 = "DOTPEN"
      stationaryItem1 = "Sanitizer"
      inventorySupplierName1 = "Shremad Tech."
      salesCategoyType = "Pharmacy"
###TestAction>>Doctor:

###TestAction>>ADT:
      generalWard = "General Ward"
      GeneralWard = "ICU"
      bedFeature = "General"
      admitWard = "General Ward"
      admitBed = "Pediatric Bed Charge"
###TestAction>>Settings:
      user = "admin"
      doctorGyno = "Dr. Lata Gautam"
      departmentGyno = "GYNAE & OBS"
      departmentNephro = "Nephro"

###############################################################################
########Defining Variables for Hope Hospital
###############################################################################
if appName == "Hope":
      appURL = "http://202.51.74.168:85/"
###TestAction>>LogIn:
      # admin user
      adminUserID = 'admin'
      adminUserPwD = 'DanpheHIMS@123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'admin'
      foUserPwD = 'DanpheHIMS@123'
      foUserName = 'Admin admin'
      #IT user
      itUserID = 'admin'
      itUserPwD = 'DanpheHIMS@123'
      #pharmacy user
      pharmacyUserID = 'admin'
      pharmacyUserPwD = 'DanpheHIMS@123'
      #pharmacyUserName = 'Ms. Prekshya Adhikari'
      pharmacyUserName = 'Admin admin'
      #laboratory user
      labUserID = 'admin'
      labUserPwD = 'DanpheHIMS@123'
      #radiologist user
      radioUserID = 'admin' #'basudev'
      radioUserPwD = 'DanpheHIMS@123'
      #Inventory user
      storeUserID = 'admin'
      storeUserPwD = 'DanpheHIMS@123'
###TestAction>>BillingItems:
      opdRate = 500
      deposit = 200
      CBC = "CBC (COMPLETE BLOOD COUNT))"
      TFT = "TFT"   #TFT(FT3,FT4,TSH) CLLEA
      T3 = "T3"
      T4 = "T4"
      TSH = "HORMONE TSH"
      TFTRate = 1000
      LDH = "LDH"
      UrineRE = "INS URINE ROUTINE EXAM" # this gets changed on V1.49.3
      BTCT = "BT / CT"
      btctRate = 175
      USG = "USG GUIDED DIAGNOSTIC PLEURAL TAPPING "
      usgRate = 1575
      admitRate = 1200
      discountCommunityName = ""
      discountSchemeName = 'PCR Discount scheme (10%)'
      creditOrganization = "Muna"
###TestAction>>Pharmacy/Store+DispensaryItems:
      drug1BrandName = "Frusix 20 mg"
      drug1GenericName = "FRUSEMIDE"
      drug1Rate = 1.2
      drug2BrandName = 'ALCAL D 500 MG'
      drug2BrandRate = 4.906
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'tafco 250 mg'
      drugSinexRate = 10.34
      drugAasma = 'AASMA 150 XR TAB'
      supplier = "AARATI MEDITCHA PVT"
      drug1NarcoticName = "LOZ 1 MG"
      drug1NarcoticRate ="2"
      drugType = 'ABDOMINAL'
      drugCompany = 'HIMALAYA'
      dispensaryName1 = "MainDispensary"
      dispensaryName2 = "Insurance Dispensary"
      pharmacySupplierName1 = "AARATI MEDITCHA PVT"
      ###TestAction>>Inventory+Procurement+SubStore:
      inventoryName1 = "General Inventory"
      inventoryName2 = "Medical Inventory"
      subStoreName1 = "General"
      subStoreName2 = "PostOps"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      storeItem1Name = "Tumb Pin"
      storeItem1Rate = 10
      # stationaryItem1 = "DOTPEN"
      stationaryItem1 = "Sanitizer"
      inventorySupplierName1 = "Shremad Tech."
      salesCategoyType = "Pharmacy"
###TestAction>>Doctor:

###TestAction>>ADT:
      generalWard = "General Ward"
      GeneralWard = "ICU"
      bedFeature = "General"
      admitWard = "General Ward"
      admitBed = "Pediatric Bed Charge"
###TestAction>>Settings:
      user = "admin"
      doctorGyno = "Dr. Sunita Bhandari"
      departmentGyno = "GYNAECOLOGY/OBS"
      departmentNephro = "Nephrology"
###TestAction>>Accounting:
      Ledger_1 = "Dr. Sunita Bhandari"
      Ledger_2 = "Cash"



   #def __str__():
    #  return