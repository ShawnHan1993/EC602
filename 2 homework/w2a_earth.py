# -*- coding: utf-8 -*-
# AUTHOR Shen Han shawnhan@bu.edu
# AUTHOR Changlong Jiang cljiang@bu.edu
# AUTHOR Xinyu Li lxinyu@bu.edu
def giveElectonNum(radio,ifNoNeutron=0):#radio is No
    mEarth=5.9736*(10**24)
    mP=1.6726*(10**(-27))
    if ifNoNeutron==1:
        return mEarth/mP
    else:        
        protonRadio=1/(1/radio+1)
        return (mEarth*protonRadio)/mP

estimatedBoundRadio=0.95
lowerBoundRadio=0.87
upperBoundRadto=1

print(giveElectonNum(estimatedBoundRadio)/(2**43))
print(giveElectonNum(lowerBoundRadio)/(2**43))
print(giveElectonNum(upperBoundRadto)/(2**43))