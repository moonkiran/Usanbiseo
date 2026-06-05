import os
import re

directory = r'e:\포폴\우산비서\usanbiseo\Usanbiseo'
html_files = ['index.html', 'login.html', 'signup.html', 'find_pw.html']

font_links = '  <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">\n  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap" rel="stylesheet">\n'

for filename in html_files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add font links if not present
    if 'family=Jua' not in content:
        content = content.replace('</head>', font_links + '</head>')
        
    # 2. Modify <style> block
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if style_match:
        style_content = style_match.group(1)
        
        # Strip existing font rules
        style_content = re.sub(r'\s*font-family:[^;}]+;?', '', style_content)
        style_content = re.sub(r'\s*font-weight:[^;}]+;?', '', style_content)
        style_content = re.sub(r'\s*font-size:[^;}]+;?', '', style_content)
        
        # Append new rules
        base_styles = '''
    body, input, button, select, textarea {
      font-family: 'Manrope', sans-serif;
      font-weight: 400;
      font-size: 16px;
    }
    
    .page-title {
      font-family: 'Jua', sans-serif;
      font-weight: 400;
      font-size: 22px;
    }
'''
        style_content += base_styles
        
        content = content[:style_match.start(1)] + style_content + content[style_match.end(1):]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Updated {filename}')
