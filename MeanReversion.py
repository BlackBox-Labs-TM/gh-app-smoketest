# Edit made here to trigger audit.

import sympy as smp
from sympy import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import log, sqrt, e, pi, exp
from scipy.optimize import minimize
from scipy.optimize import minimize_scalar
from scipy.optimize import fsolve
from scipy.integrate import quad
from functools import lru_cache
# class OptimalStopping:
#     '''
#     Provides the optimal entry d and optimal exit b
#     '''
#     def __init__(self, my, sigma, theta, r, c):
#         self.my = my
#         self.sigma = sigma
#         self.theta = theta
#         self.r = r
#         self.c = c
#         self.u_symbol, self.x_symbol = smp.symbols("u x", real=True)
#         self.integrandF = self.u_symbol ** (self.r / self.my - 1) * smp.exp((smp.sqrt(2 * self.my / self.sigma**2) * (self.x_symbol - self.theta) * self.u_symbol - self.u_symbol**2 / 2))
#         self.integrandG = self.u_symbol ** (self.r / self.my - 1) * smp.exp((smp.sqrt(2 * self.my / self.sigma**2) * (self.theta - self.x_symbol) * self.u_symbol - self.u_symbol**2 / 2))
#         self.derivativeF = smp.diff(self.integrandF, self.x_symbol)
#         self.derivativeG = smp.diff(self.integrandG, self.x_symbol)
    
#     @lru_cache(maxsize=None)
#     def F(self, x):
#         '''
#         Function F (3.3)
#         '''
#         return complex(smp.integrate(self.integrandF.subs(self.x_symbol, x), (self.u_symbol, 0, smp.oo)).evalf()).real

#     @lru_cache(maxsize=None)
#     def f(self, x):
#         '''
#         Derivative of function F
#         '''
#         return complex(smp.integrate(self.derivativeF.subs(self.x_symbol, x), (self.u_symbol, 0, smp.oo)).evalf()).real

#     def G(self, x):
#         '''
#         Function G (3.4)
#         '''
#         return complex(smp.integrate(self.integrandG.subs(self.x_symbol, x), (self.u_symbol, 0, smp.oo)).evalf()).real
    
#     def g(self, x):
#         '''
#         Derivative of function G
#         '''
#         return complex(smp.integrate(self.derivativeG.subs(self.x_symbol, x), (self.u_symbol, 0, smp.oo)).evalf()).real
    
#     def b(self):
#         '''
#         Optimal Liquidation Level b (4.3)
#         '''
#         def optFunction(b):
#             return float(abs(self.F(b) - (b - self.c) * self.f(b)))
#         result = minimize_scalar(optFunction, bounds=(0, 1), method='bounded')
#         return result.x
    
#     def V(self, x):
#         '''
#         Function V (4.2)
#         '''
#         if x < self.b():
#             return (self.b() - self.c) * (self.F(x) / self.F(self.b()))
#         else:
#             return (x - self.c)
     
#     def v(self, x):
#         '''
#         Derivative of function V
#         '''
#         if x < self.b():
#             return (self.b() - self.c) * (self.f(x) / self.F(self.b()))
#         else:
#             return (1)
    
#     def d(self):
#         '''
#         Optimal Entry Level d (4.11)
#         '''
#         def optFunction(d):
#             return float(abs(self.G(d) * (self.v(d) - 1) - (self.g(d) * (self.V(d) - d - self.c))))
#         upperBound = self.b()
#         result = minimize_scalar(optFunction, bounds=(0, upperBound), method='bounded')
#         return result.x

class OptimalStopping:
    '''
    Provides the optimal entry d and optimal exit b
    '''
    def __init__(self, my, sigma, theta, r, c):
        self.my = my
        self.sigma = sigma
        self.theta = theta
        self.r = r
        self.c = c

    @lru_cache(maxsize=None)
    def integrandF(self, u, x):
        return u ** (self.r / self.my - 1) * np.exp(
            np.sqrt(2 * self.my / self.sigma**2) * (x - self.theta) * u - u**2 / 2
        )

    def integrandG(self, u, x):
        return u ** (self.r / self.my - 1) * np.exp(
            np.sqrt(2 * self.my / self.sigma**2) * (self.theta - x) * u - u**2 / 2
        )

    @lru_cache(maxsize=None)
    def derivativeF(self, u, x):
        # Numerical derivative with respect to x
        h = 1e-5
        return (self.integrandF(u, x + h) - self.integrandF(u, x - h)) / (2 * h)

    def derivativeG(self, u, x):
        h = 1e-5
        return (self.integrandG(u, x + h) - self.integrandG(u, x - h)) / (2 * h)

    def F(self, x):
        val, _ = quad(self.integrandF, 0, np.inf, args=(x,))
        return val

    def f(self, x):
        val, _ = quad(self.derivativeF, 0, np.inf, args=(x,))
        return val

    def G(self, x):
        val, _ = quad(self.integrandG, 0, np.inf, args=(x,))
        return val

    def g(self, x):
        val, _ = quad(self.derivativeG, 0, np.inf, args=(x,))
        return val

    def b(self):
        def optFunction(b):
            return float(abs(self.F(b) - (b - self.c) * self.f(b)))

        eq_std_dev = self.sigma / np.sqrt(2 * self.my)
        search_bounds = (self.theta - 10 * eq_std_dev, self.theta + 10 * eq_std_dev)

        result = minimize_scalar(optFunction, bounds=search_bounds, method='bounded')
        return result.x

    def V(self, x):
        if x < self.b():
            return (self.b() - self.c) * (self.F(x) / self.F(self.b()))
        else:
            return (x - self.c)

    def v(self, x):
        if x < self.b():
            return (self.b() - self.c) * (self.f(x) / self.F(self.b()))
        else:
            return 1

    def d(self):
        def optFunction(d):
            return float(abs(self.G(d) * (self.v(d) - 1) - (self.g(d) * (self.V(d) - d - self.c))))
        
        exit_b = self.b() 
        eq_std_dev = self.sigma / np.sqrt(2 * self.my)
        search_bounds = (exit_b - (10 * eq_std_dev), exit_b) 

        result = minimize_scalar(optFunction, bounds=search_bounds, method='bounded')
        return result.x
