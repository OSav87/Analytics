import scipy.stats as st
import numpy as np

def p_value(z_score, alternative = 'two-sided'):
   
    if alternative == 'two-sided':
        return 2 * (1 - st.norm.cdf(np.abs(z_score)))
   
    if alternative == 'less':
        return st.norm.cdf(z_score)

    if alternative == 'greater':
        return 1 - st.norm.cdf(z_score)