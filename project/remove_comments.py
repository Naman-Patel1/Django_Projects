import os
import re

base_dir = r"c:\Users\jitin\Desktop\django project"

def remove_python_comments(text):
    lines = text.split('\n')
    new_lines = []
    for line in lines:
        if line.strip().startswith('#'):
            continue
        new_lines.append(line)
        
    result = '\n'.join(new_lines)
    result = re.sub(r'', '', result)
    return result

def remove_html_comments(text):
    return re.sub(r'<!--[\s\S]*?-->', '', text)

count = 0
for root, dirs, files in os.walk(base_dir):
    if 'venv' in root or '.git' in root or '.idea' in root or '__pycache__' in root:
        continue
        
    for file in files:
        filepath = os.path.join(root, file)
        
        if file.endswith('.py'):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = remove_python_comments(content)
            new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content) # Cleanup extra spacing
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content.strip() + '\n')
                count += 1
                
        elif file.endswith('.html'):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = remove_html_comments(content)
            new_content = re.sub(r'\n\s*\n', '\n', new_content) # Cleanup extra spacing
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content.strip() + '\n')
                count += 1

print(f"Removed comments and cleaned up {count} project files.")
