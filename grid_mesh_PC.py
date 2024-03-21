import numpy as np

def grid_mesh(D2,peaks_2,C,a,a2):
#nr_steps determines the grid mesh resolution
    Nr_steps_x=80 #this could probably be less
    Nr_steps_y=30
    step_x_array=np.linspace(-(Nr_steps_x//2),(Nr_steps_x//2),Nr_steps_x)
    step_y_array=np.linspace(1.2,0.4,Nr_steps_y)

    saved_par=np.zeros(((Nr_steps_x*Nr_steps_y),3))
    #C=O peak interval weight
    weight_1=5
    #C-O peak interval weight
    weight_2=1
    #weight 1 and 2 determine how is the match between the experimental and the reference spectrum evaluated
    u=0
    Q = np.zeros((a2, 2))
    Q[:,0]=peaks_2[:,0]
    W=np.zeros((a,2))
    k=int(a2/a)

    for x in step_x_array:
        x=round(x) #rounding x means we only use integer values of x which is not ok
        Q[:, 1] = np.roll(peaks_2[:, 1], x, 0)
        W[:,:]=Q[::k,:]

        for y in step_y_array:
            LS=0
            for i in range(a):
                if (D2[(i),0]>(C[0,0]-5) and (D2[(i),0]<C[0,0]-0.5)):
                    LS+=weight_1*(D2[(i),1]-y*W[(i),1])**2
                elif (D2[(i),0]>(C[0,0]-0.5) and D2[(i),0]<(C[0,0]+0.3)):
                    LS+=weight_2*(D2[i,1]-y*W[(i),1])**2
                elif (D2[(i),0]>(C[0,0]+2.8) and D2[(i),0]<(C[0,0]+3.5)):
                    LS+=(weight_2*(D2[i,1]-y*W[(i),1])**2)

            saved_par[u,:]=[x,y,LS]
            u+=1

    min_chi=min(saved_par[:,2])
    for i in range((Nr_steps_x*Nr_steps_y)):
        if saved_par[i,2]==min_chi:
            x1,y1=saved_par[i,[0,1]]

    new_fit=np.zeros((a2,2))

    x1_steps=round(x1) #how many steps deviation
    new_fit[:,0]=peaks_2[:,0]
    new_fit[:,1]=np.roll(peaks_2[:,1],(x1_steps),0)

    for p in range(a):
        new_fit[p,1]=y1*new_fit[p,1]

    new_fit=np.append(new_fit,[[x1_steps,x1]],axis=0)
    return new_fit

