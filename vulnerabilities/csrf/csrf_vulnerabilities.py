import re

def find_csrf_vulnerabilities(code):
        pattern = r'(?:\b|_)csrf(?:\b|_)|CSRFToken|anti_csrf_token|csrfmiddlewaretoken'
        matches = re.finditer(pattern, code, re.IGNORECASE)
        vulnerabilities = []
        for match in matches:
            vulnerability = {
                'type': 'CSRF (Cross-Site Request Forgery)',
                'pattern': match.group(),
                'line_number': code.count('\n', 0, match.start()) + 1
            }
            vulnerabilities.append(vulnerability)
        return vulnerabilities