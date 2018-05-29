#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 10:22:54 2018

@author: prmiles
"""

from pymcmcstat.chain import ChainStatistics
import unittest
import numpy as np

def removekey(d, key):
        r = dict(d)
        del r[key]
        return r

CS = ChainStatistics
chain = np.random.random_sample(size = (1000,2))
    
# --------------------------
# chainstats
# --------------------------
class Chainstats_Eval(unittest.TestCase):
    
    def test_cs_eval_with_return(self):
        stats = CS.chainstats(chain = chain, returnstats = True)
        self.assertTrue(isinstance(stats,dict))
        
    def test_cs_eval_with_no_return(self):
        stats = CS.chainstats(chain = chain, returnstats = False)
        self.assertEqual(stats, None)