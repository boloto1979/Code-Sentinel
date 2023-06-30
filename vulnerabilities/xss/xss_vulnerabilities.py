import re

xss_pattern = re.compile(r'<script>.*?</script>|<img.*?src=.*?onerror=.*?>')

def find_xss_vulnerabilities(code):
    vulnerabilities = []
    matches = xss_pattern.findall(code)
    for match in matches:
        vulnerability = {
            'type': 'XSS (Cross-Site Scripting)',
            'pattern': match,
            'line_number': code.count('\n', 0, code.index(match)) + 1
        }
        vulnerabilities.append(vulnerability)
    return vulnerabilities
