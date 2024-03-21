from math import *
import numpy as np
from numba import njit


@njit
def PC_curve(E1,C,F_g,F_l,KE_start,KE_stop,a2):
    m=(F_g/(F_g+F_l))
    m_corr=0.082841*m+2.2*(m**2)-1.2828*(m**3) #corrected m factor

    #this is in Igor software;
    if m_corr<0:
        m_corr=0
    elif m_corr>1:
        m_corr=1

    F=(1-1.1287*m+1.8987*(m**2)-0.77*(m**3))*(F_g+F_l)
    E2=E1+2
    E3=E1-3.55
    E_step_1= 0.01643363728470091
    h1=0.75*C[0,1]

    h2=h1/2
    h3=h1/1.6

    KE=np.linspace(KE_start,KE_stop,a2)

    #C-O peak
    curve_1=np.zeros((a2,1)) #curve for peak C-O
    j=0

    for i in KE: #C-O peak
        #i is then the KE energies; energies at which the spectrum was measured

        I_x=h1*m_corr*exp(-2.7726*((i-E1)**2)/(F**2))+(1-m_corr)*h1/(1+4*(i-E1)**2/(F**2))
        curve_1[j]=I_x
        j+=1

    #C-H peak
    curve_2 = np.zeros((a2, 1))  # curve for peak C-H
    j = 0
    for i in KE:
        # i is then the KE energies; energies at which the spectrum was measured

        I_x = h2* m_corr * exp(-2.7726 * ((i - E2) ** 2) / (F ** 2)) + (1 - m_corr) * h2 / (1 + 4 * (i - E2) ** 2 / (F ** 2))
        curve_2[j] = I_x
        j += 1

    #C=O peak
    curve_3 = np.zeros((a2, 1))  # curve for peak C-O
    j = 0
    for i in KE:
        # i is then the KE energies; energies at which the spectrum was measured

        I_x = h3* m_corr * exp(-2.7726 * ((i - E3) ** 2 )/ (F ** 2)) + (1 - m_corr) * h3 /(1 + 4 * (i - E3) ** 2 / (F ** 2))
        curve_3[j] = I_x
        j += 1

    curve=np.zeros((a2,1))

    for i in range(len(curve_1)):
        curve[i]=curve_1[i]+curve_2[i]+curve_3[i]

    #print(len(curve))

    return curve

#do I even need this as a separate function??
