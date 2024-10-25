# Main entry point to test the API (optional)
# main.py
from rule_engine import create_rule, combine_rules, evaluate_rule

if __name__ == "__main__":
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "salary > 50000 OR experience > 5"
    
    # Create individual rules
    ast_rule1 = create_rule(rule1)
    ast_rule2 = create_rule(rule2)
    
    # Combine rules
    combined_ast = combine_rules([ast_rule1, ast_rule2])
    
    # Sample user data
    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    
    # Evaluate rule
    result = evaluate_rule(data, combined_ast)
    print(f"Is the user eligible? {result}")
