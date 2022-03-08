"""
Created on Wed Mar  2 18:14:12 2022
@author: SAMIR
"""

from AttackFunctions import DDosAttack


site = input("IP: ")
target = DDosAttack(site)
target.begin()