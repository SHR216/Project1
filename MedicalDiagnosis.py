#import numpy
#import numpy as np
#!/usr/bin/env python
# coding: utf-8

# In[4]:


Symptoms = ["None", "Fever", "Pain in Abdomen especially ILIAC FOSSA", "vomiting", "Cough",
            "Pain in chest","Nausea","Feeling weak","Jaundice","Digestion Disorder",
            "Dark Urine","Pain in right side of Abdomen","Fatigue","Loss of appetite",
            "Bleeding easily","Bruising Easily","Itchy Skin","Joint Pain","Blood in the urine",
            "Hoarseness","Persistent lumps or swollen glands", "Obvious change in a wart or a mole",
            "Indigestion or difficulty swallowing","Unexpected weight loss/night sweats or fever",
            "Difficulty In Breathing/Shortness of Breath","Chest pain or pressure","loss of speech or movement",
            "Loss of taste or smell","Sore throat",
            "Headaches, which may be severe and worsen with activity or in the early morning","Seizures",
            "Personality or memory changes","Drowsiness","Sleep problems","Memory problems" ]

Test = ["None", "Blood CP with ESR... TLC (Total leucocyte count) will be high", 
        "DLC (Differential leucocyte count) Neutrophils will be high", "ESR high",
        "X-ray chest: pneumonic patch (sometimes)", "Examine throat: (Red enlarged tonsils, pus in tonsils)",
        "Blood Samples with more than one kind of hepatitis virus",
        "Abnormal blood cells"]
Treatment = ["None", "Surgery", "Antibiotics", 
             "anti-allergic, paracetamol. If not gone, Add antibiotics orally. If not gone and Add antibiotics IV",
             "AntiViral Medications\n","Chemotherapy\n",
             "you should rest, drink plenty of fluid, and eat nutritious food. Stay in a separate room from other family members\n",
             "surgery\n"]
Disease = ["None", "Acute appendicitis", "Pneumonia", "Acute Tonsilitis", "Hepatitis","Cancer",
           "Covid-19" ,"Brain Tumor","\n\n**Unable To Diagnose**",]

print("\t\t\t\t Welcome to Medical Diagnosis System\n ****************************************************************************************************************************** \n In order to diagnose your disease you have to Enter the symptoms and t
