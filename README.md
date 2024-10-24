# Rule-Engine-with-AST
Rule Engine with AST  is a 3-tier rule engine that determines user eligibility based on attributes like age, department, income, and experience. It uses an Abstract Syntax Tree (AST) to represent and manage rules dynamically, enabling easy creation, combination, and modification of conditions

## Key features include:

#####  Rule Creation: Build rules from conditional statements using an AST structure.
##### Rule Combination: Combine multiple rules efficiently into a single AST, minimizing redundancy.
##### Rule Evaluation: Test user data against the rules to determine eligibility.
##### Error Handling: Manage invalid rule inputs and data formats.
##### Rule Modification: Update existing rules by changing conditions or combining new rules.
##### Validation: Ensure that attributes in the rules are part of a valid catalog.

## Tech Stack
##### Backend: Django (Python-based web framework)
##### API: Django REST Framework for creating and evaluating rules
##### Frontend: HTML/CSS for a simple user interface
##### Database: PostgreSQL (or SQLite for development) for storing rules and metadata
##### Data Storage: JSON for AST representation
##### Web Server: Gunicorn (for deployment) or Django’s development server

## Data Structure
#### The AST is represented by a Node data structure with the following fields:

##### type: String indicating the node type (operator for AND/OR, operand for conditions).
##### left: Reference to another Node (left child).
##### right: Reference to another Node (right child for operators).
##### value: Optional value for operand nodes (e.g., numbers for comparisons).


## Example Rules
##### Rule 1: "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
##### Rule 2: "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

## Data Storage
#### A database (e.g., PostgreSQL or SQLite) is used to store rules and related application metadata. The schema for storing rules could include:

##### id: Rule ID.
##### rule_string: The string representation of the rule.
##### ast_structure: The AST structure in JSON format.
##### created_at: Timestamp of when the rule was created.
##### modified_at: Timestamp of the last modification

## API Design
#####  create_rule(rule_string):
######     Takes a string representing a rule and converts it into an AST, returning a Node object.
#####  combine_rules(rules):
######     Takes a list of rule strings and combines them into a single AST, optimizing for efficiency.
##### evaluate_rule(JSON data):
######     Takes a JSON of the combined rule's AST and a dictionary of user data, evaluating if the user meets the conditions of the rule.

Example input:
` ` `
                {
                    "age": 35,
                    "department": "Sales",
                    "salary": 60000,
                  "experience": 3
               }
` ` `
