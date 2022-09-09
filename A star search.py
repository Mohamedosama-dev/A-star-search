# -*- coding: utf-8 -*-
"""Untitled69.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EA2x_3Ni18J4nqoqaRB_-tHHWBWYAvW2
"""

graph = {
    'S' : [('A', 2),('B',1)],
    'A' : [('E', 5)],
    'B' : [('C', 4)],
    'C' : [('G', 5)],
    'D' : [('F', 4)],
    'E' : [('D', 2)],
    'F' : [('G', 3)]
}
H_table = {
    'S' : 11,
    'A' : 10.4,
    'B' : 6.7,
    'C' : 4,
    'D' : 8.9,
    'E' : 6.9,
    'F' : 3,
    'G' : 0
}



def path_f_cost(path):
      g_cost = 0
      for (node,cost) in path :
          g_cost += cost
      last_node = path[-1][0]
      h_cost = H_table[last_node]
      f_cost = g_cost + h_cost
      return f_cost , last_node

def a_star_search( graph , start , goal ):
        visited = []
        queue = [[( start , 0 )]]
        while queue :
               queue.sort(key = path_f_cost)
               path = queue.pop(0)
               node = path[-1][0]
               if node in visited :
                     continue
               visited.append(node)
               if node == goal :
                     return path
               else :
                    adjacent_nodes = graph.get(node,[])
                    for ( node2 , cost ) in adjacent_nodes :
                        new_path = path.copy()
                        new_path.append(( node2 , cost ))
                        queue.append(new_path)
solution= a_star_search(graph,'S','G')
print('solution is ',solution)
print('cost of solution is ',path_f_cost(solution)[0])