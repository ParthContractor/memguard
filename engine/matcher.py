# Matcher
import yaml
import re

def load_patterns(yaml_path='engine/patterns.yaml'):
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
        patterns = []
        for item in data['patterns']:
            patterns.append({
                'id': item['id'],
                'description': item['description'],
                'regex': re.compile(item['regex'])
            })
        return patterns

def scan_file(file_path, patterns):
    results = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines, start=1):
            for pattern in patterns:
                if pattern['regex'].search(line):
                    results.append({
                        'file': file_path,
                        'line': i,
                        'text': line.strip(),
                        'id': pattern['id'],
                        'description': pattern['description']
                    })
    return results
