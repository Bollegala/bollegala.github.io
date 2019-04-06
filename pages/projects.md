---
permalink: /projects/
layout: frontpage
header: no
title:  Projects
---

Research Topics/Projects
=========================

Meta embedding Learning
-------------------------
I have been working on word meta embedding learning recently, which is the task of combining multiple pre-trained word embeddings to learn more accurate and wide-coverage word embeddings. This task is important because different word embedding learning methods capture different aspects of words (sense-specific embeddings, morphological embeddings, cross-lingual embeddings etc.) and it is non-obvious as how to combine these different methods (potentially learnt on different resources such as social media, Web crawled texts, news articles etc.) to learn better word embeddings by preserving the complementary strengths. 
In our IJCAI-18 paper titled Think Globally, Embed Locally -- Locally Linear Meta-Embedding of Words, we proposed a method that preserve local neighbourhood information in word embedding spaces for the purpose of learning better meta embeddings. In our NAACL-18 paper titled Frustratingly Easy Meta-Embedding -- Computing Meta-Embeddings by Averaging Source Word Embeddings I showed that it is possible to create good quality meta-embedding by simply averaging word embeddings although mathematically it is not possible to add vectors in different vector spaces. We proved the mathematical conditions where such an addition is meaningful. In our COLING-18 paper titled  Learning Word Meta-Embeddings by Autoencoding we proposed a method for learning meta-embeddings using denoising autoencoders.

Embedding learning theory
-----------------------------
Despite the large body of empirical work on learning accurate word or relation representations, the theoretical understanding of these methods and the properties of the embeddings learnt by those methods remains unclear. Motivated by this, and in an attempt to develop theoretical tools to analyse word/relation embeddings, I have recently started to looked into this problem.

In our AAAI-18 paper titled Using k-way Co-occurrences for Learning Word Embeddings, we extended the Random Walk model originally proposed by Arora et al 2015 for explaining word embeddings, to sentences that contain co-occurrences of k-words. The extension is nontrivial and require developing new analysis tools and empirically justifying the baseline assumptions. The fact that k-way co-occurrences are sparser compared to co-occurrences of two words make the experiments complicated.

In our COLING-18 paper titled Why does PairDiff work? - A Mathematical Analysis of Bilinear Relational Compositional Operators for Analogy Detection we prove that vector offset is an accurate relation representation when several properties are assumed about the word embeddings used.


Software
================

Licensing
----------
Below, you can find the implementations for various algorithms and systems proposed in my papers.
These software are provided under the [modified BSD license](http://www.opensource.org/licenses/bsd-license.php).
Please feel free to use them in your research work. 
I would be grateful if you can kindly let me know when you use these software and cite the appropriate papers. 
Moreover, please let me know if you find any bugs in these software.
Thanks in advance.

Cross Domain Distribution Prediction
-------------------------------------
 Distribution of a word can vary from one domain (eg. corpus, category) to another. 
 In distributional semantics, the meaning of  a word is represented using its distribution over other words in a corpus. Therefore, the ability to accurately predict how the
 distribution of a word changes across domains is in an important first steps towards capturing the meaning variations
 of words across domains. Our ACL 2014 paper titled [Learning to Predict Distributions of Words across Domains](../papers/ACL_2014.pdf) proposes an unsupervised approach for predicting the distribution
 of a word across domains. The source code for the proposed method is available [here](../data/CrossSim.zip).


SVDMI
------
A tool developed in Python to perform common preprocessing tasks in NLP such as Positive Pointwise Mutual Information (PPMI) computation on co-occurrence matrices, Singular Value Decomposition (SVD)-based dimensionarity reduction/smoothing, and Partial Least Square Regression (PLSR)-based distribution prediction. Available [here](https://github.com/Bollegala/svdmi).


WebSim
---------------------------------------------------
This package implements the method proposed in our WWW 2007 paper for
measuring the semantic similarity between words using both co-occurrence
counts as well as lexical patterns extracted from a web search
engine. For further details on the WebSim software please refer its [website](../WebSim.html).
 

Cross Domain Sentiment Analysis
--------------------------------

 Here is the [source code](../data/SST.tgz) for the cross-domain sentiment
 classification method we proposed in our ACL 2011
 paper titled [Using Multiple Sources to Construct a Sentiment Sensitive Thesaurus
 for Cross-Domain Sentiment Classification](https://github.com/Bollegala/SST).

Spectral RelAdapt
--------------------------------------------

Here is the code, and the data
for the relation adaptation method described in this [paper](../papers/danushka_IJCAI_2011.pdf)
can be download [here](../RA/)

Evaluating Sentence Orderings
-----------------------------

We introduced a novel measure, average continuity, to compare a set of ordered sentences by 
an automatic multi-document summarization system. 
[Download](../data/Correlation.py) a python script to compute
average continuity as well as other popular correlation coefficients such as,
Kendall rank correlation coefficient and Spearman coefficient with confidence intervals.



