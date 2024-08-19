import pandas as pd
import scipy.stats as stats


# Load all the data files
d_d = pd.read_csv('data/d_d.csv', names=['1', '-1', '0'], header=None)
d_h = pd.read_csv('data/d_h.csv', names=['1', '-1', '0'], header=None)
d_v = pd.read_csv('data/d_v.csv', names=['1', '-1', '0'], header=None)
d_n = pd.read_csv('data/d_n.csv', names=['1', '-1', '0'], header=None)
h_h = pd.read_csv('data/h_h.csv', names=['1', '-1', '0'], header=None)
h_d = pd.read_csv('data/h_d.csv', names=['1', '-1', '0'], header=None)
h_v = pd.read_csv('data/h_v.csv', names=['1', '-1', '0'], header=None)
h_n = pd.read_csv('data/h_n.csv', names=['1', '-1', '0'], header=None)
v_v = pd.read_csv('data/v_v.csv', names=['1', '-1', '0'], header=None)
v_d = pd.read_csv('data/v_d.csv', names=['1', '-1', '0'], header=None)
v_h = pd.read_csv('data/v_h.csv', names=['1', '-1', '0'], header=None)
v_n = pd.read_csv('data/v_n.csv', names=['1', '-1', '0'], header=None)
n_n = pd.read_csv('data/n_n.csv', names=['1', '-1', '0'], header=None)
n_d = pd.read_csv('data/n_d.csv', names=['1', '-1', '0'], header=None)
n_h = pd.read_csv('data/n_h.csv', names=['1', '-1', '0'], header=None)
n_v = pd.read_csv('data/n_v.csv', names=['1', '-1', '0'], header=None)
d_pos = pd.read_csv('data/d_pos.csv', names=['position', 'times', 'state'])
n_pos = pd.read_csv('data/n_pos.csv', names=['position', 'times', 'state'])
v_pos = pd.read_csv('data/v_pos.csv', names=['position', 'times', 'state'])
h_pos = pd.read_csv('data/h_pos.csv', names=['position', 'times', 'state'])

def normal_dist():
    """
        This function checks for all possible iterations if the data follows a 
        normal distribution. The null hypothesis of the shapiro test is that 
        the data follows a normal distribution. Hence p-value of >0.05 means 
        normal and less not normal.
    
    """
    
    for i in range(3):
        nd = [d_h['1'].iloc[i], d_v['1'].iloc[i], d_n['1'].iloc[i], h_d['1'].iloc[i], h_v['1'].iloc[i], h_n['1'].iloc[i], 
                v_d['1'].iloc[i], v_h['1'].iloc[i], v_n['1'].iloc[i], n_d['1'].iloc[i], n_h['1'].iloc[i], n_v['1'].iloc[i],
                d_d['1'].iloc[i], v_v['1'].iloc[i], h_h['1'].iloc[i], n_n['1'].iloc[i]]
        
        stat, p_value = stats.shapiro(nd)

        print(p_value)
    
def anova_test1():
    """
        This function performs anova test to check if the win rate of the first 
        to play is significantly bigger than that of the second to play.
        It loops over all different number of iterations. p-value of less than 
        0.05 suggest they are different.
    
    """
    
    for i in range(3):
        f = [d_h['1'].iloc[i], d_v['1'].iloc[i], d_n['1'].iloc[i], h_d['1'].iloc[i], h_v['1'].iloc[i], h_n['1'].iloc[i], 
                    v_d['1'].iloc[i], v_h['1'].iloc[i], v_n['1'].iloc[i], n_d['1'].iloc[i], n_h['1'].iloc[i], n_v['1'].iloc[i],
                    d_d['1'].iloc[i], v_v['1'].iloc[i], h_h['1'].iloc[i], n_n['1'].iloc[i]]
        
        s = [d_h['-1'].iloc[i], d_v['-1'].iloc[i], d_n['-1'].iloc[i], h_d['-1'].iloc[i], h_v['-1'].iloc[i], h_n['-1'].iloc[i], 
                    v_d['-1'].iloc[i], v_h['-1'].iloc[i], v_n['-1'].iloc[i], n_d['-1'].iloc[i], n_h['-1'].iloc[i], n_v['-1'].iloc[i],
                    d_d['-1'].iloc[i], v_v['-1'].iloc[i], h_h['-1'].iloc[i], n_n['-1'].iloc[i]]
        
        anova_result = stats.f_oneway(f, s)
        print(anova_result)

def krus_walis1():
    """
        This function performs kruskal-wallis test to check if the win rate of the first 
        to play is significantly bigger than that of the second to play.
        It loops over all different number of iterations. p-value of less than 
        0.05 suggest they are different.
    
    """
    
    for i in range(3):
        f = [d_h['1'].iloc[i], d_v['1'].iloc[i], d_n['1'].iloc[i], h_d['1'].iloc[i], h_v['1'].iloc[i], h_n['1'].iloc[i], 
                    v_d['1'].iloc[i], v_h['1'].iloc[i], v_n['1'].iloc[i], n_d['1'].iloc[i], n_h['1'].iloc[i], n_v['1'].iloc[i],
                    d_d['1'].iloc[i], v_v['1'].iloc[i], h_h['1'].iloc[i], n_n['1'].iloc[i]]
        
        s = [d_h['-1'].iloc[i], d_v['-1'].iloc[i], d_n['-1'].iloc[i], h_d['-1'].iloc[i], h_v['-1'].iloc[i], h_n['-1'].iloc[i], 
                    v_d['-1'].iloc[i], v_h['-1'].iloc[i], v_n['-1'].iloc[i], n_d['-1'].iloc[i], n_h['-1'].iloc[i], n_v['-1'].iloc[i],
                    d_d['-1'].iloc[i], v_v['-1'].iloc[i], h_h['-1'].iloc[i], n_n['-1'].iloc[i]]
        
        krus_result = stats.kruskal(f, s)
        print(krus_result)
    
def anova_test2():
    """
        This function performs anova test to check if the win rate is different 
        when different number of itterations is used. p-value of less than 
        0.05 suggest they are different.
    
    """
    
    f = [d_h['1'].iloc[0], d_v['1'].iloc[0], d_n['1'].iloc[0], h_d['1'].iloc[0], h_v['1'].iloc[0], h_n['1'].iloc[0], 
                v_d['1'].iloc[0], v_h['1'].iloc[0], v_n['1'].iloc[0], n_d['1'].iloc[0], n_h['1'].iloc[0], n_v['1'].iloc[0],
                d_d['1'].iloc[0], v_v['1'].iloc[0], h_h['1'].iloc[0], n_n['1'].iloc[0]]
    s = [d_h['1'].iloc[1], d_v['1'].iloc[1], d_n['1'].iloc[1], h_d['1'].iloc[1], h_v['1'].iloc[1], h_n['1'].iloc[1], 
                v_d['1'].iloc[1], v_h['1'].iloc[1], v_n['1'].iloc[1], n_d['1'].iloc[1], n_h['1'].iloc[1], n_v['1'].iloc[1],
                d_d['1'].iloc[1], v_v['1'].iloc[1], h_h['1'].iloc[1], n_n['1'].iloc[1]]
    t = [d_h['1'].iloc[2], d_v['1'].iloc[2], d_n['1'].iloc[2], h_d['1'].iloc[2], h_v['1'].iloc[2], h_n['1'].iloc[2], 
                v_d['1'].iloc[2], v_h['1'].iloc[2], v_n['1'].iloc[2], n_d['1'].iloc[2], n_h['1'].iloc[2], n_v['1'].iloc[2],
                d_d['1'].iloc[2], v_v['1'].iloc[2], h_h['1'].iloc[2], n_n['1'].iloc[2]]
    
    anova_result = stats.f_oneway(f, s, t)
    print(anova_result)
    
