import re

def find_xss_vulnerabilities(code):
    pattern = r'<script>.*</script>|<img.*src=.*onerror=.*>'
    matches = re.finditer(pattern, code)
    vulnerabilities = []
    for match in matches:
        vulnerability = {
            'type': 'XSS (Cross-Site Scripting)',
            'pattern': match.group(),
            'line_number': code.count('\n', 0, match.start()) + 1
        }
        vulnerabilities.append(vulnerability)
    return vulnerabilities