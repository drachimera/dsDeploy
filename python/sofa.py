import pandas as pd


# Inputs: PaO2/FiO2 in mmHg and whether mechanically ventilated
# Output: Respiratory system SOFA score

def resp_system(pao_fio = None, vent=False):
    if pao_fio:
        if vent and pao_fio < 100:
            return 4
        elif vent and pao_fio < 200:
            return 3
        elif pao_fio < 300:
            return 2
        elif pao_fio < 400:
            return 1
        else:
            return 0
    else:
        return 0


# Inputs: Glasgow coma score (integer)
# Output: Nervous system SOFA score

def nerve_system(glasgow = None):
    
    if type(glasgow) is int:
    
        if glasgow < 6:
            return 4
        elif glasgow in xrange(6,9):
            return 3
        elif glasgow in xrange(10,13):
            return 2
        elif glasgow in xrange(13,15):
            return 1
        else:
            return 0
    else:
        return 0


# Inputs: Mean Arterial Pressure (mm/Hg), dopamine (micrograms/kg/min), dobutamine (any dose), 
# epinephrine (micrograms/kg/min), norepinephrine (micrograms/kg/min) floats
# Output: Cardiovascular system SOFA score

def card_system(MAP = None, dopamine = None, dobutamine = None, epinephrine = None, norepinephrine = None):
    if MAP and MAP < 70:
        return 1
    elif (dopamine and dopamine <= 5) or (dobutamine):
        return 2
    elif (dopamine and dopamine > 5) or (epinephrine and epinephrine <= 0.1) or (norepinephrine and norepinephrine <= 0.1):
        return 3
    elif (dopamine and dopamine > 15) or (epinephrine and epinephrine > 0.1) or (norepinephrine and norepinephrine > 0.1):
        return 4
    else:
        return 0


# Inputs: Bilirubin (mg/dl) float
# Output: Liver SOFA score

def liver(bilirubin = None):
    
    if type(bilirubin) in [float, int]:
        bilirubin = round(bilirubin,1)
    
        if bilirubin > 12.0:
            return 4
        elif 6 <= bilirubin <= 11.9:
            return 3
        elif 2 <= bilirubin <= 5.9:
            return 2
        elif 1.2 <= bilirubin <= 1.9:
            return 1
        else: 
            return 0
    else:
        return 0


# Inputs: Platelets x 10^3/microliters integer
# Output: Coagulation SOFA score

def coagulation(platelets = None):
    if type(platelets) is int:
        if platelets < 20:
            return 4
        elif platelets < 50:
            return 3
        elif platelets < 100:
            return 2
        elif platelets < 150:
            return 1
        else:
            return 0
    else:
        return 0


# Inputs: Creatinine (mg/dl) float
# Output: Kidney SOFA score

def kidneys(creatinine = None):
    
    if type(creatinine) in [int, float]:
        
        creatinine = round(creatinine,1)
    
        if creatinine > 5.0:
            return 4
        elif 3.5 <= creatinine <= 4.9:
            return 3
        elif 2 <= creatinine <= 3.4:
            return 2
        elif 1.2 <= creatinine <= 1.9:
            return 1
        else: 
            return 0
    else:
        return 0


#Inputs: PaO2/FiO2 in mmHg and whether mechanically ventilated
# Glasgow coma score (integer)
# Mean Arterial Pressure (mm/Hg), dopamine (micrograms/kg/min), dobutamine (any dose), 
# epinephrine (micrograms/kg/min), norepinephrine (micrograms/kg/min) floats
# Bilirubin (mg/dl) float
# Platelets x 10^3/microliters integer
# Creatinine (mg/dl) float
#Output: SOFA score

def sofa(pao_fio = None, vent = False, glasgow = None, 
         MAP = None, dopamine = None, dobutamine = None, 
         epinephrine = None, norepinephrine = None,
         bilirubin = None, platelets = None, creatinine = None):
    
    return resp_system(pao_fio, vent) + nerve_system(glasgow) +            card_system(MAP, dopamine, epinephrine, norepinephrine) +            liver(bilirubin) + coagulation(platelets) + kidneys(creatinine)






