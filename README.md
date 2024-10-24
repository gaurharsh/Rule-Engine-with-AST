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
##### Web Server: Django’s development server

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
        ` ` ` JSON 
                   {
                      "age": 35,
                      "department": "Sales",
                      "salary": 60000,
                      "experience": 3
                  }
                           
       ` ` `

## Test Cases
##### Create Rule: Use create_rule to generate ASTs from example rules and verify their representation.
##### Combine Rules: Combine rules using combine_rules and check if the logic is correctly reflected in the AST.
##### Evaluate Rules: Test evaluate_rule with various user data inputs and rules to verify expected outcomes.
##### Extend Rules: Explore combining more rules and testing them with different scenarios.



## Setup Instructions
#### Step 1: Clone the repository<br>
                  ` ` ` cmd
                             git clone https://github.com/gaurharsh/Rule-Engine-with-AST.git

                  ` ` `
#### Step 2: Set Up a Virtual Environment<br>
                   ` ` ` console
                               cd <project-directory>
                               python -m venv env

                   ` ` ` 

                   ` ` `console 
                               .\env\Scripts\activate
                            
                   ` ` `
#### Step 3: Install Dependencies<br>
                    ` ` `console
                               pip install -r requirements.txt

                    ` ` `
#### Step 4: Set Up the Database<br>
                    ` ` `console
                               python manage.py migrate

                    ` ` `
#### Step 5: Start the Django Development Server<br>
                    ` ` `console
                                python manage.py runserver

                    ` ` `

#### Step 6: Access the Front-End<br>  Open your browser and visit:  http://127.0.0.1:8000<br>


 ### Project Structure:

 #### rule-engine-app/<br>
│
├── rule_engine_app/<br>            # Django project folder
│   ├── __init__.py<br>
│   ├── asgi.py<br>
│   ├── settings.py<br>          # Project settings
│   ├── urls.py<br>            # Project-level URLs
│   ├── wsgi.py<br>

<br>

├── rule_engine/ <br>              # Django app folder for rule engine
│   ├── migrations/<br>             # Database migrations
│   ├── templates/<br>              # HTML templates for the front-end
│   ├── static/<br>                # Static files (CSS, JavaScript)
│   ├── __init__.py<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>               # Models for rules and attributes
│   ├── views.py<br>                # API and UI logic
│   ├── urls.py<br>                # App-level URLs
│   ├── forms.py<br>                # UI forms for rule entry
│
├── manage.py<br>                  # Django management script
├── requirements.txt<br>            # Project dependencies
└── README.md<br>                   # Project description

  

 
 ## Bonus Features
 
##### Error Handling: Handle invalid rules or missing operators/comparisons.
##### Validation: Ensure attributes used in the rules are part of a predefined catalog.
##### Rule Modification: Add functionality to modify existing rules by changing operators, operand values, or adding/removing sub-expressions.
##### Advanced Conditions: Extend the system to support user-defined functions for more complex rules.    


## Future Enhancements
##### Add more robust error handling and validation features.
##### Support combining a larger number of rules efficiently.
##### Extend the front-end with a rule-building interface for non-technical users.                  

## Screenshorts




#### License
This project is licensed under the MIT License. See the LICENSE file for details.<br>


#### Author
Harshvardhan








