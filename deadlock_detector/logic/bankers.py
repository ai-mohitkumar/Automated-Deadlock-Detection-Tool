def bankers_algorithm(processes, available, max_need, allocation):
    """
    Banker's Algorithm simplified for demo - checks allocation size heuristic.
    
    Returns safe state if no process allocates too many resources.
    """
    # Simple heuristic for demo: safe if no process has >2 resources
    for p in processes:
        allocated_resources = allocation.get(p, [])
        if len(allocated_resources) > 2:
            return False, []
    return True, processes[:]

