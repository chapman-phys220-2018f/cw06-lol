#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name:Gabriella Nutt and Gwenyth
#Student ID: 2307512
#Email: nutt@chapman.edu
#Course: PHYS220/MATH220/CPSC220 Fall 2018
#Assignment: CW 5
###

import numpy as np
from scipy import constants
import pandas as pd 
import sympy as sp 
import matplotlib.pyplot as plt 
import seaborn as sb 
"""This module is to practice using classes in 
python. Our class will be called Particle. """ 
 
class Particle(object):
    """A particle is a constituent unit of the universe.
        Attributes
        ----------
        p : momentum in units of [kgm/s]
        m : mass in units of [kg]
        r : position in units of [meters]

        Scopatz, Anthony; Huff, Kathryn D.. Effective Computation in Physics: Field Guide to Research with Python """
    
    
 
    def __init__(self, x , y , z):
        """Initializes the particle with supplied values for mass m, momentum p and position r."""
        
        self.m = 1.0
        self.r = (x, y, z)
        self.p = (0.0,0.0,0.0)
        
 
    def impulse(self, px, py, pz):
        """ "takes three floats as increments for an impulse that changes the
            momentum attribute by adding the increments (px, py, pz) to the existing momentum values."
            (wise words of Dr.Dressel)

            expexted to get impulse with units of Ns = J (Jules)
        """
        self.p = (0.0 + px, 0.0 + py, 0.0 + pz)
           
    
 
    def move(self, dt):
        """ "moves the particle by one time increment dt by using its current momentum and
             mass values to update its position to a new value" (wise words of Dr.Dressel)

             when momentum is multiplied by time it results in position

            Unit value expected is meters
        """
        self.dt = dt

        self.r = (self.p)*(self.dt)

class ChargedParticle(Particle):
            """ ChargedParticle is a subclass of the class Particle
                Attribute
                ----------
                c : charge in units [q] coulumbs
            """
            charge = constants.elementary_charge

            def __init__(self, charge):

                self.c = charge


class Eletron(ChargedParticle):
                    """ Electron is a subclass of ChargedParticle
                        Attribute
                        ----------
                        e : electron has mass [m_e] = and charge = 
                    """
                    def __init__(self, charge, mass):
                        self.charge = charge
                        self.m = constants.m_e

class Proton(ChargedParticle):
                    """ Proton is a subclass of ChargedParticle
                        Attribute
                        ----------
                        p : proton has mass [m_p] = and charge = 
                    """
                    def __init__(self, charge, mass):
                        self.m = sc.constants.m_p
                        self.charge = charge
