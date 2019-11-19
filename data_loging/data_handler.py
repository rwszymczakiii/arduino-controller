import csv
from datetime import datetime

sample_data = ['','a','','','','b', '','','c','','','','d', '','','e','a','','','','b', '','','c','','','','d', '','','e']

def convert_data(data):
  converted_data = []
  total_puff_count = 0
  cycle_count = 0
  a = f'Pump # : 1    at {datetime.now()}'
  b = f'Pump # : 2    at {datetime.now()}'
  c = f'Pump # : 3    at {datetime.now()}'
  d = f'Pump # : 4    at {datetime.now()}'
  e = f'Pump # : 5    at {datetime.now()}'

  while ('' in data):
    data.remove('')

  for i in data: 
    if i == 'a':
      cycle_count += 1
      a2 = f'--- Cycle # : {cycle_count}    at {datetime.now()} --- '
      converted_data.append(a2)
      converted_data.append(a)
      total_puff_count += 1
    elif i == 'b':
      converted_data.append(b)
      total_puff_count += 1
    elif i == 'c':
      converted_data.append(c)
      total_puff_count += 1
    elif i == 'd':
      converted_data.append(d)
      total_puff_count += 1
    elif i == 'e':
      converted_data.append(e)
      total_puff_count += 1
  
  converted_data.append(f'Run finished at {datetime.now()}')
  converted_data.append(f'Total Puffs : {total_puff_count}')

  return converted_data

converted_data = convert_data(sample_data)
print(converted_data)

def data_to_csv(data):
  with open("data_report.csv",'w') as f:
    writer = csv.writer(f,delimiter=" ")
    for i in data: 
      writer.writerow([i]) 

data_to_csv(converted_data)



