#https://pypi.org/project/PyNeuro/
#pip install PyNeuro -> terminal
from PyNeuro.PyNeuro import PyNeuro
from time import sleep
#delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, highGamma.
pn = PyNeuro()

def attention_callback(attention_value):
    """this function will be called everytime NeuroPy has a new value for attention"""
    print ("Value of attention is: ", attention_value)
    return None
def meditation_callback(meditation_value):
    """this function will be called everytime NeuroPy has a new value for meditation"""
    print ("Value of meditation is: ", meditation_value)
    return None
    
def delta_callback(delta_value):
    """this function will be called everytime NeuroPy has a new value for delta"""
    print ("Value of delta is: ", delta_value)
    return None
def theta_callback(theta_value):
    """this function will be called everytime NeuroPy has a new value for theta"""
    print ("Value of delta is: ", theta_value)
    return None

def lowalpha_callback(lowalpha_value):
    """this function will be called everytime NeuroPy has a new value for lowalpha"""
    print ("Value of lowalpha is: ", lowalpha_value)
    return None
def highalpha_callback(highalpha_value):
    """this function will be called everytime NeuroPy has a new value for highalpha"""
    print ("Value of highalpha is: ", highalpha_value)
    return None

def lowbeta_callback(lowbeta_value):
    """this function will be called everytime NeuroPy has a new value for lowbeta"""
    print ("Value of lowbeta is: ", lowbeta_value)
    return None
def highbeta_callback(highbeta_value):
    """this function will be called everytime NeuroPy has a new value for highbeta"""
    print ("Value of highbeta is: ", highbeta_value)
    return None

def lowgamma_callback(lowgamma_value):
    """this function will be called everytime NeuroPy has a new value for lowgamma"""
    print ("Value of lowgamma is: ", lowgamma_value)
    return None
def highgamma_callback(highgamma_value):
    """this function will be called everytime NeuroPy has a new value for highgamma"""
    print ("Value of highgamma is: ", highgamma_value)
    return None

pn.set_attention_callback(attention_callback)
pn.set_meditation_callback(meditation_callback)
pn.set_delta_callback(delta_callback)
pn.set_theta_callback(theta_callback)
pn.set_lowAlpha_callback(lowalpha_callback)
pn.set_highAlpha_callback(highalpha_callback)
pn.set_lowBeta_callback(lowbeta_callback)
pn.set_highBeta_callback(highbeta_callback)
pn.set_lowGamma_callback(lowgamma_callback)
pn.set_highGamma_callback(highgamma_callback)

pn.connect()
pn.start()