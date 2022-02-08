import nltk
from java.util import Random

class NLPPresentation(Random):
    def nextDouble(self):
        return 1
    def TagByBrown(self,sent):
        "@sig public String[] TagByBrown(String sent)"
        brown_a = nltk.corpus.brown.tagged_sents(categories='a')
        bigram_tagger = nltk.BigramTagger(brown_a, cutoff=0)
        lst = bigram_tagger.tag(sent.split())
        return lst