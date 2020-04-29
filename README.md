# ASTR6410 Final ReadMe
In this project, I analyzed data from NuSTAR for two different galaxies, M81 and NGC 3628. This involved downloading the data from the NuSTAR archive, processing that data, extracting spectra from each source, and modelling that spectra. The end goal was to obtain and compare mass measurements from these NuSTAR observations with measurements of those same sources that I previously made with Chandra.

I pulled data from the NuSTAR archive using the process decribed in pull_data.txt. The background subtraction and modelling was completed using a series of codes provided by Dan Wik. The process by which I was able to produce these files is described in bgd_cookboox.txt, which is a slightly modified version of an original "cookbook.txt" file provided by Dan. The commands are run in order that they appear in bgd_cookbook, and are run in idl. They generate background regions and background-subtracted fits files of each observation. The various .pro files contained in this repository are all supporting files to run the processes described in bgd_cookbook. The process for extracting source spectra and modelling those sources is described in specextract.txt. I attempted to automate the modelling process in python, but learned that the python implementation is Xspec has a number of problems and is unable to modify model parameters such as setting the minimum value of a given parameter. As a result, the process for modelling the spectra within Xspec is described in plaintext, to be cope/pasted into the terminal in the order described. 

I chose to model the spectra of the sources in M 81 and NGC 3628 with the diskbb model, provided in xspec. This model assumes a thin, multi-color disk around a compact object, and find the best fit for the inner disk temperature and normalization parameters, where the normalization factor describes the relationship between the distance to and inclination of the disk. I also included a Tuebingen-Boulder ISM absorption model, which was multiplied by the diskbb model. These models were chosen in order to compare with the results I found using Chandra for these same sources. Due to the fact that the counts were grouped in threes when generating the spectra, I utilized chi squared gehrels statistics to determine the goodness of the fit. Good fits were determined by the nearness of the reduced statistic to 1. Finally, I wrote a short code in python to ask for the value of the inner disk temperature reported by the model and its respective errors, and provide a lower limit for the mass of the compact object, along with the error on that measurement. The errors provided are within the 90% confidence, or 1.6 sigma interval. 

I found that for all of my sources with NuSTAR, the masses I got for each were unrealistically low. As an example, the mass estimate for the soucre in NGC 3628 was 0.15 Solar masses. This is an unrealistic value, especially when compared to the 2.4 Solar masses I got for the same object when I did my analysis with Chandra. However, after talking to Dan about why that may be, he suggested that NuSTAR really isn't very good when it comes to lower energies, like the 2.8 keV I got for the inner disk temperature when I modeled the spectrum from the NuSTAR data. In the future, I'd like to try to simultaneously fit NuSTAR and Chandra spectra together, so that Chandra can handle the lower energy range, and NuSTAR the high energy range. An example of the plotted spectrum and folded disk model are provided for the source in NGC 3628.

The final values I calculated for the lower limit of the mass of my 3 sources (in Solar masses) are as follows:

NGC 3628:
Obsid 60371004002:   
	Tin:  2.83696      +/-  -0.260989,+0.289499
  Mass: 0.15 Solar Masses +/- 0.36

M81:
Obsid 50401004002:
		Tin: 6.16547      +/-  0.510406
    Mass: 6.9e-3 +/- + 0.087111841711
		
Obsid 60101049002:
		T: 29.1722      +/-  2.27727 
	  Mass: 1.4e-5 +/- 0.00366916269399
