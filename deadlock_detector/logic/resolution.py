def suggest_resolution(cycles):
    """
    Suggest resolution strategies for detected deadlock cycles.
    
    Args:
        cycles (list): List of cycles found
    
    Returns:
        list: List of resolution suggestions
    """
    if not cycles:
        return []
    
    # Extract all processes involved in any cycle
    all_processes = set()
    for cycle in cycles:
        all_processes.update(cycle)
    
    processes_list = list(all_processes)
    
    suggestions = [
        f"1. Terminate lowest priority process: {processes_list[0]}",
        f"2. Preempt resource from {processes_list[1] if len(processes_list) > 1 else processes_list[0]}",
        "3. Rollback transactions to previous checkpoint",
        "4. Implement resource ordering to prevent circular wait",
        "5. Use Banker's Algorithm for safe resource allocation",
        "6. Timeout mechanism for resource requests"
    ]
    
    return suggestions

