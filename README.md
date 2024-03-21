# Fitting_PC
Script for fitting C 1s spectra (XPS) of propylene carbonate (PC). The purpose of this script is to determine the position of C 1s spectra on the kinetic energy scale, which is done by fitting the experimentally obtained spectra with a PC reference spectrum. The current form of the code is especially suitable for fitting fairly noisy PC spectra recorded with ambient pressure XPS where beam damage irradiation produces unknown species distorting the experimental data overlaps with the C-O and C-C/C-H peaks. The beam damage issue is circumvented by assessing the match between the reference and the experimental spectrum only in proximity of the C=O peak. 

The code is fairly messy (not polished!) and contains several bits that could seem redundant; those bits were however necessary to prevent large errors in the fitting. The errors stemmed from the noisiness of the data and are specific to the particular kind of the noise characteristic of my experimental data. Because of the noise specificity, even minor changes such as the change of the acquisition settings (slit size etc.) or a change in the XPS detector required substantial code modifications. It is therefore expected, that a lot of modifications will be necessary when using this code to analyze data from other experiments (even if the data is acquired in similar experiments).

The script was used to obtain plots of C 1s kinetic energy KE as a function of time, which are published in paper with DOI: . When using this code, please cite this paper as the source of the code. 

The script consists of the main code and three functions; all 4 scripts should be saved in the same folder. 
Each PC spectrum is fitted according to the following steps:
1. approximate position of the C-O and C-C peak is determined
2. linear background is subtracted
3. grid-mesh method is used to improve the overlap between the reference spectrum and the experimental spectrum
4. steepest descent algorithm using Nead-Melder sampling is used to improve the match between the reference and the experimental spectrum from point (3)

An example of a raw spectrum and the corresponding fit obtained with this code is shown below. The input required for running the code is an array with dimensions (N+1)*M. The first column contains the kinetic energy of each data point. Columns from 2 to N+1 contain the PC spectra which we would like to fit (e.g. consecutively recorded PC spectra). M is the number of data points (detector channels) of the PC spectra. Two examples of the input files are provided in the repository. The script fits each of the N PC spectra, saves a plot of each fit in the chosen directory and after fitting all N spectra, a plot of the C=O position (kinetic energy) against the number of the spectrum column (between 2 and N+1) is plotted and saved in a text file. 


