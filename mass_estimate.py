import math
import numpy as np

#this code takes an inner disk temperature estimate and returns a mass, and associated error

Msol = 1.988435 * 10.**30. #mass of the sun in kg

def M(Teff): #calculates the mass of the black hole in solar masses
    Mass = 10./(Teff**4.0)
    return Mass

def Merr(T,higherr,lowerr,): #calculates 1.6 sigma error on mass estimate
	Merrlow = higherr*4.*10./(T**3.)
	Merrhigh = lowerr*4.*10/(T**3.)
	return Merrlow,Merrhigh

Teff = input("Enter the inner disk Temperature: ")
higherr = input("Enter the upper bound for your temperature from conf: ")
lowerr = input("Enter the lower bound for your Temperature from conf: ")

Mass = M(Teff)
Masskg = Mass * Msol #returns the mass of the black hole in kg
Masserr = Merr(Teff,higherr,lowerr)

print "The mass of the black hole in solar masses is: ", Mass
print "The mass of the black hole in kg is: ", Masskg
print "The one sigma error on your mass estimate in solar masses is: +", str(Masserr[1])+" and     -",str(Masserr[0])

