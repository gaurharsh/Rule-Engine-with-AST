 # Contains parsing, combining, and evaluating logic
# rule_engine.py

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" for AND/OR or "operand" for conditions
        self.left = left  # Left child node (for operators)
        self.right = right = right  # Right child node (for operators)
        self.value = value  # Condition (e.g., "age > 30" for operand)

# Function to create an AST from a rule string
def create_rule(rule_string):
    def parse_condition(condition):
        return Node(node_type="operand", value=condition.strip())

    def parse_rule(rule_string):
        if ' AND ' in rule_string:
            left, right = rule_string.split(' AND ', 1)
            return Node(node_type="operator", left=parse_rule(left), right=parse_rule(right), value="AND")
        elif ' OR ' in rule_string:
            left, right = rule_string.split(' OR ', 1)
            return Node(node_type="operator", left=parse_rule(left), right=parse_rule(right), value="OR")
        else:
            return parse_condition(rule_string)

    return parse_rule(rule_string)

# Function to combine multiple ASTs into a single AST
def combine_rules(rules):
    if len(rules) == 1:
        return rules[0]
    
    combined_ast = rules[0]
    for rule in rules[1:]:
        combined_ast = Node(node_type="operator", left=combined_ast, right=rule, value="AND")
    return combined_ast

# Function to evaluate the AST against user data
def evaluate_node(node, data):
    if node.node_type == "operand":
        attribute, condition = node.value.split(" ", 1)
        if ">" in condition:
            return data[attribute] > int(condition.split(">")[1].strip())
        elif "<" in condition:
            return data[attribute] < int(condition.split("<")[1].strip())
        elif "=" in condition:
            return data[attribute] == condition.split("=")[1].strip().strip("'")
    elif node.node_type == "operator":
        if node.value == "AND":
            return evaluate_node(node.left, data) and evaluate_node(node.right, data)
        elif node.value == "OR":
            return evaluate_node(node.left, data) or evaluate_node(node.right, data)
    return False

def evaluate_rule(data, rule_ast):
    return evaluate_node(rule_ast, data)
