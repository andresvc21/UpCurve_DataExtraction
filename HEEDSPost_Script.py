#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Script file recorded at 25 Mar 2021 16:03:58
# Build: 11291, Version: 2020.1.1
#
# Description: 

import HEEDS

def script():
  (project, process, Study1, Analysis1) = HEEDS.createProject()
  HEEDS.openPostWorkspace()
  Info_To_HEEDS = Study1.importDesigns('Info_To_HEEDS', path='E:/Personal/ASME/TEST/Info_To_HEEDS.csv', 
      cmap={ 'API':0, 'Initial Breakdown Presseure':6, 'Total Number of Stage':5 }, 
      delim=',')
  WolfA = Study1.importDesigns('WolfA', path='E:/Personal/ASME/TEST/WolfA.csv', 
      cmap={ 'API':0, 'Initial Breakdown Presseure':6, 'Total Number of Stage':5 }, 
      delim=',')
  WolfB = Study1.importDesigns('WolfB', path='E:/Personal/ASME/TEST/WolfB.csv', 
      cmap={ 'API':0, 'Initial Breakdown Presseure':6, 'Total Number of Stage':5 }, 
      delim=',')
  _designset1 = Study1.findChild('Info_To_HEEDS', HEEDS.DesignSet)
  Info_To_HEEDS_Initial_Breakdown_Presseure = Info_To_HEEDS.findResponse('Initial_Breakdown_Presseure')
  Info_To_HEEDS_Total_Number_of_Stage = Info_To_HEEDS.findResponse('Total_Number_of_Stage')
  Relation2D1 = Study1.createPlotRelation2D(name='Relation2D_1', designSet=_designset1, 
      Xaxis=Info_To_HEEDS_Initial_Breakdown_Presseure, Yaxis=[ Info_To_HEEDS_Total_Number_of_Stage ])
  Relation_WolfA_And_WolfB = Relation2D1.setName('Relation_WolfA_And_WolfB')
  _designset2 = Study1.findChild('WolfA', HEEDS.DesignSet)
  WolfA_Initial_Breakdown_Presseure = WolfA.findResponse('Initial_Breakdown_Presseure')
  WolfA_Total_Number_of_Stage = WolfA.findResponse('Total_Number_of_Stage')
  Relation2D2 = Study1.createPlotRelation2D(name='Relation2D_2', designSet=_designset2, 
      Xaxis=WolfA_Initial_Breakdown_Presseure, Yaxis=[ WolfA_Total_Number_of_Stage ])
  Relation_WolfA = Relation2D2.setName('Relation_WolfA')
  _designset3 = Study1.findChild('WolfB', HEEDS.DesignSet)
  WolfB_Initial_Breakdown_Presseure = WolfB.findResponse('Initial_Breakdown_Presseure')
  WolfB_Total_Number_of_Stage = WolfB.findResponse('Total_Number_of_Stage')
  Relation2D3 = Study1.createPlotRelation2D(name='Relation2D_3', designSet=_designset3, 
      Xaxis=WolfB_Initial_Breakdown_Presseure, Yaxis=[ WolfB_Total_Number_of_Stage ])
  Relation_WolfB = Relation2D3.setName('Relation_WolfB')
  Correlation4 = Study1.createPlotCorrelation(name='Correlation_4', designSet=_designset1, 
      parameters=[ WolfB_Initial_Breakdown_Presseure, WolfB_Total_Number_of_Stage ])
  View1 = Study1.createPlotView(cols=[2,2],rows=2,name='View_1') # 4 Horizontal Views
  View1.setItemAt(0, Correlation4)
  View1.setItemAt(1, Relation_WolfA_And_WolfB)
  View1.setItemAt(2, Relation_WolfA)
  View1.setItemAt(3, Relation_WolfB)


# Call the primary script function
if __name__ == '__main__':
  script()

