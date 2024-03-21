import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from reference_PC_spectrum import *
from grid_mesh_PC import *
from best_overlap import *
import time
import os

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

#directory with several files (each file has one series of C 1s spectra)
path_dir_input: str= r"C:..."
file_list=os.listdir(path_dir_input)

for i in range(len(file_list)):
    filename=file_list[i]
    path_file_input = os.sep.join([path_dir_input, filename])

    #output directory
    path_dir_output: str = r"C:..."
    output_name_1=filename.removesuffix('converted.txt')
    subdirectory=output_name_1+ 'fit'
    path_file_output2 = os.sep.join([path_dir_output, subdirectory])

    #check if file exists
    check=0
    while check<1:
        if os.path.exists(path_file_output2):
            subdirectory=subdirectory+'1'
            path_file_output2=os.sep.join([path_dir_output, subdirectory])
        else:
            check=1

    os.makedirs(path_file_output2, exist_ok = True) #no error if directory already exists
    #names for the ouput files
    fit_par=output_name_1+'fit_par'+'.txt'
    fit_par_location=os.sep.join([path_file_output2, fit_par])

    D=np.genfromtxt(path_file_input,skip_header=1)
    nr_scans=(D.shape[1])
    print(D.shape[1], 'number of spectra')

    e=1
    xy=nr_scans
    PC_shift=np.zeros(((xy-e),2))
    PC_shift2=np.zeros(((xy-e),2))
    final_fit_parameters=np.zeros(((xy-e),4))
    b1=0

    for c in range(e,(xy)):

    # STEP 2: FIND THE 2 MAXIMA (i.e. find the approximate position of the C-O and C-C peak)
        st=time.time()
        print(c,'scan number c')
        D2=D[:,[0,c]]

    #interval for finding maximum points
        a=len(D2[:,0]) #nr of columns
    #offset of BE before starting to fit
        d=9  #slice up the KE range; arbitrarily chosen (best for my spectra)
        b=a//d #divide into intervals; interval approx 1.6 eV
    #energy step (kinetic energy resolution of the experimental data must be provided
        E_step= 0.061840796

        E=np.zeros(((d+1),3)) #empty array for maxima in each interval
        for i in range((d+1)):
            # the last interval is what is left over of the slicing; all in this if loop
            if i==d:
                h=D2[((i)*b):(a),[0,1]]
                E[d,1]=max(h[:,1])
                for j in range(len(h[:, 1])):
                    if h[j, 1] == E[d, 1]:
                        E[d, 0] = h[j, 0]
                        loc_a=np.where(abs(D2[:, 0]-h[j, 0])<0.012)
                        #we find the coordinate of the item with interval maximum
                        sum1=sum(D2[(int(loc_a[0]) - 5):(int(loc_a[0]) + 5), 1])
                        E[i,2]=sum1
                        #sum of intensity +- 5 points around the maximum point
                        continue
                        #E contains maxima of all intervals in column [1]

            h=D2[(i*b):((i+1)*b),[0,1]] #creating h is just to keep a better track

            E[i,1]=max(h[:,1]) #find max in each of the intervals
            #determine KE for the max
            for j in range(len(h[:,1])):
                if h[j,1]==E[i,1]:
                    E[i,0]=h[j,0]
                    loc_a = np.where(abs(D2[:, 0]-h[j, 0])<0.012)
                    sum1 = sum(D2[(int(loc_a[0]) - 5):(int(loc_a[0]) + 5), 1])
                    E[i, 2] = sum1

        B = np.zeros(((d - 1), 2))
        C = np.zeros((2, 2))
        #sort the items from largest to smallest based on the SUM of intensities at kinetic energy +- 5 around the intensity maximum
        ind3=np.argsort(E[:,2],axis=0)

        #ind matrix numbers elements in E[:,1] from smallest to largest
        #all columns are sorted in the order determined in ind3
        E[:,0]=np.take_along_axis(E[:,0],ind3,axis=-1)
        E[:,1]=np.take_along_axis(E[:,1],ind3,axis=-1)
        E[:,2]=np.take_along_axis(E[:,2],ind3,axis=-1)

        length=4
        EX=E[-length:,:]
        #if the two points with the highest sum are in the right range of each other, use this
        if abs(EX[-1, 0] - EX[-2, 0])<2.4 and abs(EX[-1, 0] - EX[-2, 0])>1.6:
            C[0,:], C[1,:]=EX[-1,[0,1]],EX[-2,[0,1]]

        #the else clause below is only necessary for fairly noisy data; it contains several 'safety' precautions to prevent
        #making large errors in the initial guess for C-O and C-C peak position on KE axis
        else:
            size=factorial(length)/(factorial(length-2))
            inter_distance=np.zeros((int(size),3))
            switch=0
            v2=0
            for i in range(length):
                for j in range(length):
                    if i!=j:
                        #find all interdistances (for all permutations)
                        inter_distance[v2, :] = [i, j, abs(EX[i, 0] - EX[j, 0])]
                        v2+=1

    #val contains coordinates of the pair that work well (are at the right distance)
            val = [0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0]
            tx=0
            for i in range(len(inter_distance[:,1])):
                if (inter_distance[i,2]<2.3 and inter_distance[i,2]>1.5):
                    tx+=1
                    val[tx]=i
                    C[0,:], C[1,:]=EX[int(inter_distance[i,0]),[0,1]], EX[int(inter_distance[(i),1]),[0,1]]
                    switch=1
                #the last pair in inter_distance that satisfies this condition is saved...

