import numpy as np
from density_func import density_func,naive_G_U

#math
import math

K_value=49

#identification
def Speaker_identification(b_test,new_mu,new_cov,new_weight,T_value):
    #caculate the concatenated probability
    prob=density_func(b_test,new_mu,new_cov,T_value,K_value)
    test_pdf=naive_G_U(prob,new_weight)
    scores=np.sum(np.log(test_pdf))
    return scores
