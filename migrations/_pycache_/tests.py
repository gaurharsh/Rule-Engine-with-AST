from django.test import TestCase, Client
from django.urls import reverse
from rule_engine_app.models import Rule
import json

class RuleEngineTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_rule_success(self):
        """Test if a rule is successfully created and stored in the database."""
        rule_data = {'rule': 'age > 30 AND salary > 50000'}
        response = self.client.post(reverse('create_rule_view'), json.dumps(rule_data), content_type='application/json')
        
        # Check if the rule was created
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn('rule_id', response_json)
        
        # Ensure the rule is saved in the database
        rule = Rule.objects.get(id=response_json['rule_id'])
        self.assertIsNotNone(rule)

    def test_create_rule_empty(self):
        """Test submitting an empty rule string."""
        rule_data = {'rule': ''}
        response = self.client.post(reverse('create_rule_view'), json.dumps(rule_data), content_type='application/json')

        # Ensure an error message is returned
        self.assertEqual(response.status_code, 400)
        response_json = response.json()
        self.assertIn('error', response_json)

    def test_evaluate_rule_success(self):
        """Test rule evaluation for a matching data set."""
        # First create a rule
        rule_data = {'rule': 'age > 30 AND salary > 50000'}
        create_response = self.client.post(reverse('create_rule_view'), json.dumps(rule_data), content_type='application/json')
        rule_id = create_response.json()['rule_id']
        
        # Now test evaluation of the rule
        user_data = {'age': 35, 'salary': 60000}
        evaluate_response = self.client.post(reverse('evaluate_rule_view', args=[rule_id]), json.dumps(user_data), content_type='application/json')

        # Check if the rule evaluation was successful
        self.assertEqual(evaluate_response.status_code, 200)
        result = evaluate_response.json()['result']
        self.assertTrue(result)

    def test_evaluate_rule_failure(self):
        """Test rule evaluation for a non-matching data set."""
        # First create a rule
        rule_data = {'rule': 'age > 30 AND salary > 50000'}
        create_response = self.client.post(reverse('create_rule_view'), json.dumps(rule_data), content_type='application/json')
        rule_id = create_response.json()['rule_id']
        
        # Now test evaluation of the rule with non-matching data
        user_data = {'age': 25, 'salary': 30000}
        evaluate_response = self.client.post(reverse('evaluate_rule_view', args=[rule_id]), json.dumps(user_data), content_type='application/json')

        # Check if the rule evaluation was unsuccessful
        self.assertEqual(evaluate_response.status_code, 200)
        result = evaluate_response.json()['result']
        self.assertFalse(result)
