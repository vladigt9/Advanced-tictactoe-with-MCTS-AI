import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

# Load data
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


# Put data into arrays for easier plots
head_head = [d_h, d_v, d_n, h_d, h_v, h_n, v_d, v_h, v_n, n_d, n_h, n_v]
head_head_names = ['d_h', 'd_v', 'd_n', 'h_d', 'h_v', 'h_n', 'v_d', 'v_h', 'v_n', 'n_d', 'n_h', 'n_v']
self_self = [d_d, h_h, v_v, n_n]
self_self_names = ['d_d', 'h_h', 'v_v', 'n_n']
pos = [d_pos, n_pos, v_pos, h_pos]
pos_names = ['Diagonal', 'Normal', 'Vertical', 'Horizontal']

def plot_winrate():
    """
        In this function one can plot the win rates of all the head to head 
        match ups. It uses bar graph where each column combines the wins, draws,
        and losses. In addition there are 3 bars for each matchup so that 
        all possible iterations of the algorithm are shown in the corresponding
        place.
    
    """
    
    
    
    x = np.arange(len(head_head_names))
    width = 0.2
    gap = 0.02

    fig, ax = plt.subplots(figsize=(14, 7))

    for i, df in enumerate(head_head):
        ax.bar(x[i] - width - 2*gap, df['1'].iloc[0], width, label='1 000' if i == 0 else "", color='dodgerblue', hatch='//')
        ax.bar(x[i] - gap, df['1'].iloc[1], width, label='10 000' if i == 0 else "", color='dodgerblue', hatch='..')
        ax.bar(x[i] + width, df['1'].iloc[2], width, label='100 000' if i == 0 else "", color='dodgerblue', hatch='xx')

        ax.bar(x[i] - width - 2*gap, df['0'].iloc[0], width, bottom=df['1'].iloc[0], color='burlywood', hatch='//')
        ax.bar(x[i]- gap, df['0'].iloc[1], width, bottom=df['1'].iloc[1], color='burlywood', hatch='..')
        ax.bar(x[i] + width, df['0'].iloc[2], width, bottom=df['1'].iloc[2], color='burlywood', hatch='xx')
        
        ax.bar(x[i] - width - 2*gap, df['-1'].iloc[0], width, bottom=df['1'].iloc[0]+df['0'].iloc[0], color='orangered', hatch='//')
        ax.bar(x[i] - gap, df['-1'].iloc[1], width, bottom=df['1'].iloc[1]+df['0'].iloc[1], color='orangered', hatch='..')
        ax.bar(x[i] + width, df['-1'].iloc[2], width, bottom=df['1'].iloc[2]+df['0'].iloc[2], color='orangered', hatch='xx')
    
    ax.set_xlabel('Match-up')
    ax.set_ylabel('Number of Games')
    ax.set_title('Win Rate of Each Match-up with Different Number of Iterations')
    ax.set_xticks(x)
    ax.set_xticklabels(head_head_names)
    
    custom_legend = [
        mpatches.Patch(facecolor='white', hatch='//', label='1 000 Iterations'),
        mpatches.Patch(facecolor='white', hatch='..', label='10 000 Iterations'),
        mpatches.Patch(facecolor='white', hatch='xx', label='100 000 Iterations'),
        mlines.Line2D([], [], color='dodgerblue', marker='s', markersize=15, linestyle='None', label='Wins'),
        mlines.Line2D([], [], color='burlywood', marker='s', markersize=15, linestyle='None', label='Draws'),
        mlines.Line2D([], [], color='orangered', marker='s', markersize=15, linestyle='None', label='Losses')
    ]
    
    ax.legend(handles=custom_legend, title="Legend", title_fontsize='13', fontsize='11')

    fig.tight_layout()

    plt.savefig('./graphs/images/winrate.png', dpi=300)
    plt.close()

