---
layout: blog
teaser: no
header: no
breadcrumb: true
#
# Content
#
title: "Domain adaptation"
categories:
  - Research
---

The problem of domain adaptation concerns with adapting a  model (e.g. a classifier) on one particular domain (source domain) to be applicable in a different domain (target domain). The main difficulty in doing so is that the distributions from which data points $$(x, y)$$ are sampled differ between the source and the target domains. This can be a severe problem in many practical applications such as developing systems to diagnose diseases where it is relatively easy to obtain samples from patients diagnosed with that particular disease but difficult to obtain samples from healthy individuals. Even if we obtain samples from healthy individuals, those samples might be clearly different from the patients with the particular disease that we are interested in detecting automatically. Therefore, we can in practice design systems that obtain near perfect classification accuracies with training data but perform very poorly on test data (in the wild). Therefore, domain adaptation is an important research problem that has been studied extensively in the field on machine learning.

In domain adaptation there can be two main scenarios. 
The first case is where we have the conditional distributions $$p(y|x)$$ fixed across source and target domains but the marginals $$p(x)$$ are different. 
This case is known as the covariate shift. The second scenario is when we have $$p(x)$$ is the same but label distributions, $$p(y|x)$$ are different across source and target domains.

This [blog post](https://blog.smola.org/post/4110255196/real-simple-covariate-shift-correction) by Alex Smola presents a simple approach to overcome the on covariate shift. The idea is to re-weight each sample by the ratio \frac{p_t(x)}{p_s(x)}. Of course, the real problem here is that how to estimate this ratio because we do not know the actual distributions. One solution is to train a binary classifier that tells whether a particular instance is sampled from the source distribution or the target distribution. The nice thing here is that this can be done with unlabeled data because we are not interested in predicting the class label for the instances but simply their domain. Any classifier that can return class conditional probabilities would do. A simple choice would be the logistic regression. On a side note, despite the word *regression* here, it is actually a classification model and not a regression model.

After reading the above-mentioned blog post, you might wonder how would different classification algorithms cope with sample selection bias. This paper investigates the effect on sample selection bias on popular binary classifiers such as Bayesian classifiers, naive Bayes, logistic regression, C 4.5 decision tree learner, and Support Vector Machines (soft and hard margin versions).

The paper introduces a notation (x, y, s) where x are features, y are labels and s is an indicator variable that denotes whether we have selected this particular instance (x, y) from a distribution D as training data or otherwise. Four cases are analyzed.

1. $$x$$ and $$y$$ are independent of $$s$$. (no selection bias here)
1. $$s$$ is independent of $$y$$ given $$x$$.  There is a biasedness only on the feature vector $$x$$.
1. $$s$$ is independent of $$x$$ given $$y$$. There is a bias but only on the label $$y$$. This can be resolved by using a cost-matrix.
1. $$s$$ depends on both $$x$$ and $$y$$. There is a bias but this case is too difficult to analyze.

The paper focuses on the second case and shows that there are two types of classifier learners: local and global. 
Local classifiers model $$p(y|x)$$ and and global classifiers model $$p(x)$$. 
Note that this distinction is closely related to the discriminative vs. generative classification. 
It turns out that, local classifiers are not affected (asymptotically speaking) by the sample selection bias and the global classifiers do get affected by it. 
Also it is shown in the paper that Bayesian classifier, logistic regression, and SVM (hard margin) are local classifiers whereas, naive Bayes, decision tree learner, and SVM (soft margin) are global classifiers. 
Although it looks as if one should never use global classifiers it must also be pointed out that they can incorporate unlabeled data and can be useful in semi-supervised settings. 
Of course, the argument as to discriminative vs. generative is a more subtle one and it can be shown that although the asymptotical empirical error of a discriminative learner is lower than its generative counter part (selected from the same hypothesis class), the generative version reaches this asymptotical error more quickly (requiring logarithmic amount of examples) whereas, the amount of examples required by the discriminative version is linear. Therefore, there are two regimes that concerns the two types of learners in theory. For more details on this matter see this paper.


<!-- 

1. $$x$$ and $$y$$ are independent of $$s$$. (no selection bias here)
1. $$s$$ is independent of $$y$$ given $$x$$  There is a biasedness only on the feature vector $x$.
1. $$s$$ is independent of $$x$$ given $$y$$ ($$p(s|x, y) = p(s|y)$$). There is a bias but only on the label $$y$$. This can be resolved by using a cost-matrix.
1. $$s$$ depends on both $$x$$ and $$y$$. There is a bias but this case is too difficult to analyze.
-->
