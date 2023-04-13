import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 441809625 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    _x = x_success /  x_cnt
    _y = y_success /y_cnt
    
    diff = np.sqrt((_x * (1 - _x) / x_cnt) + (_y * (1 - _y) / y_cnt))
    
    temp = abs(_y - _x) / diff
    temp_crit = norm.ppf(1-0.04)
    
  
    return (temp > temp_crit)