def plot_vs_self():
    """
        In this function one can plot the win rates of all the self vs self 
        match ups. It uses bar graph where each column combines the wins, draws,
        and losses. In addition there are 3 bars for each matchup so that 
        all possible iterations of the algorithm are shown in the corresponding
        place.
        
    """
    
    x = np.arange(len(self_self_names))
    width = 0.2
    gap = 0.02

    fig, ax = plt.subplots(figsize=(14, 7))

    for i, df in enumerate(self_self):
        ax.bar(x[i] - width - 2*gap, df['1'].iloc[0], width, label='1 000' if i == 0 else "", color='dodgerblue', hatch='//')
        ax.bar(x[i] - gap, df['1'].iloc[1], width, label='10 000' if i == 0 else "", color='dodgerblue', hatch='..')
        ax.bar(x[i] + width, df['1'].iloc[2], width, label='100 000' if i == 0 else "", color='dodgerblue', hatch='xx')

        ax.bar(x[i] - width - 2*gap, df['0'].iloc[0], width, bottom=df['1'].iloc[0], color='burlywood', hatch='//')
        ax.bar(x[i]- gap, df['0'].iloc[1], width, bottom=df['1'].iloc[1], color='burlywood', hatch='..')
        ax.bar(x[i] + width, df['0'].iloc[2], width, bottom=df['1'].iloc[2], color='burlywood', hatch='xx')
        
        ax.bar(x[i] - width - 2*gap, df['-1'].iloc[0], width, bottom=df['1'].iloc[0]+df['0'].iloc[0], color='orangered', hatch='//')
        ax.bar(x[i] - gap, df['-1'].iloc[1], width, bottom=df['1'].iloc[1]+df['0'].iloc[1], color='orangered', hatch='..')
        ax.bar(x[i] + width, df['-1'].iloc[2], width, bottom=df['1'].iloc[2]+df['0'].iloc[2], color='orangered', hatch='xx')
    
    ax.set_xlabel('Match-up')
    ax.set_ylabel('Number of Games')
    ax.set_title('Win Rate of Each Match-up with Different Number of Iterations')
    ax.set_xticks(x)
    ax.set_xticklabels(self_self_names)
    
    custom_legend = [
        mpatches.Patch(facecolor='white', hatch='//', label='1 000 Iterations'),
        mpatches.Patch(facecolor='white', hatch='..', label='10 000 Iterations'),
        mpatches.Patch(facecolor='white', hatch='xx', label='100 000 Iterations'),
        mlines.Line2D([], [], color='dodgerblue', marker='s', markersize=15, linestyle='None', label='Wins (Player 1)'),
        mlines.Line2D([], [], color='burlywood', marker='s', markersize=15, linestyle='None', label='Draws'),
        mlines.Line2D([], [], color='orangered', marker='s', markersize=15, linestyle='None', label='Losses (Player 1)')
    ]
    
    ax.legend(handles=custom_legend, title="Legend", title_fontsize='13', fontsize='11')

    fig.tight_layout()

    plt.savefig('./graphs/images/self_rate.png', dpi=300)
    plt.close()

def plot_pos():
    """
        In this function the turns that each algorithm has played in a corresponding
        position are plotted against other algorithms in a bar plot. For each 
        position a new plot is created. The bars are grouped on the x-axis by position
        while the y axis shows the number of times that positions has been played.
    
    """
    
    for k in range(1, 21):
        positions = []
            
        for i, p in enumerate(pos):
            p['alg'] = [f'{pos_names[i]}']*len(p)
            x = p[p['state'] == k]
            positions.append(x)
            
        
        x = pd.concat(positions, ignore_index=True)
        
        pivot_df = x.pivot(index='position', columns='alg', values='times')

        # Plotting
        pivot_df.plot(kind='bar', figsize=(10, 6))

        # Customizing the plot
        plt.xlabel('Position Played (row, column)')
        plt.ylabel('Times')
        plt.title(f"Algorithms' Responses for Game State {k}")
        plt.legend(title='Strategy')
        plt.xticks(rotation=0)
        plt.savefig(f'./graphs/images/pos_{k}.png', dpi=300)
