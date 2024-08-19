from simulations.onevone import DiavsHor, DiavsVer, DiavsNorm, HorvsVer, HorvsNorm, HorvsDia, VervsHor, VervsNorm, VervsDia, NormvsHor, NormvsVer, NormvsDia
from simulations.onevself import N_N, D_D, V_V, H_H
from simulations.turns import norm_pos, dia_pos, hor_pos, ver_pos
import pandas as pd


def str_vs_str():
    """
        In this function all algorithms are played against each other. THe final 
        results are saved in lists which are then transformed to data sets and 
        csv files. The data collected are number of wins of each player, draws and 
        number of iterations performed. The print statements are placed to keep 
        track to where the simulation is.
    
    """
    
    dia_hor = []
    dia_ver = []
    dia_norm = []
    hor_dia = []
    hor_norm = []
    hor_ver = []
    ver_hor = []
    ver_dia = []
    ver_norm = []
    norm_hor = []
    norm_ver = []
    norm_dia = []
    
    ite = 100
    n_games = 100
    
    for i in range(1,4):
        results = DiavsHor(number_games=n_games, iterations=ite*10^i)
        dia_hor.append(results)
    
    print(1)
        
    for i in range(1,4):
        results = DiavsVer(number_games=n_games, iterations=ite*10^i)
        dia_ver.append(results)
        
    print(2)
    for i in range(1,4):
        results = DiavsNorm(number_games=n_games, iterations=ite*10^i)
        dia_norm.append(results)
    print(3)
        
    for i in range(1,4):
        results = HorvsDia(number_games=n_games, iterations=ite*10^i)
        hor_dia.append(results)
    print(4)
        
    for i in range(1,4):
        results = HorvsNorm(number_games=n_games, iterations=ite*10^i)
        hor_norm.append(results)
        
    print(5)
    for i in range(1,4):
        results = HorvsVer(number_games=n_games, iterations=ite*10^i)
        hor_ver.append(results)
    
    print(6)
    for i in range(1,4):
        results = VervsHor(number_games=n_games, iterations=ite*10^i)
        ver_hor.append(results)
    
    print(7)
    for i in range(1,4):
        results = VervsDia(number_games=n_games, iterations=ite*10^i)
        ver_dia.append(results)
    
    print(8)
    for i in range(1,4):
        results = VervsNorm(number_games=n_games, iterations=ite*10^i)
        ver_norm.append(results)
    
    print(9)
    for i in range(1,4):
        results = NormvsHor(number_games=n_games, iterations=ite*10^i)
        norm_hor.append(results)
    
    print(10)
    for i in range(1,4):
        results = NormvsVer(number_games=n_games, iterations=ite*10^i)
        norm_ver.append(results)
    
    print(11)
    for i in range(1,4):
        results = NormvsDia(number_games=n_games, iterations=ite*10^i)
        norm_dia.append(results)

    d_h = pd.DataFrame(dia_hor)
    d_v = pd.DataFrame(dia_ver)
    d_n = pd.DataFrame(dia_norm)
    h_n = pd.DataFrame(hor_norm)
    h_v = pd.DataFrame(hor_ver)
    h_d = pd.DataFrame(hor_dia)
    v_d = pd.DataFrame(ver_dia)
    v_n = pd.DataFrame(ver_norm)
    v_h = pd.DataFrame(ver_hor)
    n_h = pd.DataFrame(norm_hor)
    n_v = pd.DataFrame(norm_ver)
    n_d = pd.DataFrame(norm_dia)

    dfs = [d_h, d_v, d_n, h_d, h_n, h_v, v_d, v_h, v_n, n_d, n_h, n_v]
    dfs_names  = ['d_h', 'd_v', 'd_n', 'h_d', 'h_n', 'h_v', 'v_d', 'v_h', 'v_n', 'n_d', 'n_h', 'n_v']

    for i in range(len(dfs)):
        dfs[i].to_csv(f'data/{dfs_names[i]}.csv', index=False, header=False)

def str_vs_self():
    """
        In this function all algorithms are played against themselves. THe final 
        results are saved in lists which are then transformed to data sets and 
        csv files. The data collected are number of wins of each player, draws and 
        number of iterations performed. The print statements are placed to keep 
        track to where the simulation is.
    
    """
    d_d = []
    v_v = []
    h_h = []
    n_n = []
    
    ite = 100
    n_games = 100
    
    print(1)
    for i in range(1,4):
        results = D_D(number_games=n_games, iterations=ite*10^i)
        d_d.append(results)
    
    print(2)
    for i in range(1,4):
        results = V_V(number_games=n_games, iterations=ite*10^i)
        v_v.append(results)
    
    print(3)
    for i in range(1,4):
        results = H_H(number_games=n_games, iterations=ite*10^i)
        h_h.append(results)
    
    print(4)
    for i in range(1,4):
        results = N_N(number_games=n_games, iterations=ite*10^i)
        n_n.append(results)
        
    d = pd.DataFrame(d_d)
    v = pd.DataFrame(v_v)
    h = pd.DataFrame(h_h)
    n = pd.DataFrame(n_n)
    
    dfs = [d,v,h,n]
    dfs_names = ['d_d', 'v_v', 'h_h', 'n_n']
    
    for i in range(len(dfs)):
        dfs[i].to_csv(f'data/{dfs_names[i]}.csv', index=False, header=False)
        
def pos_play():
    """
        In this function all algorithms are made to play a specific turn from a 
        predefined position. The turns taken are saved and then transfered to csv
        files. 
    
    """
    
    ite = 10000
    n_games = 100
    
    print(1)
    n_p = norm_pos(number_games=n_games, iterations=ite)
    
    print(2)
    d_p = dia_pos(number_games=n_games, iterations=ite)
    
    print(3)
    v_p = ver_pos(number_games=n_games, iterations=ite)
    
    print(4)
    h_p = hor_pos(number_games=n_games, iterations=ite)
    
    n_df = []
    h_df = []
    v_df = []
    d_df = []
    
    for idx, d in enumerate(n_p):
        df = pd.DataFrame(list(d.items()), columns=['key', 'value'])
        df['row_number'] = idx + 1
        n_df.append(df)
        
    for idx, d in enumerate(d_p):
        df = pd.DataFrame(list(d.items()), columns=['key', 'value'])
        df['row_number'] = idx + 1
        d_df.append(df)
        
    for idx, d in enumerate(v_p):
        df = pd.DataFrame(list(d.items()), columns=['key', 'value'])
        df['row_number'] = idx + 1
        v_df.append(df)
        
    for idx, d in enumerate(h_p):
        df = pd.DataFrame(list(d.items()), columns=['key', 'value'])
        df['row_number'] = idx + 1
        h_df.append(df)
    
    n_pos = pd.concat(n_df, ignore_index=True)
    v_pos = pd.concat(v_df, ignore_index=True)
    h_pos = pd.concat(h_df, ignore_index=True)
    d_pos = pd.concat(d_df, ignore_index=True)

    dfs = [n_pos, v_pos, h_pos, d_pos]
    dfs_names = ['n_pos', 'v_pos', 'h_pos', 'd_pos']
    
    for i in range(len(dfs)):
        dfs[i].to_csv(f'data/{dfs_names[i]}.csv', index=False, header=False)
