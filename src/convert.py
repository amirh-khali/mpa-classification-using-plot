import json

with open('MovieClassificationBasedOnMPARatingUsingPlot.ipynb', 'r') as f:
  notebook = json.load(f)
  
parts = ['Data Collection','Preprocessing', 'Stats']
cells = notebook['cells']

for p in parts:
  with open(f"{p}.py", 'w') as f:
    f.write('')
  curq = None

  for i in range(3):
    cell = cells[i]
    with open(f"{p}.py", 'a+') as f:
        f.writelines(cell['source'])
        f.write('\n\n')

  for cell in cells:
    if cell['cell_type'] == 'markdown' and p in cell['source'][0]:
      curq = p
      continue
    elif cell['cell_type'] == 'markdown' and curq is not None and p not in cell['source'][0] and '# ' in 	cell['source'][0] :
      break
    elif cell['cell_type'] == 'code' and curq is not None:
      with open(f"{p}.py", 'a+') as f:
        f.writelines(cell['source'])
        f.write('\n\n')

with open(f"all.py", 'w') as f:
    f.write('')
for cell in cells:
  with open(f"all.py", 'a+') as f:
    f.writelines(cell['source'])
    f.write('\n\n')
