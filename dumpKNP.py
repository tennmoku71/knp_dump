#!/usr/bin/env python
# coding: utf-8
import pyknp
import pickle
import os

class KNP():

    original_knp = ""

    def __init__(self):
        self.original_knp = pyknp.KNP()
        self.knp_dict = {}
        if os.path.exists('knp.pickle'):
            self.load()
    
    def save(self):    
        with open('knp.pickle', mode='wb') as f:
            pickle.dump(self.knp_dict, f)
        
    def load(self):
        with open('knp.pickle', mode='rb') as f:
            self.knp_dict = pickle.load(f)

    def parse(self,utterance):
        if utterance in self.knp_dict.keys():
            return self.original_knp.result(self.knp_dict[utterance])
        else:
            result = self.original_knp.parse(utterance)
            self.knp_dict[utterance]=result.all()
            return result
