import os

file_path = r'c:\Users\Chandru\Desktop\game pro\main.py'
with open(file_path, 'r') as f:
    lines = f.readlines()

new_lines = []
in_main = False
for line in lines:
    if 'async def main():' in line:
        in_main = True
        new_lines.append(line)
        continue
    
    if in_main:
        # If it's the global declaration or the while loop start, it's already indented correctly (presumably)
        # Actually, let's just indent everything after 'async def main():' and before 'if __name__ =='
        if 'if __name__ == "__main__":' in line:
            in_main = False
            new_lines.append(line)
            continue
        
        # Don't indent if it's already properly indented or empty
        if line.strip() == "":
            new_lines.append("\n")
        elif line.startswith("    "):
            new_lines.append(line)
        else:
            new_lines.append("    " + line)
    else:
        new_lines.append(line)

with open(file_path, 'w') as f:
    f.writelines(new_lines)
