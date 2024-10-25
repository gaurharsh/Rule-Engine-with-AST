document.getElementById('rule-form').addEventListener('submit', function(event) {
            event.preventDefault();

            const ruleInput = document.getElementById('rule');
            const rule = ruleInput.value;
            const resultDiv = document.getElementById('result');

            if (rule.trim() === '') {
                resultDiv.innerText = 'Please enter a rule!';
                resultDiv.classList.add('error');
                resultDiv.style.display = 'block';
                return;
            }

            // Clear previous results
            resultDiv.style.display = 'none';
            resultDiv.classList.remove('error');

            fetch('/create-rule/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ rule: rule }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.rule_id) {
                    resultDiv.innerText = 'Rule successfully submitted! Rule ID: ' + data.rule_id;
                    resultDiv.classList.remove('error');
                    resultDiv.style.display = 'block';
                } else {
                    resultDiv.innerText = 'Error submitting rule. Please try again.';
                    resultDiv.classList.add('error');
                    resultDiv.style.display = 'block';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                resultDiv.innerText = 'An error occurred. Please try again.';
                resultDiv.classList.add('error');
                resultDiv.style.display = 'block';
            });
        });
