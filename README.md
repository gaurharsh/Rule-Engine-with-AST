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
##### Web Server: Gunicorn (for deployment) or Django’s development serve
