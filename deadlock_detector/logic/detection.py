import networkx as nx

def detect_deadlock(graph):
    """
    Detect if deadlock exists by finding cycles in wait-for graph.
    
    Args:
        graph (nx.DiGraph): Wait-for graph
    
    Returns:
        tuple: (bool has_deadlock, list cycles)
    """
    try:
        cycles = list(nx.simple_cycles(graph))
        return len(cycles) > 0, cycles
    except:
        return False, []

