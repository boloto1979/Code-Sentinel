import re

def find_code_injection_vulnerabilities(code):
    pattern = r'eval\s*\(|exec\s*\(|os\.system\s*\(|subprocess\.run\s*\(|\$\(|`.*`'
    matches = re.finditer(pattern, code)
    vulnerabilities = []
    for match in matches:
        vulnerability = {
            'type': 'Code Injection',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)
    return vulnerabilities