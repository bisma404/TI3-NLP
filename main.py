from performance import Performance
from trie_structure.levenshtein_trie import LevenshteinTrie
from trie_structure.damerau_levenshtein_trie import DamerauLevenshteinTrie
from dict_structure.levenshtein_dict import LevenshteinDict
from dict_structure.damerau_levenshtein_dict import DamerauLevenshteinDict
import json
import time


""" 
TODO: Hitung akurasi dan Run-Time dari semua algoritma yang sudah disediakan, seperti 
LevenshteinTrie, DamerauLevenshteinTrie, LevenshteinDict, dan DamerauLevenshteinDict. 
Gunakan SALTIK (https://github.com/ir-nlp-csui/saltik) sebagai dataset 
dan atur parameter MAX_COST untuk setiap algoritma sebesar 2 ketika memanggil 
fungsi untuk pengambilan kandidat.
"""
def main():

    l_trie = LevenshteinTrie('./bahasa-indonesia-dictionary.txt')
    dl_trie = DamerauLevenshteinTrie('./bahasa-indonesia-dictionary.txt')
    l_dict = LevenshteinDict('./bahasa-indonesia-dictionary.txt')
    dl_dict = DamerauLevenshteinDict('./bahasa-indonesia-dictionary.txt')

    performance = Performance()

    # l_trie
    l_trie_start = time.perf_counter()
    bma_l_trie = performance.best_match_acc(l_trie)
    cm_l_trie = performance.candidate_match(l_trie)
    l_trie_end = time.perf_counter()
    l_trie_time_elapsed = l_trie_end - l_trie_start
                    
    # dl_trie
    dl_trie_start = time.perf_counter()
    bma_dl_trie = performance.best_match_acc(dl_trie)
    cm_dl_trie = performance.candidate_match(dl_trie)
    dl_trie_end = time.perf_counter()
    dl_trie_time_elapsed = dl_trie_end - dl_trie_start

    # l_dict
    l_dict_start = time.perf_counter()
    bma_l_dict = performance.best_match_acc(l_dict)
    cm_l_dict = performance.candidate_match(l_dict)
    l_dict_end = time.perf_counter()
    l_dict_time_elapsed = l_dict_end - l_dict_start

    # dl_dict
    dl_dict_start = time.perf_counter()
    bma_dl_dict = performance.best_match_acc(dl_dict)
    cm_dl_dict = performance.candidate_match(dl_dict)
    dl_dict_end = time.perf_counter()
    dl_dict_time_elapsed = dl_dict_end - dl_dict_start

    metrics = '''
    Bisma Nurrauf - 2006525596
    ----------lev_trie----------
    best accuracy:  {}
    candidate accuracy:  {}
    total_time:  {}
    ----------dalev_trie----------
    best accuracy:  {}
    candidate accuracy:  {}
    total_time:  {}
    ----------lev_dict----------
    best accuracy:  {}
    candidate accuracy:  {}
    total_time:  {}
    ----------dalev_dict----------
    best accuracy:  {}
    candidate accuracy:  {}
    total_time:  {}
    '''.format(
        bma_l_trie,
        cm_l_trie,
        l_trie_time_elapsed,
        bma_dl_trie,
        cm_dl_trie,
        dl_trie_time_elapsed,
        bma_l_dict,
        cm_l_dict,
        l_dict_time_elapsed,
        bma_dl_dict,
        cm_dl_dict,
        dl_dict_time_elapsed
    )

    print(metrics)

if __name__ == '__main__':
    main()