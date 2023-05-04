import json

my_list = "";

def refs(line):
  line = line + '<br>\n'
  return line

def questions(line):
  if '1/(N - 1) - 1/N ≈ 1/N2 ∝ d2' in line:
    line = "<blockquote>" + line + "</blockquote> \n"
  if line[0].isdigit():
    line = "<br><br><b>" + line + "</b><br> \n"
  elif line.startswith("-"):
    line = "<br><b>" + line[1:] + "</b><br> \n" 
  else: 
    line += line + '\n' 
  return line

with open('toparse.txt', encoding='utf8') as f:
    lines = f.readlines() # list containing lines of file

    for line in lines:
      line = line.strip() # remove leading/trailing white spaces
      try:
        if line:
          line = refs(line)
          my_list += line
      except: pass

print(my_list)