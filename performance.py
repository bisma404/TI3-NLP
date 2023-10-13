
"""
TODO: Gunakan file performance.py ini untuk membuat class Performance yang 
nantinya akan digunakan untuk menghitung akurasi (Best Match Accuracy & Candidate Match) 
dan run-time
"""

import json
import time

class Performance():

    def __init__(self):
        f = open('./saltik_200.json')
        self.data = json.load(f)

    def best_match_acc(self, match):
        self.match = match
        my_dict = self.data

        M = sum(1 for word, error in my_dict.items() for typo in error if self.match.get_candidates(typo['typo'], 2)[0] == word)
        N = sum(1 for word in my_dict for error in my_dict[word])

        acc = M / N * 100
        return acc

    def candidate_match(self, candidate):
        self.candidate = candidate
        my_dict = self.data

        M = sum(1 for word, error in my_dict.items() for typo in error if word in self.candidate.get_candidates(typo['typo'], 2))
        N = sum(1 for word in my_dict for error in my_dict[word])

        acc = M / N * 100
        return acc
