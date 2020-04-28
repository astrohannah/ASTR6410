# ASTR6410 Final ReadMe
In this project, I analyzed data from NuSTAR for two different galaxies, M81 and NGC 3628. This involved downloading the data from the NuSTAR archive, processing that data, extracting spectra from each source, and modelling that spectra. The end goal was to obtain and compare mass measurements from these NuSTAR observations with measurements of those same sources that I previously made with Chandra.

The background subtraction and modelling was completed using a series of codes provided by Dan Wik. The process by which I was able to produce these files is described in bgd_cookboox.txt, which is a slightly modified version of an original "cookbook.txt" file provided by Dan. The commands are run in order that they appear in bgd_cookbook, and are run in idl. They generate background regions and background-subtracted fits files of each observation. The process for extracting source spectra and modelling those sources is described in specextract.txt. I attempted to automate the modelling process in python, but learned that the python implementation is Xspec has a number of problems and is unable to modify model parameters such as setting the minimum value of a given parameter. As a result, the process for modelling the spectra within Xspec is described in plaintext, to be cope/pasted into the terminal in the order described. 

I chose to model the spectra of the sources in M 81 and NGC 3628 with the diskbb model, provided in xspec. This model assumes a thin, multi-color disk around a compact object, and find the best fit for the inner disk temperature and normalization parameters, where the normalization factor describes the relationship between the distance to and inclination of the disk. I also included a Tuebingen-Boulder ISM absorption model, which was multiplied by the diskbb model. These models were chosen in order to compare with the results I found using Chandra for these same sources. Due to the fact that the counts were grouped in threes when generating the spectra, I utilized chi^2 gehrels statistics to determine the goodness of the fit. INSERT STUFF HERE ABOUT GOODNESS OF FIT. Finally, I wrote a short code in python to take the value of the inner disk temperature reported by the model and its respective errors, and provide a lower limit for the mass of the compact object, along with the error on that measurement. The errors provided are within the 90% confidence, or 1.6 sigma interval. 
