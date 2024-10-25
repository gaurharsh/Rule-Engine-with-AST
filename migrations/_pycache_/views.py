# rule_engine_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Rule
from ast_utils import create_rule
import json
# rule_engine_app/views.py

from django.shortcuts import render

def index_view(request):
    return render(request, 'rule_engine_app/index.html')


@csrf_exempt  # Use this only for testing; handle CSRF properly in production
def create_rule_view(request):
    if request.method == 'POST':
        try:
            # Expecting a JSON payload
            data = json.loads(request.body)
            rule_string = data.get('rule')
 
            if not rule_string:
                return JsonResponse({'error': 'Rule string is required.'}, status=400)

            # Generate AST
            ast = create_rule(rule_string)

            # Convert the AST to a dictionary for JSON serialization
            rule_data = {
                'node_type': ast.node_type,
                'value': ast.value,
                'left': ast.left.__dict__ if ast.left else None,
                'right': ast.right.__dict__ if ast.right else None
            }

            # Store AST as JSON in the database
            rule = Rule.objects.create(name="Sample Rule", ast=rule_data)
            return JsonResponse({'rule_id': rule.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


def evaluate_node(node, data):
    if node['node_type'] == 'operand':
        attribute, condition = node['value'].split(' ', 1)
        if ">" in condition:
            return data[attribute] > int(condition.split(">")[1].strip())
        elif "<" in condition:
            return data[attribute] < int(condition.split("<")[1].strip())
        elif "=" in condition:
            return data[attribute] == condition.split("=")[1].strip().strip("'")
    elif node['node_type'] == 'operator':
        if node['value'] == 'AND':
            return evaluate_node(node['left'], data) and evaluate_node(node['right'], data)
        elif node['value'] == 'OR':
            return evaluate_node(node['left'], data) or evaluate_node(node['right'], data)
    return False


def evaluate_rule_view(request, rule_id):
    try:
        rule = Rule.objects.get(id=rule_id)
        data = json.loads(request.body)  # User data as JSON
        result = evaluate_node(rule.ast, data)
        return JsonResponse({'result': result})
    except Rule.DoesNotExist:
        return JsonResponse({'error': 'Rule not found.'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON payload.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
