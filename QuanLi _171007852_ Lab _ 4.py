#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-info" role="alert">
#     <center><h1 style="color:red;"><strong>Econometrics 322 Lab #4</strong></h1></center><br>
#     <center><h2><strong><color:red>Basic OLS Regression</strong></h2></center><br>
#     <center><h3><strong>Prof. Paczkowski</strong></h3></center>
# </div>
# <br><br>
# <div class="alert alert-warning" role="alert">
#     <center><h1><strong>Enter your Name in the Next Cell</strong></h1></center>
# </div>
# 

# Quan Li (RUID: 171007852)

# <div class="alert alert-info" role="alert">
# </div>

# ## Grading Rubric
# 
# <br>
# Score:_______________: Max(0, 20 - Total Deductions)
# <br><br>
# 
# 
# | Content Area | Deduction | Times Deducted | Check | Comments&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; |
# |:-----------------------------------------------------|:---------:||:------:|:-------------------------:|
# | Abstract                                             |           ||        |                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | &emsp;Insufficient/Wrong Focus                       | 1         ||[&emsp;]|                           |
# | Data Dictionary (Metadata)                           |           ||        |                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | &emsp;Insufficient/Wrong Form or Wording             | 1         ||[&emsp;]|                           |  
# | Graphs                                               |           ||        |                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | &emsp;Missing Title                                  | 1         ||[&emsp;]|                           |
# | &emsp;Missing/Wrong Labels                           | 1         ||[&emsp;]|                           |
# | Pre-Lab                                              |           ||        |                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | &emsp;Insufficient/Wrong Answer                      | 2 Each    ||[&emsp;]|                           |
# | &emsp;No/Incorrect/Insufficient Model Specification  | 2         ||[&emsp;]|                           |
# | &emsp;No/Incorrect Statistical Hypothesis Statement  | 2 Each    ||[&emsp;]|                           |
# | Post-Lab                                             |           ||        |                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | &emsp;Insufficient/Wrong Answer                      | 2 Each    ||[&emsp;]|                           |
# | Correlations                                         |           ||        |                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | &emsp;Insufficient/Wrong Analysis                    | 2         ||[&emsp;]|                           |
# | &emsp;Missing Graph                                  | 2         ||[&emsp;]|                           |
# | Estimations                                          |           ||        |                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | &emsp;No or incorrect discussion/interpretation of...|           ||        |                           |
# | &emsp;&emsp;Hypothesis tests and p-values            | 2 Each    ||[&emsp;]|                           |
# | &emsp;&emsp;$R^2$                                    | 2         ||[&emsp;]|                           |
# | &emsp;&emsp;F-Statistic                              | 2         ||[&emsp;]|                           |
# | &emsp;&emsp;Multicollinearity/VIF                    | 2         ||[&emsp;]|                           |
# | &emsp;&emsp;Heteroskedasticity/Test                  | 2         ||[&emsp;]|                           |
# | &emsp;&emsp;Autocorrelation/Test                     | 2         ||[&emsp;]|                           |
# | &emsp;No/insufficient model selection                | 2         ||[&emsp;]|                           |
# | Elasticities                                         |           ||        |                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | &emsp;Incorrect Interpretation                       | 2         ||[&emsp;]|                           |
# | &emsp;Missing Summary Table                          | 2         ||[&emsp;]|                           |
# | Model Portfolio                                      |           ||[&emsp;]|                           |
# | &emsp;Missing                                        | 5         ||[&emsp;]|                           |
# | General Comments:                                    |           ||        |                           |
# ||||||
# ||||||
# ||||||

# ## Contents
# 
# 1. [Collaboration Policy](#Collaboration-Policy)
# 2. [Introduction](#Introduction)
#     1. [Purpose](#Purpose)
#     2. [Problem](#Problem)
#     3. [Assignment](#Assignment)
# 3. [Documentation](#Documentation)
#     1. [Abstract](#Abstract)
#     2. [Data Dictionary](#Data-Dictionary)
# 4. [Tasks](#Tasks)

# ## Collaboration Policy
# 
# [Back to Contents](#Contents)
# 
#     1. Study groups are allowed but I expect students to understand and complete their own assignments and to hand in one 
#     assignment per student.
#     2. If you worked in a group, please put the names of your study group in the following table.
#     3. Just like all other classes at Rutgers, the student Honor Code is taken seriously.
#     
#     The submitted assignment must be your work.
#     
# |Collaborator(s) Name(s) |
# |------------------------|
# |       name(s) here     |

# <div class="alert alert-info" role="alert">
# </div>

# ## Introduction
# 
# [Back to Contents](#Contents)

