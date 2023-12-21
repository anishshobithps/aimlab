def calculate_cost(graph_weights, condition, weight=1):
    cost = {}
    if 'AND' in condition:
        and_nodes = condition['AND']
        cost[' AND '.join(and_nodes)] = sum(graph_weights[node] + weight for node in and_nodes)
 
    if 'OR' in condition:
        or_nodes = condition['OR']
        cost[' OR '.join(or_nodes)] = min(graph_weights[node] + weight for node in or_nodes)

    return cost

def update_cost(graph_weights, conditions, weight=1):
    least_cost = {}
    for key, current_condition in reversed(conditions.items()):
        current_cost = calculate_cost(graph_weights, current_condition, weight)
        graph_weights[key] = min(current_cost.values())
        least_cost[key] = current_cost
        print(f'{key}: {conditions[key]} >>> {current_cost}')
    
    return least_cost

def shortest_path(start, updated_cost, graph_weights):
    if start not in updated_cost:
        return start
    
    min_cost_key, min_cost = min(updated_cost[start].items(), key=lambda x: x[1])

    if len(min_cost_key.split()) == 1:
        return start + '<--' + shortest_path(min_cost_key, updated_cost, graph_weights)
    else:
        return (
            start + '<--(' + min_cost_key + ') [' +
            shortest_path(min_cost_key.split()[0], updated_cost, graph_weights) + ' + ' +
            shortest_path(min_cost_key.split()[-1], updated_cost, graph_weights) + ']'
        )

H =  {'A':1,'B':6,'C':2,'D':12,'E':2,'F':1,'G':5,'H':7,'I':7,'J':1,'T':3}

conditions = {
    'A': {'AND': ['B', 'C'], 'OR': ['D']},
    'B': {'AND': ['G'], 'OR':['H']},
    'C': {'AND': ['J']},
    'D': {'AND': ['E'], 'OR': ['F']},
    'G': {'AND': ['I']}
}

updated_cost = update_cost(H, conditions, weight=1)
print('Shortest Path:\n', shortest_path('A', updated_cost, H))