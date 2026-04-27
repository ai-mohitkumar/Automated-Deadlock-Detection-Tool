def load_sample_deadlock():
    """
    Load sample data with deadlock.
    """
    processes = ['P1', 'P2']
    resources = ['R1', 'R2']
    allocation = {
        'P1': ['R1'],
        'P2': ['R2']
    }
    request = {
        'P1': ['R2'],
        'P2': ['R1']
    }
    return processes, allocation, request

def load_sample_safe():
    """
    Load sample data without deadlock.
    """
    processes = ['P1', 'P2']
    allocation = {
        'P1': ['R1'],
        'P2': ['R2']
    }
    request = {
        'P1': [],
        'P2': []
    }
    return processes, allocation, request

