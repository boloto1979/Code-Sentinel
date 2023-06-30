import re

def find_sql_injection_vulnerabilities(code):
    pattern = r'SELECT\s+\*|DROP\s+TABLE|DELETE\s+FROM'
    matches = re.finditer(pattern, code, re.IGNORECASE)
    vulnerabilities = []
    for match in matches:
        vulnerability = {
            'type': 'SQL Injection',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)
    return vulnerabilities