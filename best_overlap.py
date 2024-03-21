import numpy as np
from scipy.optimize import minimize

def best_overlap(new_fit,D2,a,step_x,E_1,a2):

    def optimize(params):
        LS=0
        x, y = params
        k=int(a2/a)
        B[:, 1] = np.roll(new_fit[:, 1], round(x), 0)
        A[:,:]=B[::k]

        for n in range(a):
            if ((D2[n, 0] > (E_1 - 6)) and (D2[n, 0] < (E_1 + 0.5))):
                curve = y * A[((n)), 1]
                LS+=(D2[n, 1] - curve) ** 2
        return LS

    B = np.zeros((a2, 2))
    A = np.zeros((a, 2))

    k=int(a2/a)
    initial_guess=[1,1]

    result=minimize(optimize, initial_guess,method='Nelder-Mead', bounds=([-50,50],[0.25,(1.0+0.5)]),
                    options={'maxiter':2000,'xatol': 1e-8, 'disp': False})

    if result.success:
        fitted_params = result.x

    else:
        print('not enough iterations')

    x_PC, y_PC=fitted_params
    chi_final=chi(fitted_params)

    new_fit[:, 1] = np.roll(new_fit[:, 1], round(x_PC), 0)
    NEW = np.zeros((a, 4))
    NEW[:,[0,1]]=new_fit[::k,:]

    for p in range(a):
        NEW[p,1]=y_PC*NEW[p,1]

    NEW=np.append(NEW,[[(E_1+x_PC*step_x/k),0,0,0]],axis=0)
    NEW = np.append(NEW, [[round(x_PC),y_PC,chi_final,0]], axis=0)

    return NEW