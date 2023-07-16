import re

def find_lfi_vulnerabilities(code):
    pattern = r'include\s*[\'"]\.\./|require\s*[\'"]\.\./|include_once\s*[\'"]\.\./|require_once\s*[\'"]\.\./'
    matches = re.finditer(pattern, code, re.IGNORECASE)
    vulnerabilities = []
    for match in matches:
        vulnerability = {
            'type': 'LFI (Local File Inclusion)',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)
    return vulnerabilities