# ### Purpose
# 
# [Back to Contents](#Contents)
# 
# This lab will introduce you to doing a simple OLS estimation using Statsmodels.
# 
# At the end of this lab, you will be able to:
# 
# - run an OLS estimation;
# - retrieve some basic OLS relevant data.

# ### Problem
# 
# [Back to Contents](#Contents)
# 
# This is a repeat of the water consumption problem discussed in class.  What determnines the demand for bottled water?

# ### Assignment
# 
# [Back to Contents](#Contents)
# 
# Use the water consumption data to estimate a simple regression model.  The water consumption data was introduced at the beginning of the semester and is available on Sakai in the *Resources* tab for this lab.  The unknown parameters of a demand function have to be estimated.  Estimate a simple OLS model real per capita water consumption as a function of the real price per gallon.  No other variables are to be used since the purpose of this lab is just to have you become familiar with commands.

# <div class="alert alert-info" role="alert">
# </div>

# ## Documentation
# 
# [Back to Contents](#Contents)

# ### Abstract
# 
# [Back to Contents](#Contents)

# In this lab, I discovered that there is statistical relation between per capita consumption of bottled water and the real price of bottle water. The parameter of the real price is estimated to be about -8425. The relationship has a normal distribution, with sum of all the residual being 0.000. 

# ### Data Dictionary
# 
# [Back to Contents](#Contents)

# | Variable | Values   | Source | Mnemonic |
# |----------|----------|--------|---------|
# |  Aggregate Consumption | Millions of gallons, annual | Int'l Bottled Water* | aggConsumption |
# |  Aggregate Revenue | Millions of dollars, annual/nominal | IBID | aggRevenue |
# |  Per Capita Consumption | Gallons per person, annual | Calculated: aggConsumption/pop | perCapitaCons |
# |  Nominal Price per Gallon | Nominal dollars | Calculated: aggRevenue/aggConsumption | price |
# |  Real Disposible Income per Capita | Real dollars, base = 2005, annual | Economic R. of Pres. 2010 Tbl. B-31 | realDisIncome |
# |  Food CPI | Index (Total Food & Beverages | Economic R. of Pres. 2010 Tbl. B-60 | foodCPI |
# |  Population | Millions | Economic R. of Pres. 2010 Tbl. B-34 | pop |
# |  Real Price per Gallon | Real dollars, annual | Calculated: price/foodCPI | realPrice |
# 
# \* http://www.bottledwater.org/content/industry-statistics 

# <div class="alert alert-info" role="alert">
# </div>

# ## Tasks
# 
# [Back to Contents](#Contents)

# ### Load the Pandas and Statsmodels packages and give them aliases.  I recommend 'pd' and 'sm'.  You will also need the Statsmodels formula API for formulas.  See Lesson \#4 for examples.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import statsmodels.api as sm
import statsmodels.formula.api as smf 
from statsmodels.iolib.summary2 import summary_col

import matplotlib.pyplot as plt
import seaborn as sns
sns.set( )

import numpy as np


# ### Import the water consumption data.  Set the row index to the years.

# In[13]:


df = pd.read_csv( "071410_1 water consumption.csv", parse_dates = [ 'Year' ] )
df.set_index( 'Year', inplace = True )


# ### Print the first five (5) records.

# In[6]:


df.head()


# ###  Estimate an OLS model using per capita consumption as the dependent variable and real price as the independent variable.  Display the summary report.  See Lesson \#4 for an example.

# In[7]:


formula = 'perCapitaCons ~ realPrice'
mod = smf.ols( formula, data = df )
reg01 = mod.fit() 
print( reg01.summary() )


# ### Retrieve and display the estimated parameters.

# In[8]:


print( 'Estimated parameters:\n{}'.format( reg01.params ) ) 


# ### Retrieve the residuals and verify that the sum of the residuals is zero.  

# In[9]:


print( 'Residuals:\n{}'.format( reg01.resid ) )
x = sum( reg01.resid )
print( 'Sum of residuals: {:0.3f}'.format( x ) )


# ### Calculate the standard error of the regression.

# In[12]:


sse = reg01.ssr
print( 'Sum of Squared Residuals (SSE): {:0.3f}'. format( sse ) )
se_reg = np.sqrt( sse/( reg01.nobs - 2 ) )
print( 'SE of Rgeresssion Long Way = ', round( se_reg, 3 ) )


# <div class="alert alert-success" role="alert">
#   <center><h4 class="alert-heading">Well done!</h4></center><br>
#   <center>Make sure your name is on this notebook at the top and on the file.</center>
#   <center>Please submit this notebook as a PDF file.  Nothing else will be accepted.</center>
# </div>

# In[ ]:




