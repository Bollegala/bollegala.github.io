---
permalink: /software/
layout: frontpage
header: no
title:  Software
---

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
 for Cross-Domain Sentiment Classification](../papers/danushka_ACL_2011.pdf).

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



