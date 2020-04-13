# Define the equivalent of infinity. Arbitrary
max_num = 9e6

def dijkstra(graph_adj, nodes):
    visited = []
    graph = [i for i in range(nodes)]
    dist = [max_num] * nodes
    src_node = int(input("Enter source node : "))
    dist[src_node-1] = 0
    init_node = src_node-1
    visited.append(init_node)
    graph.remove(init_node)
    while graph:
        min_dist = max_num
        next_node = 0

        for i in range(nodes):
            if min_dist>graph_adj[init_node][i] and i not in visited:
                min_dist = graph_adj[init_node][i]
                next_node = i

        for i in range(nodes):
            if i in graph and graph_adj[i][init_node]>0:
                tdist = dist[init_node]+graph_adj[i][init_node]
                if tdist<dist[i]:
                    dist[i] = tdist

        visited.append(next_node)
        graph.remove(next_node)

        init_node = next_node

    print(dist)

def bfs(graph_adj, nodes):
    graph_queue = []
    src_node = int(input("Enter source node : "))
    graph_queue.append(src_node-1)
    visited = [0] * nodes
    level = [0] * nodes

    while graph_queue:
        curr_node = graph_queue[0]
        visited[curr_node] = 1
        graph_queue.pop(0)

        for i in range(nodes):
            if graph_adj[curr_node][i]>0 and visited[i]==0 and i not in graph_queue:
                graph_queue.append(i)
                level[i] = level[curr_node]+1

    print(level)

def main():
    num_vert = int(input("Number of vertices in graph : "))
    adj_mat = [[0] * num_vert for i in range(num_vert)]
    # Input format : src dest weight
    # Code stops if input is in any other format
    try:
        while(True):
            src, dest, weight = input().split()
            # Undirected graphs
            adj_mat[int(src)-1][int(dest)-1] = int(weight)
            adj_mat[int(dest)-1][int(src)-1] = int(weight)
    except ValueError:
        pass

    dijkstra(adj_mat, num_vert)
    bfs(adj_mat, num_vert)

if __name__ == '__main__':
    main()
