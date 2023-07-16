import re

def find_rfi_vulnerabilities(code):
    pattern = r'include\s*[\'"](http|https)://'
    matches = re.finditer(pattern, code, re.IGNORECASE)
    vulnerabilities = []
    for match in matches:
        vulnerability = {
            'type': 'RFI (Remote File Inclusion)',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)
    return vulnerabilities