![scan1_ID57](https://github.com/alkrizan/Fitting_PC/assets/164196118/a3dcf285-96a8-4585-a370-bff81b996671)
<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="460.8pt" height="345.6pt" viewBox="0 0 460.8 345.6" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2024-03-21T14:44:38.896260</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.6.2, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 345.6 
L 460.8 345.6 
L 460.8 0 
L 0 0 
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 57.6 307.584 
L 414.72 307.584 
L 414.72 41.472 
L 57.6 41.472 
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <defs>
       <path id="m77eaecb73d" d="M 0 0 
L 0 3.5 
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m77eaecb73d" x="63.390001" y="307.584" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <!-- 1506 -->
      <g transform="translate(50.665001 322.182437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-31" d="M 794 531 
L 1825 531 
L 1825 4091 
L 703 3866 
L 703 4441 
L 1819 4666 
L 2450 4666 
L 2450 531 
L 3481 531 
L 3481 0 
L 794 0 
L 794 531 
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-35" d="M 691 4666 
L 3169 4666 
L 3169 4134 
L 1269 4134 
L 1269 2991 
Q 1406 3038 1543 3061 
Q 1681 3084 1819 3084 
Q 2600 3084 3056 2656 
Q 3513 2228 3513 1497 
Q 3513 744 3044 326 
Q 2575 -91 1722 -91 
Q 1428 -91 1123 -41 
Q 819 9 494 109 
L 494 744 
Q 775 591 1075 516 
Q 1375 441 1709 441 
Q 2250 441 2565 725 
Q 2881 1009 2881 1497 
Q 2881 1984 2565 2268 
Q 2250 2553 1709 2553 
Q 1456 2553 1204 2497 
Q 953 2441 691 2322 
L 691 4666 
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-30" d="M 2034 4250 
Q 1547 4250 1301 3770 
Q 1056 3291 1056 2328 
Q 1056 1369 1301 889 
Q 1547 409 2034 409 
Q 2525 409 2770 889 
Q 3016 1369 3016 2328 
Q 3016 3291 2770 3770 
Q 2525 4250 2034 4250 
z
M 2034 4750 
Q 2819 4750 3233 4129 
Q 3647 3509 3647 2328 
Q 3647 1150 3233 529 
Q 2819 -91 2034 -91 
Q 1250 -91 836 529 
Q 422 1150 422 2328 
Q 422 3509 836 4129 
Q 1250 4750 2034 4750 
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-36" d="M 2113 2584 
Q 1688 2584 1439 2293 
Q 1191 2003 1191 1497 
Q 1191 994 1439 701 
Q 1688 409 2113 409 
Q 2538 409 2786 701 
Q 3034 994 3034 1497 
Q 3034 2003 2786 2293 
Q 2538 2584 2113 2584 
z
M 3366 4563 
L 3366 3988 
Q 3128 4100 2886 4159 
Q 2644 4219 2406 4219 
Q 1781 4219 1451 3797 
Q 1122 3375 1075 2522 
Q 1259 2794 1537 2939 
Q 1816 3084 2150 3084 
Q 2853 3084 3261 2657 
Q 3669 2231 3669 1497 
Q 3669 778 3244 343 
Q 2819 -91 2113 -91 
Q 1303 -91 875 529 
Q 447 1150 447 2328 
Q 447 3434 972 4092 
Q 1497 4750 2381 4750 
Q 2619 4750 2861 4703 
Q 3103 4656 3366 4563 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="127.246094"/>
       <use xlink:href="#DejaVuSans-36" x="190.869141"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_2">
      <g>
       <use xlink:href="#m77eaecb73d" x="116.152255" y="307.584" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <!-- 1508 -->
      <g transform="translate(103.427255 322.182437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-38" d="M 2034 2216 
Q 1584 2216 1326 1975 
Q 1069 1734 1069 1313 
Q 1069 891 1326 650 
Q 1584 409 2034 409 
Q 2484 409 2743 651 
Q 3003 894 3003 1313 
Q 3003 1734 2745 1975 
Q 2488 2216 2034 2216 
z
M 1403 2484 
Q 997 2584 770 2862 
Q 544 3141 544 3541 
Q 544 4100 942 4425 
Q 1341 4750 2034 4750 
Q 2731 4750 3128 4425 
Q 3525 4100 3525 3541 
Q 3525 3141 3298 2862 
Q 3072 2584 2669 2484 
Q 3125 2378 3379 2068 
Q 3634 1759 3634 1313 
Q 3634 634 3220 271 
Q 2806 -91 2034 -91 
Q 1263 -91 848 271 
Q 434 634 434 1313 
Q 434 1759 690 2068 
Q 947 2378 1403 2484 
z
M 1172 3481 
Q 1172 3119 1398 2916 
Q 1625 2713 2034 2713 
Q 2441 2713 2670 2916 
Q 2900 3119 2900 3481 
Q 2900 3844 2670 4047 
Q 2441 4250 2034 4250 
Q 1625 4250 1398 4047 
Q 1172 3844 1172 3481 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="127.246094"/>
       <use xlink:href="#DejaVuSans-38" x="190.869141"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_3">
      <g>
       <use xlink:href="#m77eaecb73d" x="168.914508" y="307.584" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <!-- 1510 -->
      <g transform="translate(156.189508 322.182437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-31" x="127.246094"/>
       <use xlink:href="#DejaVuSans-30" x="190.869141"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_4">
      <g>
       <use xlink:href="#m77eaecb73d" x="221.676761" y="307.584" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_4">
      <!-- 1512 -->
      <g transform="translate(208.951761 322.182437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-32" d="M 1228 531 
L 3431 531 
L 3431 0 
L 469 0 
L 469 531 
Q 828 903 1448 1529 
Q 2069 2156 2228 2338 
Q 2531 2678 2651 2914 
Q 2772 3150 2772 3378 
Q 2772 3750 2511 3984 
Q 2250 4219 1831 4219 
Q 1534 4219 1204 4116 
Q 875 4013 500 3803 
L 500 4441 
Q 881 4594 1212 4672 
Q 1544 4750 1819 4750 
Q 2544 4750 2975 4387 
Q 3406 4025 3406 3419 
Q 3406 3131 3298 2873 
Q 3191 2616 2906 2266 
Q 2828 2175 2409 1742 
Q 1991 1309 1228 531 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-31" x="127.246094"/>
       <use xlink:href="#DejaVuSans-32" x="190.869141"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_5">
      <g>
       <use xlink:href="#m77eaecb73d" x="274.439015" y="307.584" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 1514 -->
      <g transform="translate(261.714015 322.182437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-34" d="M 2419 4116 
L 825 1625 
L 2419 1625 
L 2419 4116 
z
M 2253 4666 
L 3047 4666 
L 3047 1625 
L 3713 1625 
L 3713 1100 
L 3047 1100 
L 3047 0 
L 2419 0 
L 2419 1100 
L 313 1100 
L 313 1709 
L 2253 4666 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-31" x="127.246094"/>
       <use xlink:href="#DejaVuSans-34" x="190.869141"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_6">
      <g>
       <use xlink:href="#m77eaecb73d" x="327.201268" y="307.584" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <!-- 1516 -->
      <g transform="translate(314.476268 322.182437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-31" x="127.246094"/>
       <use xlink:href="#DejaVuSans-36" x="190.869141"/>
      </g>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_7">
      <g>
       <use xlink:href="#m77eaecb73d" x="379.963522" y="307.584" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_7">
      <!-- 1518 -->
      <g transform="translate(367.238522 322.182437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-31" x="127.246094"/>
       <use xlink:href="#DejaVuSans-38" x="190.869141"/>
      </g>
     </g>
    </g>
    <g id="text_8">
     <!-- Kinetic Energy [eV] -->
     <g transform="translate(173.637109 338.140094) scale(0.13 -0.13)">
      <defs>
       <path id="DejaVuSans-4b" d="M 628 4666 
L 1259 4666 
L 1259 2694 
L 3353 4666 
L 4166 4666 
L 1850 2491 
L 4331 0 
L 3500 0 
L 1259 2247 
L 1259 0 
L 628 0 
L 628 4666 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-69" d="M 603 3500 
L 1178 3500 
L 1178 0 
L 603 0 
L 603 3500 
z
M 603 4863 
L 1178 4863 
L 1178 4134 
L 603 4134 
L 603 4863 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-6e" d="M 3513 2113 
L 3513 0 
L 2938 0 
L 2938 2094 
Q 2938 2591 2744 2837 
Q 2550 3084 2163 3084 
Q 1697 3084 1428 2787 
Q 1159 2491 1159 1978 
L 1159 0 
L 581 0 
L 581 3500 
L 1159 3500 
L 1159 2956 
Q 1366 3272 1645 3428 
Q 1925 3584 2291 3584 
Q 2894 3584 3203 3211 
Q 3513 2838 3513 2113 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-65" d="M 3597 1894 
L 3597 1613 
L 953 1613 
Q 991 1019 1311 708 
Q 1631 397 2203 397 
Q 2534 397 2845 478 
Q 3156 559 3463 722 
L 3463 178 
Q 3153 47 2828 -22 
Q 2503 -91 2169 -91 
Q 1331 -91 842 396 
Q 353 884 353 1716 
Q 353 2575 817 3079 
Q 1281 3584 2069 3584 
Q 2775 3584 3186 3129 
Q 3597 2675 3597 1894 
z
M 3022 2063 
Q 3016 2534 2758 2815 
Q 2500 3097 2075 3097 
Q 1594 3097 1305 2825 
Q 1016 2553 972 2059 
L 3022 2063 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-74" d="M 1172 4494 
L 1172 3500 
L 2356 3500 
L 2356 3053 
L 1172 3053 
L 1172 1153 
Q 1172 725 1289 603 
Q 1406 481 1766 481 
L 2356 481 
L 2356 0 
L 1766 0 
Q 1100 0 847 248 
Q 594 497 594 1153 
L 594 3053 
L 172 3053 
L 172 3500 
L 594 3500 
L 594 4494 
L 1172 4494 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-63" d="M 3122 3366 
L 3122 2828 
Q 2878 2963 2633 3030 
Q 2388 3097 2138 3097 
Q 1578 3097 1268 2742 
Q 959 2388 959 1747 
Q 959 1106 1268 751 
Q 1578 397 2138 397 
Q 2388 397 2633 464 
Q 2878 531 3122 666 
L 3122 134 
Q 2881 22 2623 -34 
Q 2366 -91 2075 -91 
Q 1284 -91 818 406 
Q 353 903 353 1747 
Q 353 2603 823 3093 
Q 1294 3584 2113 3584 
Q 2378 3584 2631 3529 
Q 2884 3475 3122 3366 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-20" transform="scale(0.015625)"/>
       <path id="DejaVuSans-45" d="M 628 4666 
L 3578 4666 
L 3578 4134 
L 1259 4134 
L 1259 2753 
L 3481 2753 
L 3481 2222 
L 1259 2222 
L 1259 531 
L 3634 531 
L 3634 0 
L 628 0 
L 628 4666 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-72" d="M 2631 2963 
Q 2534 3019 2420 3045 
Q 2306 3072 2169 3072 
Q 1681 3072 1420 2755 
Q 1159 2438 1159 1844 
L 1159 0 
L 581 0 
L 581 3500 
L 1159 3500 
L 1159 2956 
Q 1341 3275 1631 3429 
Q 1922 3584 2338 3584 
Q 2397 3584 2469 3576 
Q 2541 3569 2628 3553 
L 2631 2963 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-67" d="M 2906 1791 
Q 2906 2416 2648 2759 
Q 2391 3103 1925 3103 
Q 1463 3103 1205 2759 
Q 947 2416 947 1791 
Q 947 1169 1205 825 
Q 1463 481 1925 481 
Q 2391 481 2648 825 
Q 2906 1169 2906 1791 
z
M 3481 434 
Q 3481 -459 3084 -895 
Q 2688 -1331 1869 -1331 
Q 1566 -1331 1297 -1286 
Q 1028 -1241 775 -1147 
L 775 -588 
Q 1028 -725 1275 -790 
Q 1522 -856 1778 -856 
Q 2344 -856 2625 -561 
Q 2906 -266 2906 331 
L 2906 616 
Q 2728 306 2450 153 
Q 2172 0 1784 0 
Q 1141 0 747 490 
Q 353 981 353 1791 
Q 353 2603 747 3093 
Q 1141 3584 1784 3584 
Q 2172 3584 2450 3431 
Q 2728 3278 2906 2969 
L 2906 3500 
L 3481 3500 
L 3481 434 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-79" d="M 2059 -325 
Q 1816 -950 1584 -1140 
Q 1353 -1331 966 -1331 
L 506 -1331 
L 506 -850 
L 844 -850 
Q 1081 -850 1212 -737 
Q 1344 -625 1503 -206 
L 1606 56 
L 191 3500 
L 800 3500 
L 1894 763 
L 2988 3500 
L 3597 3500 
L 2059 -325 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-5b" d="M 550 4863 
L 1875 4863 
L 1875 4416 
L 1125 4416 
L 1125 -397 
L 1875 -397 
L 1875 -844 
L 550 -844 
L 550 4863 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-56" d="M 1831 0 
L 50 4666 
L 709 4666 
L 2188 738 
L 3669 4666 
L 4325 4666 
L 2547 0 
L 1831 0 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-5d" d="M 1947 4863 
L 1947 -844 
L 622 -844 
L 622 -397 
L 1369 -397 
L 1369 4416 
L 622 4416 
L 622 4863 
L 1947 4863 
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-4b"/>
      <use xlink:href="#DejaVuSans-69" x="65.576172"/>
      <use xlink:href="#DejaVuSans-6e" x="93.359375"/>
      <use xlink:href="#DejaVuSans-65" x="156.738281"/>
      <use xlink:href="#DejaVuSans-74" x="218.261719"/>
      <use xlink:href="#DejaVuSans-69" x="257.470703"/>
      <use xlink:href="#DejaVuSans-63" x="285.253906"/>
      <use xlink:href="#DejaVuSans-20" x="340.234375"/>
      <use xlink:href="#DejaVuSans-45" x="372.021484"/>
      <use xlink:href="#DejaVuSans-6e" x="435.205078"/>
      <use xlink:href="#DejaVuSans-65" x="498.583984"/>
      <use xlink:href="#DejaVuSans-72" x="560.107422"/>
      <use xlink:href="#DejaVuSans-67" x="599.470703"/>
      <use xlink:href="#DejaVuSans-79" x="662.947266"/>
      <use xlink:href="#DejaVuSans-20" x="722.126953"/>
      <use xlink:href="#DejaVuSans-5b" x="753.914062"/>
      <use xlink:href="#DejaVuSans-65" x="792.927734"/>
      <use xlink:href="#DejaVuSans-56" x="854.451172"/>
      <use xlink:href="#DejaVuSans-5d" x="922.859375"/>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_8">
      <defs>
       <path id="m2b7eab1c1b" d="M 0 0 
L -3.5 0 
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="291.500998" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_9">
      <!-- −150 -->
      <g transform="translate(23.132812 295.300217) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-2212" d="M 678 2272 
L 4684 2272 
L 4684 1741 
L 678 1741 
L 678 2272 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-31" x="83.789062"/>
       <use xlink:href="#DejaVuSans-35" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="211.035156"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_9">
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="261.644859" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_10">
      <!-- −100 -->
      <g transform="translate(23.132812 265.444078) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-31" x="83.789062"/>
       <use xlink:href="#DejaVuSans-30" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="211.035156"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_10">
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="231.78872" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_11">
      <!-- −50 -->
      <g transform="translate(29.495313 235.587939) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-35" x="83.789062"/>
       <use xlink:href="#DejaVuSans-30" x="147.412109"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_11">
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="201.932581" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- 0 -->
      <g transform="translate(44.2375 205.7318) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_12">
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="172.076442" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_13">
      <!-- 50 -->
      <g transform="translate(37.875 175.875661) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-35"/>
       <use xlink:href="#DejaVuSans-30" x="63.623047"/>
      </g>
     </g>
    </g>
    <g id="ytick_6">
     <g id="line2d_13">
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="142.220303" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_14">
      <!-- 100 -->
      <g transform="translate(31.5125 146.019522) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-30" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="127.246094"/>
      </g>
     </g>
    </g>
    <g id="ytick_7">
     <g id="line2d_14">
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="112.364164" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_15">
      <!-- 150 -->
      <g transform="translate(31.5125 116.163383) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="127.246094"/>
      </g>
     </g>
    </g>
    <g id="ytick_8">
     <g id="line2d_15">
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="82.508025" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_16">
      <!-- 200 -->
      <g transform="translate(31.5125 86.307244) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-32"/>
       <use xlink:href="#DejaVuSans-30" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="127.246094"/>
      </g>
     </g>
    </g>
    <g id="ytick_9">
     <g id="line2d_16">
      <g>
       <use xlink:href="#m2b7eab1c1b" x="57.6" y="52.651886" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_17">
      <!-- 250 -->
      <g transform="translate(31.5125 56.451105) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-32"/>
       <use xlink:href="#DejaVuSans-35" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="127.246094"/>
      </g>
     </g>
    </g>
    <g id="text_18">
     <!-- Cps [s$^{-1}$] -->
     <g transform="translate(16.402812 204.103) rotate(-90) scale(0.13 -0.13)">
      <defs>
       <path id="DejaVuSans-43" d="M 4122 4306 
L 4122 3641 
Q 3803 3938 3442 4084 
Q 3081 4231 2675 4231 
Q 1875 4231 1450 3742 
Q 1025 3253 1025 2328 
Q 1025 1406 1450 917 
Q 1875 428 2675 428 
Q 3081 428 3442 575 
Q 3803 722 4122 1019 
L 4122 359 
Q 3791 134 3420 21 
Q 3050 -91 2638 -91 
Q 1578 -91 968 557 
Q 359 1206 359 2328 
Q 359 3453 968 4101 
Q 1578 4750 2638 4750 
Q 3056 4750 3426 4639 
Q 3797 4528 4122 4306 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-70" d="M 1159 525 
L 1159 -1331 
L 581 -1331 
L 581 3500 
L 1159 3500 
L 1159 2969 
Q 1341 3281 1617 3432 
Q 1894 3584 2278 3584 
Q 2916 3584 3314 3078 
Q 3713 2572 3713 1747 
Q 3713 922 3314 415 
Q 2916 -91 2278 -91 
Q 1894 -91 1617 61 
Q 1341 213 1159 525 
z
M 3116 1747 
Q 3116 2381 2855 2742 
Q 2594 3103 2138 3103 
Q 1681 3103 1420 2742 
Q 1159 2381 1159 1747 
Q 1159 1113 1420 752 
Q 1681 391 2138 391 
Q 2594 391 2855 752 
Q 3116 1113 3116 1747 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-73" d="M 2834 3397 
L 2834 2853 
Q 2591 2978 2328 3040 
Q 2066 3103 1784 3103 
Q 1356 3103 1142 2972 
Q 928 2841 928 2578 
Q 928 2378 1081 2264 
Q 1234 2150 1697 2047 
L 1894 2003 
Q 2506 1872 2764 1633 
Q 3022 1394 3022 966 
Q 3022 478 2636 193 
Q 2250 -91 1575 -91 
Q 1294 -91 989 -36 
Q 684 19 347 128 
L 347 722 
Q 666 556 975 473 
Q 1284 391 1588 391 
Q 1994 391 2212 530 
Q 2431 669 2431 922 
Q 2431 1156 2273 1281 
Q 2116 1406 1581 1522 
L 1381 1569 
Q 847 1681 609 1914 
Q 372 2147 372 2553 
Q 372 3047 722 3315 
Q 1072 3584 1716 3584 
Q 2034 3584 2315 3537 
Q 2597 3491 2834 3397 
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-43" transform="translate(0 0.684375)"/>
      <use xlink:href="#DejaVuSans-70" transform="translate(69.824219 0.684375)"/>
      <use xlink:href="#DejaVuSans-73" transform="translate(133.300781 0.684375)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(185.400391 0.684375)"/>
      <use xlink:href="#DejaVuSans-5b" transform="translate(217.1875 0.684375)"/>
      <use xlink:href="#DejaVuSans-73" transform="translate(256.201172 0.684375)"/>
      <use xlink:href="#DejaVuSans-2212" transform="translate(309.257812 38.965625) scale(0.7)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(367.910156 38.965625) scale(0.7)"/>
      <use xlink:href="#DejaVuSans-5d" transform="translate(415.180664 0.684375)"/>
     </g>
    </g>
   </g>
   <g id="line2d_17">
    <path d="M 73.832727 193.643142 
L 75.464157 192.348691 
L 77.095587 196.629158 
L 78.727017 198.131159 
L 80.358447 189.827317 
L 81.989877 197.253426 
L 83.621307 196.185404 
L 85.252736 198.223663 
L 86.884166 196.00243 
L 88.515596 203.463471 
L 90.147026 202.79204 
L 91.778456 182.843134 
L 93.409886 198.971549 
L 95.041316 201.469395 
L 96.672746 203.482539 
L 98.304175 199.439556 
L 99.935605 201.653799 
L 101.567035 201.484053 
L 103.198465 199.692163 
L 104.829895 203.229436 
L 106.461325 195.503557 
L 108.092755 199.612835 
L 109.724185 198.476628 
L 111.355614 198.616197 
L 112.987044 201.580438 
L 114.618474 200.815438 
L 116.249904 195.181541 
L 117.881334 203.532116 
L 119.512764 194.211678 
L 121.144194 199.894541 
L 122.775624 199.424908 
L 124.407053 197.99128 
L 126.038483 190.935771 
L 127.669913 197.872932 
L 129.301343 194.153948 
L 130.932773 193.593063 
L 132.564203 192.715822 
L 134.195633 181.606583 
L 135.827063 177.273673 
L 137.458492 153.647965 
L 139.089922 168.764538 
L 140.721352 179.966255 
L 142.352782 174.16078 
L 143.984212 161.101996 
L 145.615642 155.5334 
L 147.247072 171.276415 
L 148.878502 151.625335 
L 150.509931 152.780282 
L 152.141361 159.176713 
L 153.772791 127.07622 
L 155.404221 145.299444 
L 157.035651 127.351358 
L 158.667081 157.322853 
L 160.298511 128.095835 
L 161.929941 140.62609 
L 163.56137 155.685459 
L 165.1928 159.924844 
L 166.82423 131.871171 
L 168.45566 156.437929 
L 170.08709 141.01836 
L 171.71852 137.575581 
L 173.34995 175.988601 
L 174.98138 181.161288 
L 176.61281 170.855956 
L 178.244239 185.539078 
L 179.875669 182.48825 
L 181.507099 177.520658 
L 183.138529 189.413843 
L 184.769959 193.595188 
L 186.401389 193.447272 
L 188.032819 191.758661 
L 189.664249 198.531619 
L 191.295678 193.108978 
L 192.927108 199.030846 
L 194.558538 198.334963 
L 196.189968 188.069417 
L 197.821398 190.666117 
L 199.452828 197.719861 
L 201.084258 197.586097 
L 202.715688 195.07477 
L 204.347117 193.407894 
L 205.978547 186.34046 
L 207.609977 189.018309 
L 209.241407 188.635127 
L 210.872837 194.253925 
L 212.504267 191.529783 
L 214.135697 191.775073 
L 215.767127 182.865874 
L 217.398556 182.572022 
L 219.029986 197.064482 
L 220.661416 194.731217 
L 222.292846 180.945376 
L 223.924276 182.951999 
L 225.555706 167.99108 
L 227.187136 171.314717 
L 228.818566 172.738429 
L 230.449995 167.616003 
L 232.081425 153.855719 
L 233.712855 167.62566 
L 235.344285 145.007119 
L 236.975715 132.531365 
L 238.607145 142.994979 
L 243.501434 109.397961 
L 245.132864 92.733092 
L 246.764294 54.713919 
L 250.027154 104.440974 
L 251.658584 90.113841 
L 253.290014 54.322532 
L 254.921444 53.568 
L 256.552873 58.141594 
L 258.184303 59.764805 
L 259.815733 93.055825 
L 261.447163 105.002094 
L 263.078593 112.459791 
L 264.710023 112.433749 
L 266.341453 112.658498 
L 267.972883 152.089134 
L 269.604312 145.724813 
L 271.235742 141.404681 
L 274.498602 159.298464 
L 276.130032 154.321139 
L 277.761462 164.765883 
L 279.392892 151.893043 
L 281.024322 179.825364 
L 282.655751 171.390877 
L 284.287181 159.824661 
L 285.918611 171.779588 
L 287.550041 157.369694 
L 289.181471 138.245455 
L 290.812901 121.503558 
L 292.444331 152.644279 
L 294.075761 135.337563 
L 295.70719 108.118549 
L 297.33862 133.460073 
L 298.97005 111.683237 
L 300.60148 114.036131 
L 302.23291 95.936376 
L 303.86434 101.143518 
L 305.49577 148.549804 
L 307.1272 125.870237 
L 308.75863 119.34093 
L 310.390059 109.873182 
L 312.021489 106.269777 
L 313.652919 146.128491 
L 315.284349 144.705718 
L 316.915779 154.358439 
L 318.547209 142.698773 
L 320.178639 147.729644 
L 321.810069 145.665502 
L 323.441498 169.304211 
L 325.072928 167.044631 
L 326.704358 167.37316 
L 328.335788 175.714599 
L 329.967218 174.995953 
L 331.598648 189.911535 
L 333.230078 188.571464 
L 334.861508 193.879937 
L 336.492937 185.762165 
L 338.124367 176.882344 
L 339.755797 196.109749 
L 341.387227 185.92838 
L 343.018657 186.112703 
L 344.650087 190.308856 
L 346.281517 197.257626 
L 347.912947 190.472512 
L 349.544376 199.99995 
L 351.175806 195.449813 
L 352.807236 199.324511 
L 354.438666 202.457833 
L 356.070096 200.449223 
L 357.701526 200.727355 
L 359.332956 200.822236 
L 360.964386 191.715657 
L 362.595815 195.090349 
L 364.227245 197.792679 
L 365.858675 195.362083 
L 367.490105 194.314304 
L 369.121535 204.11941 
L 370.752965 201.608322 
L 372.384395 201.685719 
L 374.015825 198.004789 
L 375.647254 198.504209 
L 377.278684 195.338381 
L 378.910114 203.329208 
L 380.541544 200.86039 
L 382.172974 193.020565 
L 383.804404 197.349578 
L 385.435834 191.938026 
L 387.067264 195.203981 
L 388.698693 198.925958 
L 390.330123 203.663359 
L 391.961553 199.728356 
L 393.592983 200.693549 
L 395.224413 203.872144 
L 396.855843 199.407152 
L 398.487273 197.962453 
L 398.487273 197.962453 
" clip-path="url(#pe42bb4d5c4)" style="fill: none"/>
    <defs>
     <path id="m0700159113" d="M 0 1.25 
C 0.331504 1.25 0.649475 1.118292 0.883883 0.883883 
C 1.118292 0.649475 1.25 0.331504 1.25 0 
C 1.25 -0.331504 1.118292 -0.649475 0.883883 -0.883883 
C 0.649475 -1.118292 0.331504 -1.25 0 -1.25 
C -0.331504 -1.25 -0.649475 -1.118292 -0.883883 -0.883883 
C -1.118292 -0.649475 -1.25 -0.331504 -1.25 0 
C -1.25 0.331504 -1.118292 0.649475 -0.883883 0.883883 
C -0.649475 1.118292 -0.331504 1.25 0 1.25 
z
" style="stroke: #9467bd"/>
    </defs>
    <g clip-path="url(#pe42bb4d5c4)">
     <use xlink:href="#m0700159113" x="73.832727" y="193.643142" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="75.464157" y="192.348691" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="77.095587" y="196.629158" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="78.727017" y="198.131159" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="80.358447" y="189.827317" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="81.989877" y="197.253426" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="83.621307" y="196.185404" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="85.252736" y="198.223663" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="86.884166" y="196.00243" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="88.515596" y="203.463471" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="90.147026" y="202.79204" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="91.778456" y="182.843134" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="93.409886" y="198.971549" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="95.041316" y="201.469395" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="96.672746" y="203.482539" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="98.304175" y="199.439556" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="99.935605" y="201.653799" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="101.567035" y="201.484053" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="103.198465" y="199.692163" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="104.829895" y="203.229436" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="106.461325" y="195.503557" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="108.092755" y="199.612835" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="109.724185" y="198.476628" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="111.355614" y="198.616197" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="112.987044" y="201.580438" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="114.618474" y="200.815438" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="116.249904" y="195.181541" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="117.881334" y="203.532116" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="119.512764" y="194.211678" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="121.144194" y="199.894541" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="122.775624" y="199.424908" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="124.407053" y="197.99128" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="126.038483" y="190.935771" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="127.669913" y="197.872932" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="129.301343" y="194.153948" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="130.932773" y="193.593063" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="132.564203" y="192.715822" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="134.195633" y="181.606583" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="135.827063" y="177.273673" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="137.458492" y="153.647965" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="139.089922" y="168.764538" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="140.721352" y="179.966255" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="142.352782" y="174.16078" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="143.984212" y="161.101996" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="145.615642" y="155.5334" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="147.247072" y="171.276415" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="148.878502" y="151.625335" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="150.509931" y="152.780282" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="152.141361" y="159.176713" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="153.772791" y="127.07622" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="155.404221" y="145.299444" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="157.035651" y="127.351358" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="158.667081" y="157.322853" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="160.298511" y="128.095835" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="161.929941" y="140.62609" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="163.56137" y="155.685459" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="165.1928" y="159.924844" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="166.82423" y="131.871171" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="168.45566" y="156.437929" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="170.08709" y="141.01836" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="171.71852" y="137.575581" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="173.34995" y="175.988601" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="174.98138" y="181.161288" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="176.61281" y="170.855956" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="178.244239" y="185.539078" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="179.875669" y="182.48825" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="181.507099" y="177.520658" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="183.138529" y="189.413843" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="184.769959" y="193.595188" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="186.401389" y="193.447272" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="188.032819" y="191.758661" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="189.664249" y="198.531619" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="191.295678" y="193.108978" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="192.927108" y="199.030846" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="194.558538" y="198.334963" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="196.189968" y="188.069417" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="197.821398" y="190.666117" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="199.452828" y="197.719861" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="201.084258" y="197.586097" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="202.715688" y="195.07477" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="204.347117" y="193.407894" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="205.978547" y="186.34046" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="207.609977" y="189.018309" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="209.241407" y="188.635127" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="210.872837" y="194.253925" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="212.504267" y="191.529783" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="214.135697" y="191.775073" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="215.767127" y="182.865874" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="217.398556" y="182.572022" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="219.029986" y="197.064482" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="220.661416" y="194.731217" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="222.292846" y="180.945376" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="223.924276" y="182.951999" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="225.555706" y="167.99108" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="227.187136" y="171.314717" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="228.818566" y="172.738429" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="230.449995" y="167.616003" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="232.081425" y="153.855719" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="233.712855" y="167.62566" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="235.344285" y="145.007119" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="236.975715" y="132.531365" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="238.607145" y="142.994979" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="240.238575" y="132.039798" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="241.870005" y="121.772503" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="243.501434" y="109.397961" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="245.132864" y="92.733092" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="246.764294" y="54.713919" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="248.395724" y="78.915536" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="250.027154" y="104.440974" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="251.658584" y="90.113841" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="253.290014" y="54.322532" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="254.921444" y="53.568" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="256.552873" y="58.141594" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="258.184303" y="59.764805" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="259.815733" y="93.055825" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="261.447163" y="105.002094" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="263.078593" y="112.459791" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="264.710023" y="112.433749" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="266.341453" y="112.658498" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="267.972883" y="152.089134" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="269.604312" y="145.724813" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="271.235742" y="141.404681" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="272.867172" y="150.395192" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="274.498602" y="159.298464" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="276.130032" y="154.321139" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="277.761462" y="164.765883" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="279.392892" y="151.893043" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="281.024322" y="179.825364" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="282.655751" y="171.390877" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="284.287181" y="159.824661" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="285.918611" y="171.779588" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="287.550041" y="157.369694" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="289.181471" y="138.245455" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="290.812901" y="121.503558" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="292.444331" y="152.644279" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="294.075761" y="135.337563" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="295.70719" y="108.118549" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="297.33862" y="133.460073" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="298.97005" y="111.683237" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="300.60148" y="114.036131" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="302.23291" y="95.936376" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="303.86434" y="101.143518" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="305.49577" y="148.549804" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="307.1272" y="125.870237" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="308.75863" y="119.34093" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="310.390059" y="109.873182" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="312.021489" y="106.269777" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="313.652919" y="146.128491" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="315.284349" y="144.705718" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="316.915779" y="154.358439" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="318.547209" y="142.698773" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="320.178639" y="147.729644" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="321.810069" y="145.665502" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="323.441498" y="169.304211" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="325.072928" y="167.044631" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="326.704358" y="167.37316" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="328.335788" y="175.714599" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="329.967218" y="174.995953" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="331.598648" y="189.911535" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="333.230078" y="188.571464" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="334.861508" y="193.879937" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="336.492937" y="185.762165" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="338.124367" y="176.882344" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="339.755797" y="196.109749" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="341.387227" y="185.92838" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="343.018657" y="186.112703" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="344.650087" y="190.308856" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="346.281517" y="197.257626" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="347.912947" y="190.472512" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="349.544376" y="199.99995" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="351.175806" y="195.449813" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="352.807236" y="199.324511" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="354.438666" y="202.457833" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="356.070096" y="200.449223" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="357.701526" y="200.727355" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="359.332956" y="200.822236" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="360.964386" y="191.715657" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="362.595815" y="195.090349" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="364.227245" y="197.792679" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="365.858675" y="195.362083" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="367.490105" y="194.314304" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="369.121535" y="204.11941" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="370.752965" y="201.608322" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="372.384395" y="201.685719" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="374.015825" y="198.004789" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="375.647254" y="198.504209" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="377.278684" y="195.338381" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="378.910114" y="203.329208" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="380.541544" y="200.86039" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="382.172974" y="193.020565" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="383.804404" y="197.349578" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="385.435834" y="191.938026" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="387.067264" y="195.203981" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="388.698693" y="198.925958" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="390.330123" y="203.663359" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="391.961553" y="199.728356" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="393.592983" y="200.693549" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="395.224413" y="203.872144" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="396.855843" y="199.407152" style="fill: #9467bd; stroke: #9467bd"/>
     <use xlink:href="#m0700159113" x="398.487273" y="197.962453" style="fill: #9467bd; stroke: #9467bd"/>
    </g>
   </g>
   <g id="line2d_18">
    <path d="M 73.832727 210.00228 
L 75.457625 201.542648 
L 99.831089 201.245894 
L 111.205373 200.906525 
L 116.080066 200.549436 
L 119.329861 200.081168 
L 120.954758 199.719563 
L 122.579656 199.232551 
L 124.204554 198.580194 
L 125.829451 197.714308 
L 127.454349 196.578752 
L 129.079247 195.11066 
L 130.704144 193.242863 
L 132.329042 190.907668 
L 133.953939 188.042038 
L 135.578837 184.594051 
L 140.778509 171.336019 
L 144.028305 159.83901 
L 148.902998 141.537205 
L 150.527895 136.01283 
L 152.152793 131.198536 
L 153.77769 127.346531 
L 155.402588 124.67885 
L 157.027486 123.361356 
L 158.652383 123.479712 
L 160.277281 125.025194 
L 161.902179 127.896187 
L 163.527076 131.914711 
L 165.151974 136.851351 
L 166.776871 142.450936 
L 173.276462 166.564389 
L 174.90136 172.019628 
L 176.526257 176.975977 
L 178.151155 181.370388 
L 179.776052 185.177216 
L 181.40095 188.402534 
L 183.025848 191.077244 
L 184.650745 193.249784 
L 186.275643 194.979171 
L 187.900541 196.328886 
L 189.525438 197.361967 
L 191.150336 198.1374 
L 192.775233 198.707798 
L 194.400131 199.118173 
L 197.649926 199.599413 
L 200.899722 199.789137 
L 204.149517 199.793784 
L 207.399312 199.635942 
L 210.649107 199.255868 
L 212.274005 198.936677 
L 213.898903 198.490927 
L 215.5238 197.875792 
L 217.148698 197.036876 
L 218.773595 195.907367 
L 220.398493 194.408036 
L 222.023391 192.44845 
L 223.648288 189.929821 
L 225.273186 186.749795 
L 226.898084 182.809353 
L 228.522981 178.021749 
L 230.147879 172.323104 
L 231.772776 165.683961 
L 233.397674 158.120751 
L 235.022572 149.705927 
L 238.272367 130.932397 
L 243.14706 101.9059 
L 244.771957 93.437021 
L 246.396855 86.252816 
L 248.021753 80.743633 
L 249.64665 77.236599 
L 251.271548 75.953812 
L 252.896446 76.978051 
L 254.521343 80.238434 
L 256.146241 85.522108 
L 257.771138 92.506826 
L 259.396036 100.802146 
L 262.645831 119.647894 
L 265.895627 138.863675 
L 267.520524 147.776937 
L 269.145422 155.894988 
L 270.770319 163.045096 
L 272.395217 169.112346 
L 274.020115 174.03274 
L 275.645012 177.784263 
L 277.26991 180.377388 
L 278.894808 181.846443 
L 280.519705 182.242885 
L 282.144603 181.631134 
L 283.7695 180.087093 
L 285.394398 177.698997 
L 287.019296 174.569886 
L 288.644193 170.820726 
L 290.269091 166.593156 
L 296.768681 148.477647 
L 298.393579 144.685598 
L 300.018477 141.619472 
L 301.643374 139.467231 
L 303.268272 138.372035 
L 304.89317 138.413206 
L 306.518067 139.594208 
L 308.142965 141.84275 
L 309.767862 145.023145 
L 311.39276 148.956004 
L 313.017658 153.439045 
L 321.142146 177.370106 
L 322.767043 181.423308 
L 324.391941 185.030401 
L 326.016839 188.168062 
L 327.641736 190.838889 
L 329.266634 193.065959 
L 330.891532 194.887007 
L 332.516429 196.34881 
L 334.141327 197.502216 
L 335.766224 198.398109 
L 337.391122 199.084431 
L 339.01602 199.604234 
L 342.265815 200.28657 
L 345.51561 200.669277 
L 350.390303 200.968883 
L 360.139689 201.238697 
L 379.63846 201.492995 
L 397.512334 201.585454 
L 397.512334 201.585454 
" clip-path="url(#pe42bb4d5c4)" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_19">
    <path d="M 73.832727 245.285721 
L 75.464157 252.450903 
L 77.095587 256.744058 
L 78.727017 258.259433 
L 80.358447 249.969704 
L 81.989877 257.410723 
L 83.621307 256.358471 
L 85.252736 258.41343 
L 86.884166 256.209905 
L 88.515596 263.689749 
L 90.147026 263.038313 
L 91.778456 243.110704 
L 93.409886 259.261845 
L 95.041316 261.783994 
L 96.672746 263.823192 
L 98.304175 259.808237 
L 99.935605 262.052764 
L 101.567035 261.915935 
L 103.198465 260.160123 
L 104.829895 263.737386 
L 106.461325 256.056505 
L 108.092755 260.217403 
L 109.724185 259.141825 
L 111.355614 259.354532 
L 112.987044 262.409506 
L 114.618474 261.760121 
L 116.249904 256.276964 
L 117.881334 264.827529 
L 119.512764 255.775369 
L 121.144194 261.819837 
L 122.775624 261.837216 
L 124.407053 261.055945 
L 126.038483 254.866322 
L 127.669913 262.939039 
L 129.301343 260.688147 
L 130.932773 261.995059 
L 132.564203 263.453013 
L 134.195633 255.209405 
L 135.827063 254.324482 
L 137.458492 234.762547 
L 139.089922 254.56588 
L 140.721352 270.275095 
L 142.352782 270.032743 
L 143.984212 262.907845 
L 145.615642 263.490428 
L 147.247072 285.409287 
L 148.878502 271.732989 
L 150.509931 278.412311 
L 152.141361 289.623036 
L 153.772791 261.374548 
L 155.404221 282.265453 
L 157.035651 265.634861 
L 158.667081 295.488 
L 160.298511 264.7155 
L 161.929941 274.374762 
L 163.56137 285.415607 
L 165.1928 284.718352 
L 166.82423 251.065095 
L 168.45566 269.628391 
L 170.08709 248.047526 
L 171.71852 238.506075 
L 173.34995 271.069071 
L 174.98138 270.786519 
L 176.61281 255.524839 
L 178.244239 265.813549 
L 179.875669 258.955893 
L 181.507099 250.762983 
L 183.138529 259.981459 
L 184.769959 261.990263 
L 186.401389 260.112961 
L 188.032819 257.074633 
L 189.664249 262.814511 
L 191.295678 256.616437 
L 192.927108 261.967907 
L 194.558538 260.861649 
L 196.189968 250.308689 
L 197.821398 252.711563 
L 199.452828 259.642778 
L 201.084258 259.441819 
L 202.715688 256.90829 
L 204.347117 255.258969 
L 205.978547 248.248472 
L 207.609977 251.027226 
L 209.241407 250.798939 
L 210.872837 256.642916 
L 212.504267 254.237965 
L 214.135697 254.929006 
L 215.767127 246.634941 
L 217.398556 247.180006 
L 219.029986 262.801974 
L 220.661416 261.96804 
L 222.292846 250.141785 
L 223.924276 254.667037 
L 225.555706 242.886144 
L 227.187136 250.150223 
L 228.818566 256.361539 
L 230.449995 256.937758 
L 232.081425 249.816616 
L 233.712855 271.149768 
L 235.344285 256.946051 
L 236.975715 253.600777 
L 238.607145 273.707441 
L 240.238575 272.638773 
L 241.870005 272.172613 
L 243.501434 269.13692 
L 245.132864 260.94093 
L 246.764294 230.105962 
L 250.027154 288.849234 
L 251.658584 275.804888 
L 253.290014 238.98934 
L 254.921444 234.974425 
L 256.552873 234.264345 
L 258.184303 228.902838 
L 259.815733 253.898538 
L 261.447163 256.658615 
L 263.078593 254.456756 
L 266.341453 235.439682 
L 267.972883 265.957056 
L 269.604312 251.474684 
L 271.235742 240.004444 
L 272.867172 242.927705 
L 274.498602 246.910583 
L 276.130032 238.181736 
L 277.761462 246.033355 
L 279.392892 231.691459 
L 281.024322 259.227338 
L 282.655751 251.404602 
L 284.287181 241.382426 
L 285.918611 255.72545 
L 287.550041 244.444667 
L 289.181471 229.069589 
L 290.812901 216.555261 
L 292.444331 252.238197 
L 294.075761 239.60298 
L 295.70719 216.980734 
L 297.33862 246.627286 
L 298.97005 228.642498 
L 300.60148 234.061519 
L 302.23291 218.114005 
L 303.86434 224.416342 
L 305.49577 271.781457 
L 307.1272 247.920888 
L 308.75863 239.143039 
L 310.390059 226.494896 
L 312.021489 218.958632 
L 313.652919 254.334305 
L 315.284349 248.085514 
L 316.915779 252.767376 
L 318.547209 236.170664 
L 320.178639 236.450066 
L 321.810069 229.940254 
L 323.441498 249.525762 
L 325.072928 243.659089 
L 326.704358 240.849956 
L 328.335788 246.520569 
L 329.967218 243.574854 
L 331.598648 256.669387 
L 333.230078 253.867513 
L 334.861508 258.022581 
L 338.124367 239.442772 
L 339.755797 258.150374 
L 341.387227 247.578594 
L 343.018657 247.470992 
L 344.650087 251.448778 
L 346.281517 258.233208 
L 347.912947 251.322883 
L 349.544376 260.753145 
L 351.175806 256.125789 
L 352.807236 259.937465 
L 354.438666 263.017927 
L 356.070096 260.963828 
L 357.701526 261.201937 
L 359.332956 261.260965 
L 360.964386 252.121819 
L 362.595815 255.46662 
L 364.227245 258.14131 
L 365.858675 255.685013 
L 367.490105 254.613239 
L 369.121535 264.395876 
L 370.752965 261.863696 
L 372.384395 261.921255 
L 374.015825 258.221637 
L 375.647254 258.703422 
L 377.278684 255.520934 
L 378.910114 263.496 
L 380.541544 261.012254 
L 382.172974 253.158275 
L 383.804404 257.473851 
L 385.435834 252.04953 
L 387.067264 255.30334 
L 388.698693 259.013755 
L 390.330123 263.740136 
L 391.961553 259.794622 
L 393.592983 260.749781 
L 395.224413 263.918788 
L 396.855843 259.456191 
L 398.487273 258.021858 
L 398.487273 258.021858 
" clip-path="url(#pe42bb4d5c4)" style="fill: none"/>
    <defs>
     <path id="m643a3a05e1" d="M 0 0.75 
C 0.198902 0.75 0.389685 0.670975 0.53033 0.53033 
C 0.670975 0.389685 0.75 0.198902 0.75 0 
C 0.75 -0.198902 0.670975 -0.389685 0.53033 -0.53033 
C 0.389685 -0.670975 0.198902 -0.75 0 -0.75 
C -0.198902 -0.75 -0.389685 -0.670975 -0.53033 -0.53033 
C -0.670975 -0.389685 -0.75 -0.198902 -0.75 0 
C -0.75 0.198902 -0.670975 0.389685 -0.53033 0.53033 
C -0.389685 0.670975 -0.198902 0.75 0 0.75 
z
" style="stroke: #000000"/>
    </defs>
    <g clip-path="url(#pe42bb4d5c4)">
     <use xlink:href="#m643a3a05e1" x="73.832727" y="245.285721" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="75.464157" y="252.450903" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="77.095587" y="256.744058" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="78.727017" y="258.259433" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="80.358447" y="249.969704" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="81.989877" y="257.410723" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="83.621307" y="256.358471" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="85.252736" y="258.41343" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="86.884166" y="256.209905" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="88.515596" y="263.689749" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="90.147026" y="263.038313" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="91.778456" y="243.110704" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="93.409886" y="259.261845" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="95.041316" y="261.783994" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="96.672746" y="263.823192" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="98.304175" y="259.808237" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="99.935605" y="262.052764" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="101.567035" y="261.915935" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="103.198465" y="260.160123" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="104.829895" y="263.737386" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="106.461325" y="256.056505" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="108.092755" y="260.217403" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="109.724185" y="259.141825" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="111.355614" y="259.354532" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="112.987044" y="262.409506" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="114.618474" y="261.760121" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="116.249904" y="256.276964" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="117.881334" y="264.827529" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="119.512764" y="255.775369" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="121.144194" y="261.819837" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="122.775624" y="261.837216" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="124.407053" y="261.055945" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="126.038483" y="254.866322" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="127.669913" y="262.939039" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="129.301343" y="260.688147" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="130.932773" y="261.995059" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="132.564203" y="263.453013" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="134.195633" y="255.209405" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="135.827063" y="254.324482" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="137.458492" y="234.762547" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="139.089922" y="254.56588" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="140.721352" y="270.275095" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="142.352782" y="270.032743" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="143.984212" y="262.907845" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="145.615642" y="263.490428" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="147.247072" y="285.409287" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="148.878502" y="271.732989" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="150.509931" y="278.412311" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="152.141361" y="289.623036" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="153.772791" y="261.374548" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="155.404221" y="282.265453" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="157.035651" y="265.634861" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="158.667081" y="295.488" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="160.298511" y="264.7155" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="161.929941" y="274.374762" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="163.56137" y="285.415607" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="165.1928" y="284.718352" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="166.82423" y="251.065095" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="168.45566" y="269.628391" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="170.08709" y="248.047526" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="171.71852" y="238.506075" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="173.34995" y="271.069071" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="174.98138" y="270.786519" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="176.61281" y="255.524839" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="178.244239" y="265.813549" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="179.875669" y="258.955893" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="181.507099" y="250.762983" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="183.138529" y="259.981459" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="184.769959" y="261.990263" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="186.401389" y="260.112961" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="188.032819" y="257.074633" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="189.664249" y="262.814511" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="191.295678" y="256.616437" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="192.927108" y="261.967907" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="194.558538" y="260.861649" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="196.189968" y="250.308689" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="197.821398" y="252.711563" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="199.452828" y="259.642778" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="201.084258" y="259.441819" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="202.715688" y="256.90829" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="204.347117" y="255.258969" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="205.978547" y="248.248472" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="207.609977" y="251.027226" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="209.241407" y="250.798939" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="210.872837" y="256.642916" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="212.504267" y="254.237965" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="214.135697" y="254.929006" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="215.767127" y="246.634941" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="217.398556" y="247.180006" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="219.029986" y="262.801974" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="220.661416" y="261.96804" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="222.292846" y="250.141785" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="223.924276" y="254.667037" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="225.555706" y="242.886144" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="227.187136" y="250.150223" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="228.818566" y="256.361539" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="230.449995" y="256.937758" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="232.081425" y="249.816616" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="233.712855" y="271.149768" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="235.344285" y="256.946051" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="236.975715" y="253.600777" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="238.607145" y="273.707441" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="240.238575" y="272.638773" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="241.870005" y="272.172613" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="243.501434" y="269.13692" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="245.132864" y="260.94093" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="246.764294" y="230.105962" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="248.395724" y="259.816762" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="250.027154" y="288.849234" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="251.658584" y="275.804888" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="253.290014" y="238.98934" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="254.921444" y="234.974425" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="256.552873" y="234.264345" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="258.184303" y="228.902838" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="259.815733" y="253.898538" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="261.447163" y="256.658615" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="263.078593" y="254.456756" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="264.710023" y="244.689391" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="266.341453" y="235.439682" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="267.972883" y="265.957056" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="269.604312" y="251.474684" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="271.235742" y="240.004444" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="272.867172" y="242.927705" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="274.498602" y="246.910583" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="276.130032" y="238.181736" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="277.761462" y="246.033355" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="279.392892" y="231.691459" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="281.024322" y="259.227338" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="282.655751" y="251.404602" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="284.287181" y="241.382426" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="285.918611" y="255.72545" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="287.550041" y="244.444667" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="289.181471" y="229.069589" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="290.812901" y="216.555261" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="292.444331" y="252.238197" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="294.075761" y="239.60298" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="295.70719" y="216.980734" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="297.33862" y="246.627286" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="298.97005" y="228.642498" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="300.60148" y="234.061519" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="302.23291" y="218.114005" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="303.86434" y="224.416342" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="305.49577" y="271.781457" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="307.1272" y="247.920888" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="308.75863" y="239.143039" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="310.390059" y="226.494896" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="312.021489" y="218.958632" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="313.652919" y="254.334305" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="315.284349" y="248.085514" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="316.915779" y="252.767376" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="318.547209" y="236.170664" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="320.178639" y="236.450066" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="321.810069" y="229.940254" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="323.441498" y="249.525762" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="325.072928" y="243.659089" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="326.704358" y="240.849956" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="328.335788" y="246.520569" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="329.967218" y="243.574854" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="331.598648" y="256.669387" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="333.230078" y="253.867513" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="334.861508" y="258.022581" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="336.492937" y="249.008915" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="338.124367" y="239.442772" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="339.755797" y="258.150374" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="341.387227" y="247.578594" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="343.018657" y="247.470992" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="344.650087" y="251.448778" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="346.281517" y="258.233208" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="347.912947" y="251.322883" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="349.544376" y="260.753145" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="351.175806" y="256.125789" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="352.807236" y="259.937465" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="354.438666" y="263.017927" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="356.070096" y="260.963828" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="357.701526" y="261.201937" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="359.332956" y="261.260965" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="360.964386" y="252.121819" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="362.595815" y="255.46662" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="364.227245" y="258.14131" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="365.858675" y="255.685013" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="367.490105" y="254.613239" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="369.121535" y="264.395876" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="370.752965" y="261.863696" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="372.384395" y="261.921255" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="374.015825" y="258.221637" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="375.647254" y="258.703422" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="377.278684" y="255.520934" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="378.910114" y="263.496" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="380.541544" y="261.012254" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="382.172974" y="253.158275" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="383.804404" y="257.473851" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="385.435834" y="252.04953" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="387.067264" y="255.30334" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="388.698693" y="259.013755" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="390.330123" y="263.740136" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="391.961553" y="259.794622" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="393.592983" y="260.749781" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="395.224413" y="263.918788" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="396.855843" y="259.456191" style="stroke: #000000"/>
     <use xlink:href="#m643a3a05e1" x="398.487273" y="258.021858" style="stroke: #000000"/>
    </g>
   </g>
   <g id="line2d_20">
    <path d="M 73.832727 261.644859 
L 398.487273 261.644859 
L 398.487273 261.644859 
" clip-path="url(#pe42bb4d5c4)" style="fill: none; stroke-dasharray: 3.7,1.6; stroke-dashoffset: 0; stroke: #7f7f7f"/>
   </g>
   <g id="line2d_21">
    <path d="M 254.921444 346.6 
L 254.921444 -1 
" clip-path="url(#pe42bb4d5c4)" style="fill: none; stroke-dasharray: 5.55,2.4; stroke-dashoffset: 0; stroke: #808080; stroke-width: 1.5"/>
   </g>
   <g id="patch_3">
    <path d="M 57.6 307.584 
L 57.6 41.472 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 414.72 307.584 
L 414.72 41.472 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_5">
    <path d="M 57.6 307.584 
L 414.72 307.584 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_6">
    <path d="M 57.6 41.472 
L 414.72 41.472 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="pe42bb4d5c4">
   <rect x="57.6" y="41.472" width="357.12" height="266.112"/>
  </clipPath>
 </defs>
</svg>

Violet dots show the experimental data, orange line is the best fit between the experimental data and the reference spectrum, grey vertical line corresponds to the initial guess for the C-O peak and black dots are the residuals of the best fit. 
