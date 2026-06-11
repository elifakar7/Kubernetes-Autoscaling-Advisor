def calculate_status(cpu, memory, latency):
    if cpu > 85 or memory > 85 or latency > 300:
        return "critical_load"
    elif cpu > 70 or memory > 70 or latency > 150:
        return "high_load"
    elif cpu > 40 or memory > 40 or latency > 80:
        return "medium_load"
    else:
        return "low_load"


def calculate_replicas(cpu, memory, rps, latency):
    if cpu > 85 or memory > 85 or rps > 2000 or latency > 300:
        return 8
    elif cpu > 70 or memory > 70 or rps > 1000 or latency > 150:
        return 6
    elif cpu > 40 or memory > 40 or rps > 500 or latency > 80:
        return 4
    else:
        return 2


def calculate_layer(rps):
    if rps < 500:
        return "Pod"
    elif rps < 1500:
        return "Deployment"
    else:
        return "Node"


def estimate_monthly_cost(replicas):
    cost_per_replica_month = 20
    return replicas * cost_per_replica_month


def generate_recommendation(status, layer, replicas):
    return (
        f"System status is {status}. "
        f"Recommended scaling layer is {layer} with {replicas} replicas."
    )