# Contains unit tests for rule parsing, combining, and evaluating
# tests.py

from rule_engine import create_rule, combine_rules, evaluate_rule

# Test rule creation
def test_create_rule():
    rule_string = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule_string)
    assert ast.node_type == "operator"
    print("Test Create Rule: Passed")

# Test combining rules
def test_combine_rules():
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "salary > 50000 OR experience > 5"
    combined_ast = combine_rules([create_rule(rule1), create_rule(rule2)])
    assert combined_ast.node_type == "operator"
    print("Test Combine Rules: Passed")

# Test rule evaluation
def test_evaluate_rule():
    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    rule_string = "age > 30 AND department = 'Sales'"
    rule_ast = create_rule(rule_string)
    result = evaluate_rule(data, rule_ast)
    assert result == True
    print("Test Evaluate Rule: Passed")

# Run all tests
if __name__ == "__main__":
    test_create_rule()
    test_combine_rules()
    test_evaluate_rule()
