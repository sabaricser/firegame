import os

file_path = r'c:\Users\Chandru\Desktop\game pro\main.py'
with open(file_path, 'r') as f:
    lines = f.readlines()

new_lines = []
indent_next = False
for i, line in enumerate(lines):
    # Find the while loop start
    if 'while running:' in line and 'async def main' not in lines[i-1]: # secondary check
        new_lines.append(line)
        indent_next = True
        continue
    
    if indent_next:
        # Stop indenting at the end of main
        if 'pygame.mixer.music.stop()' in line:
            indent_next = False
            new_lines.append(line)
            continue
        
        # Don't indent empty lines
        if line.strip() == "":
            new_lines.append("\n")
        else:
            new_lines.append("    " + line)
    else:
        new_lines.append(line)

with open(file_path, 'w') as f:
    f.writelines(new_lines)
