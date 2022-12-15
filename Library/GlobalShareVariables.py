appName = input("Please enter project/application name:\n"
                "SNCH\n"
                "MMH\n"
                "LPH\n"
                "MPH\n"
                "RTM\n"
                "RCH\n"
                "Core\n"
                "Hope\n"
                "APF\n"
                "Charak\n"
                "matrika\n")

###########################################################################
if appName == "LPH":
    appURL = "http://202.51.74.168:453/"

    # Login Credentials
    # admin user
    adminUserID = 'Admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # IT user
    itUserID = 'Admin'  # 'bhuwan'
    itUserPwD = 'DanpheHIMS@123'
    # billing user
    foUserID = 'Admin'  # 'ashmita' #LPH user
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Mr. admin admin'  # 'Ms. Ashmita Karki'
    # Lab user
    labUserID = 'Admin'  # 'karuna'
    labUserPwD = 'DanpheHIMS@123'
    # ER Lab user
    ERlabUserID = 'Admin'  # 'erlab'
    ERlabUserPwD = 'DanpheHIMS@123'
    # radiologist user
    radioUserID = 'Admin'  # 'radiology'
    radioUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'Admin'  # 'padam'
    pharmacyUserPwD = 'DanpheHIMS@123'
    pharmacyUserName = 'admin admin'
    # pharmacyUserName = 'Ms. Debika'
    # nurse user
    nurseUserID = 'Admin'
    nurseUserPwD = 'DanpheHIMS@123'
    # store user
    storeUserID = 'Admin'  # 'shreeram'
    storeUserPwD = 'DanpheHIMS@123'
    # Medical Record user
    MRUserID = 'Admin'  # 'mr'
    MRUserPwD = 'DanpheHIMS@123'
    # vaccination user
    vaccineUserID = 'Admin'  # 'surendra'
    vaccineUserPwD = 'DanpheHIMS@123'

    # TestAction>>BillingItems:
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

    # EHS Billing
    opdRateEHS = 400
    discountCommunityName = "SOCIAL SERVICE UNIT"
    discountSchemeName = "Helpless (50%)"

    # TestAction>>Pharmacy/Store+DispensaryItems:
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
    drug1NarcoticRate = "4"
    drugType = 'GASTRIC'
    drugCompany = 'HIMALAYA'
    dispensaryName1 = "MainDispensary"
    dispensaryName2 = "Insurance Dispensary"
    pharmacySupplierName1 = "ASHWANI PHARMACY"
    salesCategoyType = "Pharmacy Unit"
    supplier = "AAHANA PHARMA"

    # TestAction>>Inventory+Procurement+SubStore:
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

    # Suppliers Name list
    inventorySupplierName1 = "Shremad Tech."

    # TestAction>>ADT:
    generalWard = "Labour Ward"
    generalBedFeature = "General Bed"
    admitWard = "Labour Ward"
    admitBed = "General Bed"

    # TestAction>>Settings:
    UserBilling = 'Mr. Bhagawati Pandey'
    doctorGyno = "dr subash pokhrel"
    departmentGyno = "GYNAE & OBS"
    doctorGynoEHS = "Dr. Anupa Thapa"
    doctor2 = "Mr. admin admin"

    # Dispensary Credit Organization
    creditOrganization = "LPH-Default Cr. Organization"

##############################################################################
# This Section is used for Declaring SNCH variables
###############################################################################

if appName == "SNCH":
    appURL = "http://202.51.74.168:168/"

    # SNCH Login Credentials

    # admin user
    adminUserID = 'Admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'Admin'  # 'sabitri'
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Mr. admin admin'  # 'Ms. Sabitri Sharma Adhikari'
    # IT user
    itUserID = 'Admin'  # 'rn'
    itUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'Admin'  # 'shivraj'
    pharmacyUserPwD = 'DanpheHIMS@123'
    pharmacyUserName = 'admin admin'  # 'shiv raj'
    # laboratory user
    labUserID = 'Admin'
    labUserPwD = 'DanpheHIMS@123'
    # Radiology user
    radioUserID = 'Admin'
    radioUserPwD = 'DanpheHIMS@123'
    # Inventory user
    storeUserID = 'Admin'
    storeUserPwD = 'DanpheHIMS@123'
    # Medical Record user
    MRUserID = 'Admin'  # 'haris'
    MRUserPwD = 'DanpheHIMS@123'

    # TestAction>>BillingItems:
    opdRate = 500
    deposit = 200
    CBC = "CBC"
    TFT = "FREE TFT"  # TFT(FT3,FT4,TSH) CLLEA
    T3 = "FT3"
    T4 = "FT4"
    TSH = "TSH"
    TFTRate = 1200
    LDH = "LDH"
    UrineRE = "URINE R/E"  # this gets changed on V1.49.3
    BTCT = "BT/CT"
    btctRate = 300
    USG = "USG ABDOMIN AND PELVIS"
    usgRate = 1000
    admitRate = 1500
    discountCommunityName = "Hospital"
    discountSchemeName = "Referal (10%)"
    DiscountPercent = 10
    ReferredBy = "Dr. Amit Chaturbedi"

    # Test Action: DB Connection
    # import pyodbc
    # import pandas as pd
    #
    # conn = pyodbc.connect("Driver={SQL Server};"
    #                       "Server=DESKTOP-68UCKA5\SQLEXPRESS;"  # DESKTOP-68UCKA5\SQLEXPRESS
    #                       "Database=DanpheEMR_SNCH_UAT;"  # TEST_LIVE_DanpheEMR_MMH_NewV2
    #                       "Trusted_Connection=yes;")
    #
    # ##### Getting pharmacy item rate #####################
    # query = "select CostPrice, MRP from PHRM_MST_Stock where ItemId = (select ItemId from PHRM_MST_Item where ItemName = 'SINEX TAB')"
    # df = pd.read_sql(query, conn)
    # print("df:", df)
    # rate = df.at[0, 'MRP']
    # print("Drug Rate:", rate)
    # CostPrice = df.at[0, 'CostPrice']
    # print("Drug CostPrice:", CostPrice)

    # TestAction>>Pharmacy/Store+DispensaryItems:
    drug1BrandName = "SINEX TAB"
    drug1GenericName = "PARACETAMOL"
    drug1Rate = 3
    drug1CostPrice = 2
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

    # TestAction>>Inventory+Procurement+SubStore:
    inventoryName1 = "General Inventory"
    inventoryName2 = "Medical Inventory"
    subStoreName1 = "ACCOUNT"
    subStoreName2 = "Administration Store"
    A4Paper = 'A4 PAPER'
    storeItem1Name = 'A4 PAPER'
    storeItem2Name = 'Paper Roll'
    PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
    photocopypaperRate = 2300
    stationaryItem1 = "PENCIL"
    stationaryItem2 = "DOTPEN"
    File = "FILE"
    SubStore1 = "General"
    SubStore2 = "PostOps"
    inventorySupplierName1 = "Shremad Tech."
    salesCategoyType = "Pharmacy Unit"

    # TestAction>>ADT:
    generalWard = "General Ward"
    GeneralWard = "ICU"
    bedFeature = "BED CHARGE General Ward"
    admitWard = "Pediatric Ward"
    admitBed = "Pediatric Bed Charge"

    # TestAction>>Settings:
    user = "admin"
    doctorGyno = "Dr. Jyoti Rana"
    departmentGyno = "Gynecology"
    departmentNephro = "Nephro"
    doctor2 = "Amit Chaturbedi"

    # Dispensary Credit Organization
    creditOrganization = "SCH Staff Account"

    # TestAction>>Accounting:
    Ledger_1 = "Sunita "
    Ledger_2 = "Cash"

    # Medical Record Diagnosis
    dianosis1 = "Measles"
    dianosis2 = "Diptheria"

