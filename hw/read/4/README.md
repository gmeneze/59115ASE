#Reading Assignment # 4

## Date: September 15, 2015

### Summary of _A systematic and comprehensive investigation of methods to build and evaluate fault prediction models_ [1]

#### Download link
http://tiny.cc/32be3x

#### Keywords
* ii1: _Fault Prediction Models_: "binary classifiers typically developed using one of the supervised learning techniques from either a subset of the fault data from the current project or from a similar past project." [2]
* ii2: _Fault Proneness_: "the number of defects detected in a software component (e.g., class)" [1]
* ii3: _Cost-Effectiveness_: refers to the return on investment of time and resources expended to acheive a desired outcome.  In the context of this paper, _cost-effectiveness_ is measured per model by the ratio of the percentage of the number of lines of code examined (% NOS) to the percentage of totals faults discovered (% faults).  _Cost effectiveness_ is used as a variable for success criteria.
* ii4: _Verification_: in testing, the act of ensuring that a particular software system meets specifications and meets its intended purpose [3]

#### Key Points
* iii1: _Motivational Statements_: After performing a literature review of select publications within the field of fault-proneness prediction models, the authors found that none addressed the impact of _selecting_ any particular modeling technique for fault prediction.  Therefore, the authors focus the paper on the systematic assessment of three aspects on how to build and evaluate fault-proneness models in context of a Java legacy system development project in an industrial setting.  These three aspects are:
  * "compare many data mining and machine learning techniques to build fault-proneness models"
  * "assess the impact of using different metric sets" (e.g., source code structural measures, change history)
  * "compare several alternative ways of assessing the performance of the models", including:
    * confusion matrix criteria
    * ranking ability
    * author-proposed cost-effectiveness measure
* iii2: _Related Works_: Gathered in the aforementioned literature review, the authors present accounts of multiple fault prediction models in previous works, which they intend to use in their experiment. The authors note in response to related works that existing studies only considered "code structural metrics", and only a subset of studies included any further measures. The authors note that there exist a few studies which compare a comprehensive set of data mining techniques for building fault prediction models; though, none were performed systematically nor did they attempt to evaulate the benefits of including particular structural measures, such as code churn and process measures. Models gleaned from related works include:
  *  Neural Network
  *  Decorate C4.5
  *  SVM
  *  Logistic Regression
  *  Boost C4.5
  *  PART
  *  C4.5 + Part
  *  C4.5
* iii3:
* iii4:

#### Suggestions for Improvement
* iv1:
* iv2:
* iv3:

#### Connection to Intitial Paper

#### References
[1] Arisholm, Erik, Lionel C. Briand, and Eivind B. Johannessen. "A systematic and comprehensive investigation of methods to build and evaluate fault prediction models." Journal of Systems and Software 83.1 (2010): 2-17.
APA	

[2] Jiang, Yue, et al. "Variance analysis in software fault prediction models." Software Reliability Engineering, 2009. ISSRE'09. 20th International Symposium on. IEEE, 2009.

[3] https://en.wikipedia.org/wiki/Software_verification_and_validation