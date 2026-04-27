import networkx as nx

def create_wait_for_graph(processes, allocation, request):
    """
    Create wait-for graph from allocation and request matrices.
    
    Args:
        processes (list): List of process names
        allocation (dict): Dict of process -> list of allocated resources
        request (dict): Dict of process -> list of requested resources
    
    Returns:
        nx.DiGraph: Directed graph representing wait-for relations
    """
    G = nx.DiGraph()
    
    # Add nodes for processes
    for p in processes:
        G.add_node(p)
    
    # Add edges: if P requests R held by Q, then P -> Q (P waits for Q)
    for p in processes:
        for r in request.get(p, []):
            for holder in processes:
                if holder != p and r in allocation.get(holder, []):
                    G.add_edge(p, holder)
    
    return G

