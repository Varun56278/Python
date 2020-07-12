import matplotlib.pyplot as plt
import networkx as nx

G = nx.star_graph(10)
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos,
                       nodelist=[0],
                       node_color='r',
                       node_size=500)
                     
nx.draw_networkx_nodes(G, pos,
                       nodelist=[1],
                       node_color='pink',
                       node_size=500)
                     
nx.draw_networkx_nodes(G, pos,
                       nodelist=[2],
                       node_color='brown',
                       node_size=500)
                       
nx.draw_networkx_nodes(G, pos,
                       nodelist=[3],
                       node_color='green',
                       node_size=500)
                       
nx.draw_networkx_nodes(G, pos,
                       nodelist=[4],
                       node_color='yellow',
                       node_size=500)
                       
nx.draw_networkx_nodes(G, pos,
                       nodelist=[5],
                       node_color='orange',
                       node_size=500)
                       
nx.draw_networkx_nodes(G, pos,
                       nodelist=[6, 7, 8, 9, 10],
                       node_color='b',
                       node_size=500)

# edges
nx.draw_networkx_edges(G, pos, width=1.0)
nx.draw_networkx_edges(G, pos,
                       edgelist=[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)],
                       width=5, edge_color='green')
nx.draw_networkx_edges(G, pos,
                       edgelist=[(0, 6), (0, 7), (0, 8), (0, 9), (0, 10)],
                       width=5, edge_color='yellow')



nx.draw_networkx_labels(G, pos, with_labels=1, font_size=16)

plt.axis('off')
plt.show()






















import matplotlib.pyplot as plt
import networkx as nx

G = nx.cubical_graph()
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos,
                       nodelist=[0, 1, 2, 3],
                       node_color='r',
                       node_size=500,
                       alpha=0.8)
nx.draw_networkx_nodes(G, pos,
                       nodelist=[4, 5, 6, 7],
                       node_color='b',
                       node_size=500,
                       alpha=0.8)

# edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos,
                       edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
                       width=8, alpha=0.5, edge_color='r')
nx.draw_networkx_edges(G, pos,
                       edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
                       width=8, alpha=0.5, edge_color='b')


# some math labels
labels = {}
labels[0] = r'$a$'
labels[1] = r'$b$'
labels[2] = r'$c$'
labels[3] = r'$d$'
labels[4] = r'$\alpha$'
labels[5] = r'$\beta$'
labels[6] = r'$\gamma$'
labels[7] = r'$\delta$'
nx.draw_networkx_labels(G, pos, labels, font_size=16)

plt.axis('off')
plt.show()
 

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
K = nx.star_graph(100)
nx.draw(K,with_labels=1, node_color='r')
plt.show()





import networkx as nx
import matplotlib.pyplot as plt
my_graph = nx.Graph()
my_graph.add_edges_from([
                        ('Mohit','Shivam'),
                        ('Shivam','Sanjay'), 
                        ('Mohit','Sanjay'),
                        ('Arpit','Shubham'),
                        ('Sanjay','Shubham'),
                        ('Shivam','Mohit'),
                        ('Mohit','Arpit'),
                        ('Arpit','Sanjay'),
                        ('Sanjay','Arpit'),
                        ('Shubham','Sanjay'),
                        ('Shubham','Shivam'),
                        ('Arpit','Mohit'),
                        ('Shivam','Sanjay'),
                        ('Mohit','Sanjay'),
                        ('Sanjay','Prachi'),
                        ('Shivam','Shubham')])
nx.draw(my_graph, with_labels=True, font_weight='bold')
plt.show()
















import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
B = np.matrix([[0,1,1,0],[1,0,0,0],[1,1,0,1],[0,0,0,0]])
print(B)
K = nx.from_numpy_matrix(B)
nx.draw(K)
plt.show()