#interval of the 'accepted' distance between the two points/maxima is enlarged for every subsequent if clause
            if switch<1:
                for i in range(len(inter_distance[:,1])):
                    if (inter_distance[i, 2] < 2.4 and inter_distance[i, 2] > 1.5):
                        tx += 1
                        val[tx] = i
                        C[0, :], C[1, :] = EX[int(inter_distance[i, 0]), [0, 1]], EX[int(inter_distance[(i), 1]), [0, 1]]
                        switch = 1

            if switch < 1:
                for i in range(len(inter_distance[:,1])):
                    if (inter_distance[i, 2] < 2.6 and inter_distance[i, 2] > 1.3):
                        tx += 1
                        val[tx] = i
                        C[0, :], C[1, :] = EX[int(inter_distance[i, 0]), [0, 1]], EX[int(inter_distance[(i), 1]), [0, 1]]
                        switch = 1

    #C matrix has a specific order; the first position is the KE and the intensity of the C-O peak, the second is the C-C peak
    #this order is ensured with the 2 lines below
        if C[0, 0] > C[1, 0]:
            C = np.flipud(C)

        #STEP 3: BACKGROUND CORRECTION (linear background assumes)
        sum_left_BG=0
        q=0

        #step 1: find average intensity on the right side of the PC spectrum (at higher KE values)
        point4=a
        #find avg on the left
        klm=0
        point3=0
        for i in range(a):
            if klm!=0:
                break

        #change the interval span (i.e. adjust 1.7 to some other number) when changing the spectrum center
            if (D2[i,0]>(C[1,0]+1.7)):
                point3=i
                klm=1

        #just in case point3 is not found (so that the code does not stop...)
        if point3==0:
            point3=a-50

        D_reshaped_x=np.reshape(D2[point3:point4,0],(-1,1))
        D_reshaped_y=np.reshape(D2[point3:point4,1],(-1,1))
        BG_fit = LinearRegression().fit(D_reshaped_x, D_reshaped_y)
        BG_linear=BG_fit.predict(D_reshaped_x)
        n1=BG_fit.intercept_
        k1=BG_fit.coef_
        D_predict=BG_fit.predict(D_reshaped_x)
        x1=D2[point3,0]
        y1=x1*k1+n1
        #the code takes some interval on the right of the spectrum (where we are sure that there are no more peaks),
        #then finds a linear regression for those points and finally, calculates the standard deviation from this linear line
        var=np.var(np.abs(D_reshaped_y - D_predict))
        std_dev=sqrt(var)

        #here we determine the minimum intensity point in the background on the right
        min_right_BG=np.amin(D2[point3:,1])
        min_coord_2 = np.where(D2[point3:,1] == min_right_BG)
        minimum_right=D2[(min_coord_2[0][0]+point3),1]

        klm4=0
        blank3=np.zeros(((point4-point3),2))
        for i in range(point3,point4):
            if (D2[i,1]<(2.5*std_dev+minimum_right)):
                blank3[klm4,:]=D2[i,:]
                klm4+=1
        #blank3_1 contains all background points that have are in intensity within the interval between the minimum BG point
        #and the sum of the minimum BG point and 2.5*standard deviation
        blank3_1=blank3[:klm4,:]

    #if condition below just to check if no points inside blank3_1
        if 0 in blank3_1.shape:
            print('error')
            continue

        #from this selection of BG points on the right side, we calculate another linear line
        blank3_reshaped_x = np.reshape(blank3_1[:, 0], (-1, 1))
        blank3_reshaped_y = np.reshape(blank3_1[:, 1], (-1, 1))
        BG_fit_right2 = LinearRegression().fit(blank3_reshaped_x, blank3_reshaped_y)
        blank3_predict = BG_fit_right2.predict(blank3_reshaped_x)
        n11 = BG_fit_right2.intercept_
        k11 = BG_fit_right2.coef_
    # we find one 'point' which serves as the 'average' value of the background; x of this point is where we previously found a minimum
    # y of this point is calculate from the linear regression line
        x1 = D2[point4-1, 0]
        y1 = x1*k11+n11

        #CALCULATE THE BACKGROUND ON THE LEFT; the same procedure as for the BG on the right
        point1=0
        klm2=0
        point2=0

        for i in range(a):
            if klm2!=0:
                break
            if D2[i,0]>(C[0,0]-5.0):
                point2=i
                klm2=1
        if point2==0:
            point2=50

        min_left_BG=np.amin(D2[point1:point2,1])
        min_coord = np.where(D2[:,1] == min_left_BG)
        blank1=np.zeros((point2,2))

        klm3=0
        for i in range(point2):
            if (D2[i,1]-2.5*std_dev-min_left_BG)<0:
                blank1[klm3,:]=D2[i,[0,1]]
                klm3 += 1

        blank1_1=blank1[:klm3,:]

        #check if blank 1_1 contains any points
        if 0 in blank1_1.shape:
            print('blank1')
            continue

        blank1_1_reshaped_x = np.reshape(blank1_1[:, 0], (-1, 1))
        blank1_1_reshaped_y = np.reshape(blank1_1[:, 1], (-1, 1))
        BG_fit_left = LinearRegression().fit(blank1_1_reshaped_x, blank1_1_reshaped_y)
        n2 = BG_fit_left.intercept_
        k2 = BG_fit_left.coef_
    #we find one 'point' which serves as the 'average' value of the background; x of this point is where we previously found a minimum
    #y of this point is calculate from the linear regression line
        x2 = D2[min_coord[0][0], 0]
        y2= k2*x2+n2

        #final n and k of the linear backrgound are calculated from the two points determined at each of the two BG sides
        #from the spectrum (left and right background)
        k_fin=(y1-y2)/(x1-x2)
        n_fin=y1-k_fin*x1

        #create a matrix for the linear background
        BG=np.zeros((a,2))
        BG[:,0]=D2[:,0]

        for j in range(a):
            BG[j,1]=(k_fin*BG[j,0])+n_fin
        chi_1=0

        #SUBTRACT BACKGROUND
        for i in range(a):
            D2[i,1]=D2[i,1]-BG[i,1]

        #subtract BG from the two points in C array
        C[0,1]=C[0,1]-k_fin*C[0,0]-n_fin
        C[1,1]=C[1,1]-k_fin*C[1,0]-n_fin

        #NEXT: construct a reference PC spectrum
        #pseudo Voigt; sum of G+L
        F_g=1 #eV
        F_l=0.15 #eV
        #the reference spectrum should have a better KE resolution as the experimental one; a2 determines the KE
        #resolution of the reference spectrum
        a2=5*a

        #E_1 is the position of the C-O peak
        E_1=C[0,0]
        KE_start= D2[0,0]
        KE_stop=D2[(a-1),0]
        #fit curve function draws the reference PC spectrum (function output is an array with the reference spectrum)
        peaks=PC_curve(E_1,C,F_g,F_l,KE_start,KE_stop,a2)
        #peaks has the dimensions (1,a2); contains only intensities for the KEs

        peaks_2=np.zeros((a2,2))
        KE=np.linspace(KE_start,KE_stop,a2)
        #new matrix, peaks_2, which has dimensions (a2,2) and also contains KEs
        for i in range(a2):
            peaks_2[i,:]=[KE[i],float(peaks[i])]

        #function adjust_curve looks for the best match between the reference PC spectrum and the experimental spectrum
        # by using the grid-mesh optimization
        new_fit=grid_mesh(D2,peaks_2,C,a,a2)
        steps_x,x1=new_fit[a2,:]
        new_fit = np.delete(new_fit, a, 0)
        steps_x=round(steps_x)
    #a new array with the residuals of the overlap between the experimental and the reference spectrum
        residuals=np.zeros((a,2))
        E_1 = E_1+(x1*E_step/(a2/a))

        #residuals are shifted along y-axis (downwards) to make the plot clearer
    #the following few lines only make arrays used to plot the residuals in a nicer way
        res_shift=-60
        for i in range(a):
           residuals[i,0]=D2[i,0]

        res_level=np.zeros((a,2))
        res_level[:,0]=D2[:,0]
        for i in range(a):
            res_level[i,1]=res_shift

        resid=np.zeros((a,2))
        resid[:,0]=residuals[:,0]

        newfit2=best_overlap(new_fit,D2,a,E_step,E_1,a2)
        for i in range(a):
            resid[i, 1] = D2[i, 1] - newfit2[i, 1] + res_shift

        PC_shift[(c-e),0]=c #c is never 0; we start from c=1
        PC_shift[(c-e), 1] = (newfit2[(a), 0])

        #E_CO_current is the KE of the C=O peak
        E_CO_current=(newfit2[(a), 0])

        final_fit_parameters[(c-e),:]=newfit2[(a+1),:]

        #deletes last two rows
        newfit_2=np.delete(newfit2,(a,(a+1)),0)
        newfit2=newfit_2[:,[0,1]]

        #a condition for plotting and saving the fit of each individual scan
        if True:
            fig, ax = plt.subplots(1, 1)
            plt.xlabel(r'Kinetic Energy [eV]', fontsize=13)
            plt.ylabel(r'Cps [s$^{-1}$]', fontsize=13)

            ax.plot(D2[:, 0], D2[:, 1],linewidth=0,linestyle='-',label='experimental',marker='o',markersize=1.5,color=colors[4])
            ax.plot(newfit2[:, 0], newfit2[:, 1],linewidth=1.5,linestyle='-',label='best fit',color=colors[1])
            ax.plot(resid[:, 0], resid[:, 1],linewidth=0.4,linestyle='-', label='residuals',color=colors[3])
            ax.plot(res_level[:, 0], res_level[:, 1],linewidth=1,linestyle='--',label='residual baseline',color=colors[7])

            #vertical grey line to indicate where was the initial guess for C-O
            plt.axvline(x=C[0,0], ymin=-100, ymax=200, linestyle='--', color='gray')
            #plt.legend(loc='upper left')

            #save the plotted fit of each scan
            plot_name='scan'+str(c)+'_'  +output_name_1+'.jpg'
            plot_location= os.sep.join([path_file_output2, plot_name])
            plt.savefig(plot_location)
            plt.close()

            #in each c-th loop save the array containing the C=O positions of all spectra that have been fitted so far
            #the number of fitted spectra is equal to c
            shift_array=output_name_1+'_PC_shift'+'.txt'
            shift_array_location=os.sep.join([path_file_output2, shift_array])
            np.savetxt(shift_array_location,PC_shift,delimiter='\t')
            np.savetxt(fit_par_location, final_fit_parameters, delimiter='\t')

        #the 3 lines below are for timing the computational time of each scan
        et=time.time()
        total_time=et-st
        print(total_time,'time elapsed')

    #plot KE as a function of the number of scans
    fig, ax = plt.subplots(1, 1)
    plt.xlabel(r'Scan number', fontsize=13)
    plt.ylabel(r'PC shift', fontsize=13)

    plt.tight_layout()
    ax.plot(PC_shift[:, 0], PC_shift[:, 1],marker='o',markersize=2.5, color='b')

#plt.show() commented out if we are fitting several experiments in one go; i.e. if the input directory contains several
#spectra, showing a plot would stop the code from fitting the next spectrum
    #plt.show()