###########################################################################
# This section is used for declaring  MediPlus Variables
###########################################################################

if appName == "MPH":
    appURL = "http://202.51.74.168:129/"

    # Login Credentials for MediPlus Hospital
    # admin user
    adminUserID = 'admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'admin'  # bandana
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Ms. Bandana Harmel'
    # IT user
    itUserID = 'admin'  # 'alina'
    itUserPwD = 'DanpheHIMS@123'
    # Lab user
    labUserID = 'admin'  # 'supriya'
    labUserPwD = 'DanpheHIMS@123'
    # ER Lab user
    ERlabUserID = 'admin'  # 'erlab'
    ERlabUserPwD = 'DanpheHIMS@123'
    # radiologist user
    radioUserID = 'admin'  # 'basudev'
    radioUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'admin'  # 'kishor'
    pharmacyUserPwD = 'DanpheHIMS@123'
    # nurse user
    nurseUserID = 'admin'
    nurseUserPwD = 'DanpheHIMS@123'
    # store user
    storeUserID = 'admin'  # 'radha'
    storeUserPwD = 'DanpheHIMS@123'

    # TestAction>>BillingItems:
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
    USG2 = "USG (ABDOMEN / PELVIS)"
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

    # TestAction>>Pharmacy/Store+DispensaryItems:
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

    # TestAction>>Inventory+Procurement+SubStore:
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
    stationaryItem1 = "envelop print"

    # TestAction>>ADT:
    generalWard = "General Non-Covid Ward"
    bedFeature = "General Non-Covid Ward"
    admitWard = "General Non-Covid Ward"
    admitBed = "Pediatric Bed Charge"

    # TestAction>>Settings:
    UserBilling = 'Mr. Bhagawati Pandey'
    doctorNephro = "Dr. Eva Gauchan"
    departmentNephro = "Pediatrics "
    doctor2 = "Dr. Alisha Surkheti"
    doctorGyno = "Dr. Pravin Baniya"
    departmentGyno = "Dermatology & Cosmatology"

    # Accounting LedgerName
    Ledger_1 = "Vehicle"
    Ledger_2 = "SIDDARTHA BANK LIMITED "

#######################################################################
# This section is used for declaring Rhythm variables
#######################################################################

if appName == "RTM":
    appURL = "http://202.51.74.168:85/"

    # Login credentials of Rythm Hospital User
    # admin user
    adminUserID = 'admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'mamata'
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Ms. Mamata Gartaula'
    # IT user
    itUserID = 'admin'
    itUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'admin'
    pharmacyUserPwD = 'DanpheHIMS@123'
    # pharmacyUserName = 'Ms. Prekshya Adhikari'
    pharmacyUserName = 'Prekshya Adhikari'  # Ms. is removed due to Rhythm 'User Collection Report' not having salutation field.
    # laboratory user
    labUserID = 'muna'
    labUserPwD = 'DanpheHIMS@123'
    # Inventory user
    storeUserID = 'admin'
    storeUserPwD = 'DanpheHIMS@123'

    # TestAction>>BillingItems:
    opdRate = 500
    deposit = 200
    CBC = "CBC(HB,TC,DC,PLT)"
    TFT = "TFT(T3,T4,TSH)"  # TFT(FT3,FT4,TSH) CLLEA
    T3 = "T3"
    T4 = "T4"
    TSH = "TSH"
    TFTRate = 1050
    LDH = "LACTIC DEHYDROGENASE(LDH)"
    UrineRE = "URINE RE/ME"  # this gets changed on V1.49.3
    BTCT = "BT/CT"
    btctRate = 350
    USG = "ULTRA SOUND"
    usgRate = 1000
    admitRate = 1200
    discountCommunityName = ""
    discountSchemeName = "Staff (50%)"
    creditOrganization = "Arogin Care Home"

    # TestAction>>Pharmacy/Store+DispensaryItems:
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
    drug1NarcoticRate = "2"
    drugType = 'ABDOMINAL'
    drugCompany = 'HIMALAYA'
    dispensaryName1 = "MainDispensary"
    dispensaryName2 = "Insurance Dispensary"
    pharmacySupplierName1 = "AARATI MEDITCHA PVT"

    # TestAction>>Inventory+Procurement+SubStore:
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

    # TestAction>>ADT:
    generalWard = "General Ward"
    GeneralWard = "ICU"
    bedFeature = "General"
    admitWard = "General Ward"
    admitBed = "Pediatric Bed Charge"

    # TestAction>>Settings:
    user = "admin"
    doctorGyno = "Dr. Lata Gautam"
    departmentGyno = "PSYCHIATRIC"
    departmentNephro = "Nephro"

###############################################################################
# This Section is used for Defining Variables for Radian Skin Care
###############################################################################

if appName == "RSC":
    appURL = "http://172.16.2.34:89/"
    # Login Credentials for Radiant Skin Care
    # admin user
    adminUserID = 'admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'admin'
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Admin admin'
    # IT user
    itUserID = 'admin'
    itUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'admin'
    pharmacyUserPwD = 'DanpheHIMS@123'
    # pharmacyUserName = 'Ms. Prekshya Adhikari'
    pharmacyUserName = 'Admin admin'
    # laboratory user
    labUserID = 'admin'
    labUserPwD = 'DanpheHIMS@123'
    # Inventory user
    storeUserID = 'admin'
    storeUserPwD = 'DanpheHIMS@123'

    # TestAction>>BillingItems:
    opdRate = 500
    deposit = 200
    CBC = "CBC(HB,TC,DC,PLT)"
    TFT = "TFT(T3,T4,TSH)"  # TFT(FT3,FT4,TSH) CLLEA
    T3 = "T3"
    T4 = "T4"
    TSH = "TSH"
    TFTRate = 1050
    LDH = "LACTIC DEHYDROGENASE(LDH)"
    UrineRE = "URINE RE/ME"  # this gets changed on V1.49.3
    BTCT = "BT/CT"
    btctRate = 350
    USG = "ULTRA SOUND"
    usgRate = 1000
    admitRate = 1200
    discountCommunityName = ""
    discountSchemeName = "Staff (50%)"

    # TestAction>>Pharmacy/Store+DispensaryItems:
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
    drug1NarcoticRate = "2"
    drugType = 'ABDOMINAL'
    drugCompany = 'HIMALAYA'
    dispensaryName1 = "MainDispensary"
    dispensaryName2 = "Insurance Dispensary"
    pharmacySupplierName1 = "AARATI MEDITCHA PVT"

    # TestAction>>Inventory+Procurement+SubStore:
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

    # TestAction>>ADT:
    generalWard = "General Ward"
    GeneralWard = "ICU"
    bedFeature = "General"
    admitWard = "General Ward"
    admitBed = "Pediatric Bed Charge"

    # TestAction>>Settings:
    user = "admin"
    doctorGyno = "Dr. Lata Gautam"
    departmentGyno = "GYNAE & OBS"
    departmentNephro = "Nephro"

