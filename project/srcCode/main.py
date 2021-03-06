# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 10:07:08 2015

@author: akond
"""



from models import IntegratedDefectModel
import tests, ModelExecAll, integrator, utility, IO_Utility 
########### Obsolete ########
#def execBottom(showFlows):
#  print "############# BOTTOM #########"
#  # print "Executing test cases for bottom ... no fail means passing !"
#  # tests.testBottom(showFlows)
#  print "Executing the 'bottom' part of the model ... "
#  ModelExec.executeModelBottom(showFlows)
#
#
#    
#def execTop(showFlows):
#  print "############# TOP #########"
#  print "Executing test cases for top ... no fail means passing !"
#  tests.testTop(showFlows)
#  print "Executing the 'top' part of the model ... "
#  ModelExec.executeModelTop(showFlows) 


def execAll(showFlows):

  print "############# ALL #########"
  print "Executing test cases for whole model ... no fail means passing !"
  tests.testAll(showFlows)
  print "Executing the 'ALL' part of the model ... "
  ModelExecAll.executeModelAll(showFlows) 



#def runIntegrator():
#  print "############# Dummy Integration #########"
#  print "Executing test cases for whole model with dummy integration ... no fail means passing !"
#  tests.testDummyIntegration()
  
def getBaselineForModel(cntParam, dirToWriteP, fileNameToWriteP, constFlagForBaselineP):
  print "Getting baseline for {} times".format(cntParam) 
  baselineDict = integrator.runModelForBaseline(cntParam, constFlagForBaselineP)  
  print "Writing dictionary to file ... ",   IO_Utility.writeDictToFile(dirToWriteP, fileNameToWriteP, baselineDict)
  minOfBaseline_ = utility.getFeatureFromDict(baselineDict,  "min") 
  maxOfBaseline_ = utility.getFeatureFromDict(baselineDict,  "max")  

  return minOfBaseline_, maxOfBaseline_
  
def createConstraintFile(dirP, fileP, lowerRangeP, upperRangeP, constFlagParam): 
  auxNames= utility.getAuxNameList()     
  lowerRange, upperRange = utility.createAuxList(lowerRangeP, upperRangeP, constFlagParam)
  IO_Utility.createConstraintFiles(dirP, fileP, auxNames, lowerRange, upperRange)
  return "Created  file " + fileP  

showFlows=False  # to show flow values while executing the model 
#execAll(showFlows)

runCount = 365  ## how many time the model will run 
constFlag = False ## th flag detrmines whether or not hte five equations will be used to geenrate constaints 
deRunList=[1000]  ## howmany times DE will run? 
dirToWriteP="/Users/akond/Documents/Fall_2015/ase/59115ASE/project/supplementary/" ## directory to store baseline and constraint files  
lowerRange = 0  ## settign the lower range for axuiliries of the model 
upperRange = 1  ## settign the upper range for axuiliries of the model 
iterations = 10  ## settign how many times we will do the experiemnts 
deExp=True  
#galeExp=False 

###   creatiing constraint file ######
#constraintFileNameParam=  "all_0_1_equ.csv" ## file to store baseline and constraint files
#print "### creating constraints file ###" 
#print createConstraintFile(dirToWriteP, constraintFileNameParam, lowerRange, upperRange, constFlag)

#### DE ZONE STARTS ! #########
if deExp:
# important part: execution od DE for multiple iterations , for n number of times #####
 for cnt in xrange(iterations):
  print " ************ Iteration # {} ***************  ".format(cnt)  
  for deRunCount in deRunList:
    print "### gettting baseline ###" 
    baseline_fileNameToWriteP = "baseline_" + str(runCount) + "_" + str(deRunCount) + "_" + str("cnt")
    minB, maxB = getBaselineForModel(runCount, dirToWriteP, baseline_fileNameToWriteP, constFlag)
    #print "And the baseline is (min, max format) \n", minB, maxB

    print "Executing D.E (minimized version) ... for {} D.E. runs and {} model runs".format(deRunCount, runCount)
    print "========================================================================="
    #constraintFileNameParam = "all_0_1_equ.csv"
    constraintFileNameParam = "all_0_1_no_equ.csv"
    constraintFile = dirToWriteP + constraintFileNameParam 
    with  utility.duration(): 
      integrator.runDE(minB, maxB, IntegratedDefectModel, deRunCount, runCount, constraintFile)
  print "------------------------------------------ END ----------------------------------------------------------"    
####  DE ZONE ENDS! #########
##### GALE ZONE STARTS ! #########
#if galeExp:
# for cnt in xrange(iterations):
#  galeRunCount = 10 
#  print "### gettting baseline ###" 
#  baseline_fileNameToWriteP = "baseline_" + str(runCount)
#  minB, maxB = getBaselineForModel(runCount, dirToWriteP, baseline_fileNameToWriteP, constFlag)
#  print "And the baseline is (min, max format) \n", minB, maxB
#
#  print "Executing GALE (minimized version) ... for {} GALE runs and {} model runs".format(galeRunCount, runCount)
#  print "========================================================================="   
#  with utility.duration():
#    integrator.runGALE(galeRunCount, minB, maxB)    
##### GALE ZONE STARTS ! #########  