def krus_walis2():
    """
        This function performs kruskal-wallis test to check if the win rate is different 
        when different number of itterations is used. p-value of less than 
        0.05 suggest they are different.
    
    """
    
    f = [d_h['1'].iloc[0], d_v['1'].iloc[0], d_n['1'].iloc[0], h_d['1'].iloc[0], h_v['1'].iloc[0], h_n['1'].iloc[0], 
                v_d['1'].iloc[0], v_h['1'].iloc[0], v_n['1'].iloc[0], n_d['1'].iloc[0], n_h['1'].iloc[0], n_v['1'].iloc[0],
                d_d['1'].iloc[0], v_v['1'].iloc[0], h_h['1'].iloc[0], n_n['1'].iloc[0]]
    s = [d_h['1'].iloc[1], d_v['1'].iloc[1], d_n['1'].iloc[1], h_d['1'].iloc[1], h_v['1'].iloc[1], h_n['1'].iloc[1], 
                v_d['1'].iloc[1], v_h['1'].iloc[1], v_n['1'].iloc[1], n_d['1'].iloc[1], n_h['1'].iloc[1], n_v['1'].iloc[1],
                d_d['1'].iloc[1], v_v['1'].iloc[1], h_h['1'].iloc[1], n_n['1'].iloc[1]]
    t = [d_h['1'].iloc[2], d_v['1'].iloc[2], d_n['1'].iloc[2], h_d['1'].iloc[2], h_v['1'].iloc[2], h_n['1'].iloc[2], 
                v_d['1'].iloc[2], v_h['1'].iloc[2], v_n['1'].iloc[2], n_d['1'].iloc[2], n_h['1'].iloc[2], n_v['1'].iloc[2],
                d_d['1'].iloc[2], v_v['1'].iloc[2], h_h['1'].iloc[2], n_n['1'].iloc[2]]
    
    krus_result = stats.kruskal(f, s, t)
    print(krus_result)

def anova_test3():
    """
        This function performs anova test to check if the win rate of the normal 
        MCTS is signifacntly different than the win rates of the other 
        strategies. p-value of less than 0.05 suggest they are different.
    
    """
    
    for i in range(3):
        f = [d_h['1'].iloc[i], d_v['1'].iloc[i], d_n['1'].iloc[i], h_d['1'].iloc[i], h_v['1'].iloc[i], h_n['1'].iloc[i], 
                    v_d['1'].iloc[i], v_h['1'].iloc[i], v_n['1'].iloc[i],
                    d_d['1'].iloc[i], v_v['1'].iloc[i], h_h['1'].iloc[i]]
        
        s = [n_d['-1'].iloc[i], n_h['-1'].iloc[i], n_v['-1'].iloc[i], n_n['-1'].iloc[i]]
        
        anova_result = stats.f_oneway(f, s)
        print(anova_result)

def krus_walllis3():
    """
        This function performs kruskal-wallis test to check if the win rate of the normal 
        MCTS is signifacntly different than the win rates of the other 
        strategies. p-value of less than 0.05 suggest they are different.
    
    """
    
    for i in range(3):
        f = [d_h['1'].iloc[i], d_v['1'].iloc[i], d_n['1'].iloc[i], h_d['1'].iloc[i], h_v['1'].iloc[i], h_n['1'].iloc[i], 
                    v_d['1'].iloc[i], v_h['1'].iloc[i], v_n['1'].iloc[i],
                    d_d['1'].iloc[i], v_v['1'].iloc[i], h_h['1'].iloc[i]]
        
        s = [n_d['-1'].iloc[i], n_h['-1'].iloc[i], n_v['-1'].iloc[i], n_n['-1'].iloc[i]]
        
        krus_result = stats.kruskal(f, s)
        print(krus_result)