###############################################################################
# This section is used for Defining Variables for Hope Hospital
###############################################################################
if appName == "Hope":
    appURL = "http://202.51.74.168:85/"

    # login Credentials for Hope Hospital
    # admin user
    adminUserID = 'admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'admin'
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Admin admin'
    # IT user
    itUserID = 'admin'
    itUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'admin'
    pharmacyUserPwD = 'DanpheHIMS@123'
    # pharmacyUserName = 'Ms. Prekshya Adhikari'
    pharmacyUserName = 'Admin admin'
    # laboratory user
    labUserID = 'admin'
    labUserPwD = 'DanpheHIMS@123'
    # radiologist user
    radioUserID = 'admin'  # 'basudev'
    radioUserPwD = 'DanpheHIMS@123'
    # Inventory user
    storeUserID = 'admin'
    storeUserPwD = 'DanpheHIMS@123'

    # TestAction>>BillingItems:
    opdRate = 500
    deposit = 200
    CBC = "CBC (COMPLETE BLOOD COUNT))"
    TFT = "TFT"  # TFT(FT3,FT4,TSH) CLLEA
    T3 = "T3"
    T4 = "T4"
    TSH = "HORMONE TSH"
    TFTRate = 1000
    LDH = "LDH"
    UrineRE = "INS URINE ROUTINE EXAM"  # this gets changed on V1.49.3
    BTCT = "BT / CT"
    btctRate = 175
    USG = "USG GUIDED DIAGNOSTIC PLEURAL TAPPING "
    usgRate = 1575
    admitRate = 1200
    discountCommunityName = ""
    discountSchemeName = 'PCR Discount scheme (10%)'
    creditOrganization = "Muna"

    # TestAction>>Pharmacy/Store+DispensaryItems:
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
    drug1NarcoticRate = "2"
    drugType = 'ABDOMINAL'
    drugCompany = 'HIMALAYA'
    dispensaryName1 = "MainDispensary"
    dispensaryName2 = "Insurance Dispensary"
    pharmacySupplierName1 = "AARATI MEDITCHA PVT"

    # TestAction>>Inventory+Procurement+SubStore:
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

    # TestAction>>ADT:
    generalWard = "General Ward"
    GeneralWard = "ICU"
    bedFeature = "General"
    admitWard = "General Ward"
    admitBed = "Pediatric Bed Charge"

    # TestAction>>Settings:
    user = "admin"
    doctorGyno = "Dr. Sunita Bhandari"
    departmentGyno = "GYNAECOLOGY/OBS"
    departmentNephro = "Nephrology"

    # TestAction>>Accounting:
    Ledger_1 = "Dr. Sunita Bhandari"
    Ledger_2 = "Cash"

