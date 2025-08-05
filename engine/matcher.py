# matcher.py
import os
import yaml
import re

def load_patterns():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(current_dir, "patterns.yaml")

    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
        patterns = []
        for item in data['patterns']:
            patterns.append({
                'id': item['id'],
                'description': item['description'],
                'regex': re.compile(item['regex']),
                'prompt': item.get('prompt', None)  # optional for later
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
                        'code': line.strip(),  # unified key name
                        'description': pattern['description'],
                        'prompt': pattern.get('prompt', None),
                        'id': pattern['id']
                    })
    return results
