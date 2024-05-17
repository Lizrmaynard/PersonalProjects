#!/usr/bin/env python
# coding: utf-8

# In[6]:


#imports and setup for probability calculator
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

#define the function for the input number you are rollling below
def below_probability(target,rolls):
    #define parameters for inputs
    if target <1 or target >20:
        raise ValueError("Target number must be between 1 and 20")
        
    if rolls <= 0:
        raise ValueError("Number of rolls must be a positive integer")
        
    probability_single_roll = (target * 1/20.0)
    
    probability_all_rolls = probability_single_roll ** rolls
    
    probability_only_below = probability_all_rolls * 100
    
    return probability_only_below


# In[7]:


#we use the example numbers

target = 11
rolls = 48

#Fromatting the resulting value into percentage and ratio

probability = below_probability(target, rolls)

probability_percent = np.format_float_positional(probability, trim='-')

probability_percent_ratio = Decimal(probability_percent)

probability_non_float = probability / 100

probability_ratio = 1/probability_non_float

probability_round = round(probability_ratio)

#Printing the probability in percentage and ratio
print("Probability of only rolling below or equal to", target, "on a 20-sided dice in", rolls, "rolls:", probability_percent,"%")
print("Probability ratio of only rolling below or equal to", target, "on a 20-sided dice in", rolls, "rolls:", "1 in", probability_round)


# In[8]:


#Setting up example 2

target1 = 15
rolls1 = 10

#Formatting the resulting value into percentage and ratio

probability1 = below_probability(target1, rolls1)

probability_percent1 = np.format_float_positional(probability1, trim='-')

probability_percent_ratio1 = Decimal(probability_percent1)

probability_non_float1 = probability1 / 100

probability_ratio1 = 1/probability_non_float1

probability_round1 = round(probability_ratio1)


#Printing the probability in percentage and ratio
print("Probability of only rolling below or equal to", target1, "on a 20-sided dice in", rolls1, "rolls:", probability_percent1,"%")
print("Probability ratio of only rolling below or equal to", target1, "on a 20-sided dice in", rolls1, "rolls:", "1 in", probability_round1)


# In[9]:


#Setting up example 3

target2 = 5
rolls2 = 22

#Formatting the resulting value into percentage and ratio

probability2 = below_probability(target2, rolls2)

probability_percent2 = np.format_float_positional(probability2, trim='-')

probability_percent_ratio2 = Decimal(probability_percent2)

probability_non_float2 = probability2 / 100

probability_ratio2 = 1/probability_non_float2

probability_round2 = round(probability_ratio2)


#Printing the probability in percentage and ratio
print("Probability of only rolling below or equal to", target2, "on a 20-sided dice in", rolls2, "rolls:", probability_percent2,"%")
print("Probability ratio of only rolling below or equal to", target2, "on a 20-sided dice in", rolls2, "rolls:", "1 in", probability_round2)


# In[10]:


#Setting up example 4

target3 = 20
rolls3 = 1

#Formatting the resulting value into percentage and ratio

probability3 = below_probability(target3, rolls3)

probability_percent3 = np.format_float_positional(probability3, trim='-')

probability_percent_ratio3 = Decimal(probability_percent3)

probability_non_float3 = probability3 / 100

probability_ratio3 = 1/probability_non_float3

probability_round3= round(probability_ratio3)


#Printing the probability in percentage and ratio
print("Probability of only rolling below or equal to", target3, "on a 20-sided dice in", rolls3, "rolls:", probability_percent3,"%")
print("Probability ratio of only rolling below or equal to", target3, "on a 20-sided dice in", rolls3, "rolls:", "1 in", probability_round3)


# In[ ]:




