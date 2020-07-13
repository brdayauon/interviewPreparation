#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compute_number_score function below.
def compute_number_score(number):
    score = 0
    prev = 0
    current = 0
    consecutive = 0 
    while (number != 0):
            pop = number % 10;
            current = pop
            if pop == 7:  # 
                score += 1
            if prev == 5 and current == 5:  #consecutive 5 check
                score += 3
            if pop % 2 == 0: #if even
                score += 4
            if (current - 1) == prev:
                consecutive += 1  
            
                number = number // 10;
            prev = pop 

    if number % 3 == 0: # if number is multiple of 3
        score += 2

    return score 
    
if __name__ == '__main__':