###############################################################################
# This section is used for Defining Variables for MMH Hospital
###############################################################################
if appName == "MMH":
    appURL = "http://localhost:88/"

    # Login Credentials for MMH Hospital
    # admin user
    adminUserID = 'admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'admin'
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Admin admin'
    # IT user
    itUserID = 'admin'
    itUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'admin'
    pharmacyUserPwD = 'DanpheHIMS@123'
    # pharmacyUserName = 'Ms. Prekshya Adhikari'
    pharmacyUserName = 'Admin admin'
    # laboratory user
    labUserID = 'admin'
    labUserPwD = 'DanpheHIMS@123'
    # radiologist user
    radioUserID = 'admin'  # 'basudev'
    radioUserPwD = 'DanpheHIMS@123'
    # Inventory user
    storeUserID = 'admin'
    storeUserPwD = 'DanpheHIMS@123'

    # Test Action: DB Connection
    # import pyodbc
    # import pandas as pd
    #
    # conn = pyodbc.connect("Driver={SQL Server};"
    #                       "Server=DESKTOP-68UCKA5\SQLEXPRESS;"  # DESKTOP-68UCKA5\SQLEXPRESS
    #                       "Database=TEST_LIVE_DanpheEMR_MMH_NewV2;"  # TEST_LIVE_DanpheEMR_MMH_NewV2
    #                       "Trusted_Connection=yes;")
    #
    # # Getting Lab Test Data #####################
    # # query = "SELECT TOP(10) ItemName, Price FROM BIL_CFG_BillItemPrice where Price > 0 and IsActive = 1 and ServiceDepartmentId = (select ServiceDepartmentId from BIL_MST_ServiceDepartment where ServiceDepartmentName = 'biochemistry')"
    # ## TFT##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'TFT'"
    # df = pd.read_sql(query, conn)
    # nameTFT = df.at[0, 'ItemName']
    # print("TFT Name:", nameTFT)
    # rateTFT = df.at[0, 'Price']
    # print("TFT Rate:", rateTFT)
    #
    # ##CBC##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'CBC'"
    # df = pd.read_sql(query, conn)
    # nameCBC = df.at[0, 'ItemName']
    # print("CBC Name:", nameCBC)
    # rateCBC = df.at[0, 'Price']
    # print("CBC Rate:", rateCBC)
    #
    # ##T3##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'T3'"
    # df = pd.read_sql(query, conn)
    # nameT3 = df.at[0, 'ItemName']
    # print("T3 Name:", nameT3)
    # rateT3 = df.at[0, 'Price']
    # print("T3 Rate:", rateT3)
    #
    # ##T4##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'T4'"
    # df = pd.read_sql(query, conn)
    # nameT4 = df.at[0, 'ItemName']
    # print("T4 Name:", nameT4)
    # rateT4 = df.at[0, 'Price']
    # print("T4 Rate:", rateT4)
    #
    # ##TSH##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'TSH'"
    # df = pd.read_sql(query, conn)
    # nameTSH = df.at[0, 'ItemName']
    # print("TSH Name:", nameTSH)
    # rateTSH = df.at[0, 'Price']
    # print("TSH Rate:", rateTSH)
    #
    # ##LDH##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'LDH'"
    # df = pd.read_sql(query, conn)
    # nameLDH = df.at[0, 'ItemName']
    # print("LDH Name:", nameLDH)
    # rateLDH = df.at[0, 'Price']
    # print("LDH Rate:", rateLDH)
    #
    # ##Urine RE/ME##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'Urine RE/ME'"
    # df = pd.read_sql(query, conn)
    # nameUrineRE = df.at[0, 'ItemName']
    # print("Urine RE/ME Name:", nameUrineRE)
    # rateUrineRE = df.at[0, 'Price']
    # print("Urine RE/ME Rate:", rateUrineRE)
    #
    # ##BT##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'BT'"
    # df = pd.read_sql(query, conn)
    # nameBT = df.at[0, 'ItemName']
    # print("BT Name:", nameBT)
    # rateBT = df.at[0, 'Price']
    # print("BT Rate:", rateBT)
    #
    # ##CT##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'CT'"
    # df = pd.read_sql(query, conn)
    # nameCT = df.at[0, 'ItemName']
    # print("CT Name:", nameCT)
    # rateCT = df.at[0, 'Price']
    # print("CT Rate:", rateCT)

    # ##### Getting Imaging Test Data #####################
    # ##USG##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'USG'"
    # df = pd.read_sql(query, conn)
    # nameUSG = df.at[0, 'ItemName']
    # print("USG Name:", nameUSG)
    # rateUSG = df.at[0, 'Price']
    # print("USG Rate:", rateUSG)
    #
    # ##### Getting Other Billing Test Data #####################
    # ##Admission Charge##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'Admission Charge'"
    # df = pd.read_sql(query, conn)
    # nameAdmission = df.at[0, 'ItemName']
    # print("Admission Charge:", nameAdmission)
    # rateAdmission = df.at[0, 'Price']
    # print("Admission Charge:", rateAdmission)
    #
    # ##Credit Organization Name##
    # query = "select OrganizationName from BIL_MST_Credit_Organization where IsActive > 0"
    # df = pd.read_sql(query, conn)
    # creditOrganizationName = df.at[0, 'OrganizationName']
    # print("creditOrganizationName:", creditOrganizationName)
    # creditOrganization = creditOrganizationName
    #
    # ##Billing Department Name##
    # query = "select DepartmentName from MST_Department where Description = 'Gynaecology'"
    # df = pd.read_sql(query, conn)
    # DepartmentGyno = df.at[0, 'DepartmentName']
    # print("Gyno Department Name:", DepartmentGyno)
    #
    # ##Billing Doctor Name##
    # query = "select FirstName from EMP_Employee where DepartmentId = (select DepartmentId from MST_Department where Description = 'Gynaecology')"
    # df = pd.read_sql(query, conn)
    # DoctorGyno = df.at[1, 'FirstName']
    # print("Gyno Doctor Name:", DoctorGyno)
    #
    # query = "select FirstName from EMP_Employee where DepartmentId = (select DepartmentId from MST_Department where Description = 'Nephrology')"
    # df = pd.read_sql(query, conn)
    # doctorNephro = df.at[0, 'FirstName']
    # print("Nephro Doctor Name:", doctorNephro)
    #
    # ########################################################
    #
    # ###TestAction>>BillingItems:
    # opdRate = 500
    # deposit = 200
    # CBC = nameCBC
    # # TFT = "TFT"   #TFT(FT3,FT4,TSH) CLLEA
    # TFT = nameTFT
    # T3 = nameT3
    # T4 = nameT4
    # TSH = nameTSH
    # # TFTRate = 1000
    # TFTRate = rateTFT
    # LDH = nameLDH
    # UrineRE = nameUrineRE
    # BT = nameBT
    # CT = nameCT
    # btRate = rateBT
    # ctRate = rateCT
    # # USG = "USG GUIDED DIAGNOSTIC PLEURAL TAPPING "
    # # usgRate = 1575
    # USG = nameUSG
    # usgRate = rateUSG
    # admitRate = rateAdmission
    #
    # ###Getting discount name and scheme ###
    # query = "select MembershipTypeName, DiscountPercent, CommunityName from PAT_CFG_MembershipType where DiscountPercent > 0"
    # df = pd.read_sql(query, conn)
    # MembershipTypeName = df.at[0, 'MembershipTypeName']
    # print("MembershipTypeName:", MembershipTypeName)
    # DiscountPercent = df.at[0, 'DiscountPercent']
    # print("DiscountPercent:", DiscountPercent)
    # DiscountPercent = int(DiscountPercent)
    # print("DiscountPercent:", DiscountPercent)
    # CommunityName = df.at[0, 'CommunityName']
    # print("CommunityName:", CommunityName)
    # discountSchemeName = MembershipTypeName + " (" + str(DiscountPercent) + "%)"
    # print("discountSchemeName:", discountSchemeName)
    # discountCommunityName = CommunityName
    # discountSchemeName = discountSchemeName
    #
    # ###TestAction>>Pharmacy/Store+DispensaryItems:
    # ##### Getting Pharmacy Billing Test Data ##############
    # ##Drug Name and Rate##
    # query = "select i.ItemName, ss.AvailableQuantity, ss.MRP from PHRM_TXN_StoreStock ss inner join PHRM_MST_Item i on ss.ItemId = i.ItemId where  AvailableQuantity >100 and storeid = ( select StoreId from PHRM_MST_Store where Name = 'MainDispensary')"
    # df = pd.read_sql(query, conn)
    # drug1BrandNameName = df.at[0, 'ItemName']
    # print("Drug Item Name:", drug1BrandNameName)
    # drugAvailableQuantity = df.at[0, 'AvailableQuantity']
    # print("Drug Available Quantity:", drugAvailableQuantity)
    # drugRate = df.at[0, 'MRP']
    # print("drug Rate:", drugRate)
    #
    # ########################################################
    #
    # drug1BrandName = drug1BrandNameName
    # drug1GenericName = "dfdfd"
    # drug1Rate = drugRate
    # drug2BrandName = 'ALCAL D 500 MG'
    # drug2BrandRate = 4.906
    # drug3BrandName = "Sinex tab"
    # drug4BrandName = "10 ML DIS.SYRINGE"
    # drug4BrandRate = 6.49
    # drug5BrandName = 'MONOTRATE-20MG TAB'
    # drug5BrandRate = 4.86
    # drugSinexName = 'tafco 250 mg'
    # drugSinexRate = 10.34
    # drugAasma = 'AASMA 150 XR TAB'
    # supplier = "AARATI MEDITCHA PVT"
    # drug1NarcoticName = "LOZ 1 MG"
    # drug1NarcoticRate = "2"
    # drugType = 'ABDOMINAL'
    # drugCompany = 'HIMALAYA'
    # dispensaryName1 = "MainDispensary"
    # dispensaryName2 = "Insurance Dispensary"
    # pharmacySupplierName1 = "AARATI MEDITCHA PVT"
    # ###TestAction>>Inventory+Procurement+SubStore:
    # inventoryName1 = "General Inventory"
    # inventoryName2 = "Medical Inventory"
    # subStoreName1 = "General"
    # subStoreName2 = "PostOps"
    # A4Paper = 'Paper A4'
    # PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
    # photocopypaperRate = 2300
    # storeItem1Name = "Tumb Pin"
    # storeItem1Rate = 10
    # # stationaryItem1 = "DOTPEN"
    # stationaryItem1 = "Sanitizer"
    # inventorySupplierName1 = "Shremad Tech."
    # salesCategoyType = "Pharmacy"
    #
    # ###TestAction>>ADT:
    # generalWard = "General"
    # bedFeature = "BED CHARGE (GENERAL WARD)"
    # admitWard = "Pediatric"
    # admitBed = "BED CHARGE (PAEDIATRIC WARD)"
    # ###TestAction>>Settings:
    # user = "admin"
    # doctorGyno = DoctorGyno
    # departmentGyno = DepartmentGyno
    # departmentNephro = doctorNephro
    # ###TestAction>>Accounting:
    # query = "select LedgerName from ACC_Ledger"
    # df = pd.read_sql(query, conn)
    # ledgerName1 = df.at[0, 'LedgerName']
    # print("ledger1 Name:", ledgerName1)
    # ledgerName2 = df.at[1, 'LedgerName']
    # print("ledger2 Name:", ledgerName2)
    #
    # Ledger_1 = ledgerName1
    # Ledger_2 = ledgerName2

###############################################################################
# Defining Variables for APF Hospital
###############################################################################
if appName == "APF":
    appURL = "http://172.16.30.62:107/"
    # TestAction>>LogIn:
    # admin user
    adminUserID = 'admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'admin'
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Admin admin'
    # IT user
    itUserID = 'admin'
    itUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'admin'
    pharmacyUserPwD = 'DanpheHIMS@123'
    # pharmacyUserName = 'Ms. Prekshya Adhikari'
    pharmacyUserName = 'Admin admin'
    # laboratory user
    labUserID = 'admin'
    labUserPwD = 'DanpheHIMS@123'
    # radiologist user
    radioUserID = 'admin'  # 'basudev'
    radioUserPwD = 'DanpheHIMS@123'
    # Inventory user
    storeUserID = 'admin'
    storeUserPwD = 'DanpheHIMS@123'

    # #################Test Action: DB Connection###########
    # import pyodbc
    # import pandas as pd
    #
    # conn = pyodbc.connect("Driver={SQL Server};"
    #                       "Server=DESKTOP-68UCKA5\SQLEXPRESS;"  # DESKTOP-68UCKA5\SQLEXPRESS
    #                       "Database=DanpheEMR_LIVE_APF_HOSPITAL;"  # TEST_LIVE_DanpheEMR_MMH_NewV2
    #                       "Trusted_Connection=yes;")
    #
    # ##### Getting Lab Test Data #####################
    # # query = "SELECT TOP(10) ItemName, Price FROM BIL_CFG_BillItemPrice where Price > 0 and IsActive = 1 and ServiceDepartmentId = (select ServiceDepartmentId from BIL_MST_ServiceDepartment where ServiceDepartmentName = 'biochemistry')"
    # ##TFT##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'TFT'"
    # df = pd.read_sql(query, conn)
    # print("df:", df)
    # nameTFT = df.at[0, 'ItemName']
    # print("TFT Name:", nameTFT)
    # rateTFT = df.at[0, 'Price']
    # print("TFT Rate:", rateTFT)
    #
    # ##CBC##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'CBC'"
    # df = pd.read_sql(query, conn)
    # nameCBC = df.at[0, 'ItemName']
    # print("CBC Name:", nameCBC)
    # rateCBC = df.at[0, 'Price']
    # print("CBC Rate:", rateCBC)
    #
    # ##T3##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'T3'"
    # df = pd.read_sql(query, conn)
    # nameT3 = df.at[0, 'ItemName']
    # print("T3 Name:", nameT3)
    # rateT3 = df.at[0, 'Price']
    # print("T3 Rate:", rateT3)
    #
    # ##T4##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'T4'"
    # df = pd.read_sql(query, conn)
    # nameT4 = df.at[0, 'ItemName']
    # print("T4 Name:", nameT4)
    # rateT4 = df.at[0, 'Price']
    # print("T4 Rate:", rateT4)
    #
    # ##TSH##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'TSH'"
    # df = pd.read_sql(query, conn)
    # nameTSH = df.at[0, 'ItemName']
    # print("TSH Name:", nameTSH)
    # rateTSH = df.at[0, 'Price']
    # print("TSH Rate:", rateTSH)
    #
    # ##LDH##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'LDH'"
    # df = pd.read_sql(query, conn)
    # nameLDH = df.at[0, 'ItemName']
    # print("LDH Name:", nameLDH)
    # rateLDH = df.at[0, 'Price']
    # print("LDH Rate:", rateLDH)
    #
    # ##Urine RE/ME##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'Urine RE/ME'"
    # df = pd.read_sql(query, conn)
    # nameUrineRE = df.at[0, 'ItemName']
    # print("Urine RE/ME Name:", nameUrineRE)
    # rateUrineRE = df.at[0, 'Price']
    # print("Urine RE/ME Rate:", rateUrineRE)
    #
    # ##BT##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'BT'"
    # df = pd.read_sql(query, conn)
    # nameBT = df.at[0, 'ItemName']
    # print("BT Name:", nameBT)
    # rateBT = df.at[0, 'Price']
    # print("BT Rate:", rateBT)
    #
    # ##CT##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'CT'"
    # df = pd.read_sql(query, conn)
    # nameCT = df.at[0, 'ItemName']
    # print("CT Name:", nameCT)
    # rateCT = df.at[0, 'Price']
    # print("CT Rate:", rateCT)
    #
    # ##### Getting Imaging Test Data #####################
    # ##USG##
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'USG'"
    # df = pd.read_sql(query, conn)
    # nameUSG = df.at[0, 'ItemName']
    # print("USG Name:", nameUSG)
    # rateUSG = df.at[0, 'Price']
    # print("USG Rate:", rateUSG)
    #
    # ##### Getting Other Billing Test Data #####################
    #
    # ##Billing Department Name##
    # query = "select DepartmentName from MST_Department where Description = 'Gynaecology Ward'"
    # df = pd.read_sql(query, conn)
    # DepartmentGyno = df.at[0, 'DepartmentName']
    # print("Gyno Department Name:", DepartmentGyno)
    #
    # ##Billing Doctor Name##
    # query = "select FirstName from EMP_Employee where DepartmentId = (select DepartmentId from MST_Department where Description = 'Gynaecology Ward')"
    # df = pd.read_sql(query, conn)
    # DoctorGyno = df.at[0, 'FirstName']
    # print("Gyno Doctor Name:", DoctorGyno)
    #
    # ########################################################
    #
    # ###TestAction>>BillingItems:
    # opdRate = 500
    # deposit = 200
    # CBC = nameCBC
    # # TFT = "TFT"   #TFT(FT3,FT4,TSH) CLLEA
    # TFT = nameTFT
    # T3 = nameT3
    # T4 = nameT4
    # TSH = nameTSH
    # # TFTRate = 1000
    # TFTRate = rateTFT
    # LDH = nameLDH
    # UrineRE = nameUrineRE
    # BT = nameBT
    # CT = nameCT
    # btRate = rateBT
    # ctRate = rateCT
    # # USG = "USG GUIDED DIAGNOSTIC PLEURAL TAPPING "
    # # usgRate = 1575
    # USG = nameUSG
    # usgRate = rateUSG
    # # admitRate = rateAdmission
    #
    # ###Getting discount name and scheme ###
    # query = "select MembershipTypeName, DiscountPercent, CommunityName from PAT_CFG_MembershipType where DiscountPercent > 0"
    # df = pd.read_sql(query, conn)
    # MembershipTypeName = df.at[0, 'MembershipTypeName']
    # print("MembershipTypeName:", MembershipTypeName)
    # DiscountPercent = df.at[0, 'DiscountPercent']
    # print("DiscountPercent:", DiscountPercent)
    # DiscountPercent = int(DiscountPercent)
    # print("DiscountPercent:", DiscountPercent)
    # CommunityName = df.at[0, 'CommunityName']
    # print("CommunityName:", CommunityName)
    # discountSchemeName = MembershipTypeName + " (" + str(DiscountPercent) + "%)"
    # print("discountSchemeName:", discountSchemeName)
    # discountCommunityName = CommunityName
    # discountSchemeName = discountSchemeName
    #
    # ###TestAction>>Pharmacy/Store+DispensaryItems:
    # ##### Getting Pharmacy Billing Test Data ##############
    # ##Drug Name and Rate##
    # query = "select i.ItemName, ss.AvailableQuantity, ss.MRP from PHRM_TXN_StoreStock ss inner join PHRM_MST_Item i on ss.ItemId = i.ItemId where  AvailableQuantity >100 and storeid = ( select StoreId from PHRM_MST_Store where Name = 'MainDispensary (Pharmacy)')"
    # df = pd.read_sql(query, conn)
    # drug1BrandNameName = df.at[0, 'ItemName']
    # print("Drug Item Name:", drug1BrandNameName)
    # drugAvailableQuantity = df.at[0, 'AvailableQuantity']
    # print("Drug Available Quantity:", drugAvailableQuantity)
    # drugRate = df.at[0, 'MRP']
    # print("drug Rate:", drugRate)
    #
    # ########################################################
    #
    # drug1BrandName = drug1BrandNameName
    # drug1GenericName = "dfdfd"
    # drug1Rate = drugRate
    # drug2BrandName = 'ALCAL D 500 MG'
    # drug2BrandRate = 4.906
    # drug3BrandName = "Sinex tab"
    # drug4BrandName = "10 ML DIS.SYRINGE"
    # drug4BrandRate = 6.49
    # drug5BrandName = 'MONOTRATE-20MG TAB'
    # drug5BrandRate = 4.86
    # drugSinexName = 'tafco 250 mg'
    # drugSinexRate = 10.34
    # drugAasma = 'AASMA 150 XR TAB'
    # supplier = "AARATI MEDITCHA PVT"
    # drug1NarcoticName = "LOZ 1 MG"
    # drug1NarcoticRate = "2"
    # drugType = 'ABDOMINAL'
    # drugCompany = 'HIMALAYA'
    # dispensaryName1 = "MainDispensary"
    # dispensaryName2 = "Insurance Dispensary"
    # pharmacySupplierName1 = "AARATI MEDITCHA PVT"
    # ###TestAction>>Inventory+Procurement+SubStore:
    # inventoryName1 = "General Inventory"
    # inventoryName2 = "Medical Inventory"
    # subStoreName1 = "General"
    # subStoreName2 = "PostOps"
    # A4Paper = 'Paper A4'
    # PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
    # photocopypaperRate = 2300
    # storeItem1Name = "Tumb Pin"
    # storeItem1Rate = 10
    # # stationaryItem1 = "DOTPEN"
    # stationaryItem1 = "Sanitizer"
    # inventorySupplierName1 = "Shremad Tech."
    # salesCategoyType = "Pharmacy"
    #
    # ###TestAction>>ADT:
    # generalWard = "General"
    # bedFeature = "BED CHARGE (GENERAL WARD)"
    # admitWard = "Pediatric"
    # admitBed = "BED CHARGE (PAEDIATRIC WARD)"
    # ###TestAction>>Settings:
    # user = "admin"
    # doctorGyno = DoctorGyno
    # departmentGyno = DepartmentGyno
    # # departmentNephro = doctorNephro
    # ###TestAction>>Accounting:
    # query = "select LedgerName from ACC_Ledger"
    # df = pd.read_sql(query, conn)
    # ledgerName1 = df.at[0, 'LedgerName']
    # print("ledger1 Name:", ledgerName1)
    # ledgerName2 = df.at[1, 'LedgerName']
    # print("ledger2 Name:", ledgerName2)
    #
    # Ledger_1 = ledgerName1
    # Ledger_2 = ledgerName2

