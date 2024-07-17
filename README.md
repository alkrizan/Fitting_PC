# Fitting_PC
Script for fitting C 1s spectra (XPS) of propylene carbonate (PC). The script was used to obtain plots of C 1s kinetic energy KE as a function of time, which are published in paper with DOI: . When using this code, please cite this paper as the source of the code. 

The purpose of this script is to determine the position of C 1s spectra on the kinetic energy scale, which is done by fitting the experimentally obtained spectra with a PC reference spectrum. The current form of the code is especially suitable for fitting noisy PC spectra recorded with ambient pressure XPS where beam damage irradiation produces unknown species distorting the experimental data overlaps with the C-O and C-C/C-H peaks. The beam damage issue is circumvented by assessing the match between the reference and the experimental spectrum only in proximity of the C=O peak. Additionally, fitting procedure is adjusted to a specific type/form of the noise present in experiments discussed in DOI: . Because of the noise specificity, even minor changes such as the change of the acquisition settings (slit size etc.) or a change in the XPS detector require some code modifications. 

The script consists of the main code and three functions; all 4 scripts should be saved in the same folder. 
Each PC spectrum is fitted according to the following steps:
1. approximate position of the C-O and C-C peak is determined
2. linear background is subtracted
3. grid-mesh method is used to adjust the reference spectrum position and improve the overlap between the reference spectrum and the experimental spectrum
4. steepest descent algorithm using Nelder-Mead sampling is used to improve the match between the reference and the experimental spectrum from point (3)

An example of a raw spectrum and the corresponding fit obtained with this code is shown below. The input required for running the code is an array with dimensions (N+1)*M. The first column contains the kinetic energy of each data point. Columns from 2 to N+1 contain the PC spectra which we would like to fit (e.g. consecutively recorded PC spectra). M is the number of data points (detector channels) of the PC spectra. Two examples of the input files are provided in the repository. The script fits each of the N PC spectra, saves a plot of each fit in the chosen directory and after fitting all N spectra, a plot of the C=O position (kinetic energy) against the number of the spectrum column (between 2 and N+1) is plotted and saved in a text file. 

![rect8517](https://github.com/alkrizan/Fitting_PC/assets/164196118/da37a5e0-89fb-4a6e-90c4-e66692277e9e)

Violet dots show the experimental data, orange line is the best fit between the experimental data and the reference spectrum, grey vertical line corresponds to the initial guess for the C-O peak and black dots are the residuals of the best fit. 