###############################################################################
# This Section is used for Defining Variables for Charak
###############################################################################

if appName == "Charak":

    # appURL = "http://172.16.30.129:108/"
    appURL = "http://202.51.74.168:85/"
    # Login Credentials :
    # admin user
    adminUserID = 'Admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'Admin'  # 'sabitri'
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Mr. admin admin'  # 'Ms. Sabitri Sharma Adhikari'
    # IT user
    itUserID = 'Admin'  # 'rn'
    itUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'Admin'  # 'shivraj'
    pharmacyUserPwD = 'DanpheHIMS@123'
    pharmacyUserName = 'admin admin'  # 'shiv raj'
    # laboratory user
    labUserID = 'Admin'
    labUserPwD = 'DanpheHIMS@123'
    # Radiology user
    radioUserID = 'Admin'
    radioUserPwD = 'DanpheHIMS@123'
    # Inventory user
    storeUserID = 'Admin'
    storeUserPwD = 'DanpheHIMS@123'
    # Medical Record user
    MRUserID = 'Admin'  # 'haris'
    MRUserPwD = 'DanpheHIMS@123'

    # TestAction>>BillingItems:
    opdRate = 850
    deposit = 200
    CBC = "CBC(HB,PCV,RBC,WBC,TC,DC,PLT,MCV"
    TFT = "TC,DC"  # TFT(FT3,FT4,TSH) CLLEA
    T3 = "RETICS"
    T4 = "E"
    TSH = "HB"
    TFTRate = 200
    LDH = "LDH"
    UrineRE = "URINE R/E,M/E"  # this gets changed on V1.49.3
    BTCT = "BT/CT"
    btctRate = 200
    USG = "USG ABDOMEIN/PELVIS WITH OBS"
    usgRate = 2000
    admitRate = 2000
    discountCommunityName = "Hospital"
    discountSchemeName = "Staff Family (30%)"
    DiscountPercent = 10
    ReferredBy = "Dr. Kovid Nepal"

    # TestAction>>Pharmacy/Store+DispensaryItems:
    drug1BrandName = "SINEX TAB"
    drug1GenericName = "PARACETAMOL"
    drug1Rate = 3
    drug1CostPrice = 2
    drug2BrandName = 'ASTHALIN ROTACAPS '
    drug2BrandRate = 69.18
    drug3BrandName = "PANTOP-40MG TAB "
    drug4BrandName = "10ML SYRINGE "
    drug4BrandRate = 10
    drug5BrandName = 'MONOTRATE-20MG '
    drug5BrandRate = 5.34
    drugSinexName = 'SINEX TAB'
    drugSinexRate = 3
    drugAasma = 'AASMA XR-150MG '
    drug1NarcoticName = "MORFIUM-10MG/1ML INJ."
    drug1NarcoticRate = 100
    drugType = 'SURGICALS'
    drugCompany = 'HIMALAYANS'
    dispensaryName1 = "MainDispensary"
    dispensaryName2 = "Insurance Dispensary"
    pharmacySupplierName1 = "Diya Traders"
    supplier = "srijan traders"

    # TestAction>>Inventory+Procurement+SubStore:
    inventoryName1 = "General Inventory"
    inventoryName2 = "Medical Inventory"
    subStoreName1 = "Accounting Store"
    subStoreName2 = "Administration Store"
    A4Paper = 'PHOTOCOPY PAPER A4'
    storeItem1Name = 'PHOTOCOPY PAPER A4'
    storeItem2Name = 'USG PAPER'
    PhotocopyPaper = 'PHOTOCOPY PAPER A4'
    photocopypaperRate = 240
    stationaryItem1 = "PENCIL"
    stationaryItem2 = "PILOT PEN"
    File = "PATIENT RECORD FILE"
    SubStore1 = "Billing Store"
    SubStore2 = "Lab Store"
    inventorySupplierName1 = "Charak Hospital Vendor"
    salesCategoyType = "Pharmacy Unit"

    # TestAction>>ADT:
    generalWard = "General"
    GeneralWard = "ICU"
    bedFeature = "General"
    admitWard = "General"
    admitBed = "General"

    # TestAction>>Settings:
    user = "admin"
    doctorGyno = "Dr. Bishnu Palikhe"
    departmentGyno = "Gynecology"
    departmentNephro = "Nephrology"
    doctor2 = "Dr. Juju Raj Shrestha"

    # Dispensary Credit Organization
    creditOrganization = "Prabhu Insurance"

    # TestAction>>Accounting:
    Ledger_1 = "SUNITA GURUNG "
    Ledger_2 = "CASH ON HAND"

    # Medical Record Diagnosis
    dianosis1 = "Measles"
    dianosis2 = "Diptheria"

    # # Test Action: DB Connection
    # import pyodbc
    # import pandas as pd
    #
    # conn = pyodbc.connect("Driver={SQL Server};"
    #                       "Server=DESKTOP-68UCKA5\SQLEXPRESS;"  # DESKTOP-68UCKA5\SQLEXPRESS
    #                       "Database=DanpheHIMS_Charak_MergeVersion;"  # TEST_LIVE_DanpheEMR_MMH_NewV2
    #                       "Trusted_Connection=yes;")
    #
    # # Getting Lab Test Data
    # # query = "SELECT TOP(10) ItemName, Price FROM BIL_CFG_BillItemPrice where Price > 0 and IsActive = 1 and ServiceDepartmentId = (select ServiceDepartmentId from BIL_MST_ServiceDepartment where ServiceDepartmentName = 'biochemistry')"
    # # TFT
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'TFT'"
    # df = pd.read_sql(query, conn)
    # print("df:", df)
    # nameTFT = df.at[0, 'ItemName']
    # print("TFT Name:", nameTFT)
    # rateTFT = df.at[0, 'Price']
    # print("TFT Rate:", rateTFT)
    #
    # # CBC
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'CBC'"
    # df = pd.read_sql(query, conn)
    # nameCBC = df.at[0, 'ItemName']
    # print("CBC Name:", nameCBC)
    # rateCBC = df.at[0, 'Price']
    # print("CBC Rate:", rateCBC)
    #
    # # T3
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'T3'"
    # df = pd.read_sql(query, conn)
    # nameT3 = df.at[0, 'ItemName']
    # print("T3 Name:", nameT3)
    # rateT3 = df.at[0, 'Price']
    # print("T3 Rate:", rateT3)
    #
    # # T4
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'T4'"
    # df = pd.read_sql(query, conn)
    # nameT4 = df.at[0, 'ItemName']
    # print("T4 Name:", nameT4)
    # rateT4 = df.at[0, 'Price']
    # print("T4 Rate:", rateT4)
    #
    # # TSH
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'TSH'"
    # df = pd.read_sql(query, conn)
    # nameTSH = df.at[0, 'ItemName']
    # print("TSH Name:", nameTSH)
    # rateTSH = df.at[0, 'Price']
    # print("TSH Rate:", rateTSH)
    #
    # # LDH
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'LDH'"
    # df = pd.read_sql(query, conn)
    # nameLDH = df.at[0, 'ItemName']
    # print("LDH Name:", nameLDH)
    # rateLDH = df.at[0, 'Price']
    # print("LDH Rate:", rateLDH)
    #
    # # Urine RE/ME
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'Urine RE/ME'"
    # df = pd.read_sql(query, conn)
    # nameUrineRE = df.at[0, 'ItemName']
    # print("Urine RE/ME Name:", nameUrineRE)
    # rateUrineRE = df.at[0, 'Price']
    # print("Urine RE/ME Rate:", rateUrineRE)
    #
    # # BT
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'BT'"
    # df = pd.read_sql(query, conn)
    # nameBT = df.at[0, 'ItemName']
    # print("BT Name:", nameBT)
    # rateBT = df.at[0, 'Price']
    # print("BT Rate:", rateBT)
    #
    # # CT
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'BT'"
    # df = pd.read_sql(query, conn)
    # nameCT = df.at[0, 'ItemName']
    # print("CT Name:", nameCT)
    # rateCT = df.at[0, 'Price']
    # print("CT Rate:", rateCT)
    #
    # # Getting Imaging Test Data
    # # USG
    # query = "select ItemName, Price from BIL_CFG_BillItemPrice where Description = 'USG'"
    # df = pd.read_sql(query, conn)
    # nameUSG = df.at[0, 'ItemName']
    # print("USG Name:", nameUSG)
    # rateUSG = df.at[0, 'Price']
    # print("USG Rate:", rateUSG)
    #
    # # Getting Other Billing Test Data
    #
    # # Billing Department Name
    # query = "select DepartmentName from MST_Department where Description = 'Gynaecology Ward'"
    # df = pd.read_sql(query, conn)
    # DepartmentGyno = df.at[0, 'DepartmentName']
    # print("Gyno Department Name:", DepartmentGyno)
    #
    # # Billing Doctor Name
    # query = "select FirstName from EMP_Employee where DepartmentId = (select DepartmentId from MST_Department where Description = 'Gynaecology Ward')"
    # df = pd.read_sql(query, conn)
    # DoctorGyno = df.at[0, 'FirstName']
    # print("Gyno Doctor Name:", DoctorGyno)
    #
    # ########################################################
    #
    # # TestAction>>BillingItems:
    # opdRate = 500
    # deposit = 200
    # CBC = nameCBC
    # # TFT = "TFT"   #TFT(FT3,FT4,TSH) CLLEA
    # TFT = nameTFT
    # T3 = nameT3
    # T4 = nameT4
    # TSH = nameTSH
    # # TFTRate = 1000
    # TFTRate = rateTFT
    # LDH = nameLDH
    # UrineRE = nameUrineRE
    # BT = nameBT
    # CT = nameCT
    # btRate = rateBT
    # ctRate = rateCT
    # # USG = "USG GUIDED DIAGNOSTIC PLEURAL TAPPING "
    # # usgRate = 1575
    # USG = nameUSG
    # usgRate = rateUSG
    # # admitRate = rateAdmission
    #
    # # Getting discount name and scheme
    # query = "select MembershipTypeName, DiscountPercent, CommunityName from PAT_CFG_MembershipType where DiscountPercent > 0"
    # df = pd.read_sql(query, conn)
    # MembershipTypeName = df.at[0, 'MembershipTypeName']
    # print("MembershipTypeName:", MembershipTypeName)
    # DiscountPercent = df.at[0, 'DiscountPercent']
    # print("DiscountPercent:", DiscountPercent)
    # DiscountPercent = int(DiscountPercent)
    # print("DiscountPercent:", DiscountPercent)
    # CommunityName = df.at[0, 'CommunityName']
    # print("CommunityName:", CommunityName)
    # discountSchemeName = MembershipTypeName + " (" + str(DiscountPercent) + "%)"
    # print("discountSchemeName:", discountSchemeName)
    # discountCommunityName = CommunityName
    # discountSchemeName = discountSchemeName
    #
    # # TestAction>>Inventory+Procurement+SubStore:
    # inventoryName1 = "General Inventory"
    # inventoryName2 = "Medical Inventory"
    # subStoreName1 = "General"
    # subStoreName2 = "PostOps"
    # A4Paper = 'Paper A4'
    # PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
    # photocopypaperRate = 2300
    # storeItem1Name = "Tumb Pin"
    # storeItem1Rate = 10
    # # stationaryItem1 = "DOTPEN"
    # stationaryItem1 = "Sanitizer"
    # inventorySupplierName1 = "Shremad Tech."
    # salesCategoyType = "Pharmacy"
    #
    # # TestAction>>ADT:
    # generalWard = "General"
    # bedFeature = "BED CHARGE (GENERAL WARD)"
    # admitWard = "Pediatric"
    # admitBed = "BED CHARGE (PAEDIATRIC WARD)"
    # # TestAction>>Settings:
    # user = "admin"
    # doctorGyno = DoctorGyno
    # departmentGyno = DepartmentGyno
    # # departmentNephro = doctorNephro
    # # TestAction>>Accounting:
    # query = "select LedgerName from ACC_Ledger"
    # df = pd.read_sql(query, conn)
    # ledgerName1 = df.at[0, 'LedgerName']
    # print("ledger1 Name:", ledgerName1)
    # ledgerName2 = df.at[1, 'LedgerName']
    # print("ledger2 Name:", ledgerName2)
    #
    # Ledger_1 = ledgerName1
    # Ledger_2 = ledgerName2

###############################################################################
# Matrika Eye Center
###############################################################################
if appName == "matrika":
    appURL = "http://202.51.74.168:220/"
    # TestAction>>LogIn:
    # admin user
    adminUserID = 'Admin'
    adminUserPwD = 'DanpheHIMS@123'  # '28A7hi0jvH0='
    # billing user
    foUserID = 'Admin'  # 'sabitri'
    foUserPwD = 'DanpheHIMS@123'
    foUserName = 'Mr. admin admin'  # 'Ms. Sabitri Sharma Adhikari'
    # IT user
    itUserID = 'Admin'  # 'rn'
    itUserPwD = 'DanpheHIMS@123'
    # pharmacy user
    pharmacyUserID = 'Admin'  # 'shivraj'
    pharmacyUserPwD = 'DanpheHIMS@123'
    pharmacyUserName = 'admin admin'  # 'shiv raj'
    # laboratory user
    labUserID = 'Admin'
    labUserPwD = 'DanpheHIMS@123'
    # Radiology user
    radioUserID = 'Admin'
    radioUserPwD = 'DanpheHIMS@123'
    # Inventory user
    storeUserID = 'Admin'
    storeUserPwD = 'DanpheHIMS@123'
    # Medical Record user
    MRUserID = 'Admin'  # 'haris'
    MRUserPwD = 'DanpheHIMS@123'
    # TestAction>>BillingItems:
    opdRate = 350
    deposit = 200
    CBC = "A scan"
    TFT = "Yag Capsulotomy"  # TFT(FT3,FT4,TSH) CLLEA
    TFTRate = 1500
    LDH = "LDH"
    UrineRE = "TRIA"  # this gets changed on V1.49.3
    BTCT = "B-SCAN"
    btctRate = 500
    USG = "BANDAGE CONTACT LENS"
    usgRate = 1000
    admitRate = 1500
    discountCommunityName = "Hospital"
    discountSchemeName = "Referal (10%)"
    DiscountPercent = 10
    ReferredBy = ""

    # TestAction>>Pharmacy/Store+DispensaryItems:

    drug1BrandName = "SINEX TAB"
    drug1GenericName = "PARACETAMOL"
    drug1Rate = 3
    drug1CostPrice = 2
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

    # TestAction>>Inventory+Procurement+SubStore:

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

    # TestAction>>ADT:
    generalWard = "General Ward"
    GeneralWard = "ICU"
    bedFeature = "BED CHARGE General Ward"
    admitWard = "Pediatric Ward"
    admitBed = "Pediatric Bed Charge"

    # TestAction>>Settings:
    user = "admin"
    doctorGyno = "Dr. Ben Limbu"
    departmentGyno = "OPHTHALMOLOGY"
    departmentNephro = "OPHTHALMOLOGY"

    # Dispensary Credit Organization
    creditOrganization = "Arogin Care Home"

# def __str__():
#  return
