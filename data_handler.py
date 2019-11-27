import csv
from datetime import datetime
from itertools import zip_longest
# from main import start_time

# sample_data = ['','a','a','a','a','a','a','','b','b','b','b','b','b','b','b','','','c','c','c','c','c','c','','','','d','d','d','d','d','d','d','d','','','e','','','a','a','a','a','a','a','','','','b','b','b','b','b','b','b','b','b','','','c','c','c','c','c','c','','','','d','d','d','d','d','d','','','e','','','','a','a','a','a','a','a','','b','b','b','b','b','b','b','b','','','c','c','c','c','c','c','','','','d','d','d','d','d','d','d','d','','','e','','','a','a','a','a','a','a','','','','b','b','b','b','b','b','b','b','b','','','c','c','c','c','c','c','','','','d','d','d','d','d','d','','','e','','']

def convert_data(data):
  converted_data = []
  total_puff_count = 0
  cycle_count = 0

  while ('' in data):
    data.remove('')

  # for i in data: 
  #   try:
  #     if i != data[data.index(i)+1] and i != data[data.index(i)-1]:
  #       data.remove(i)
  #   except:
  #     break

  # data.remove(data[len(data)-1])

  def remove_consecutive_duplicates(lst):
    ahead = iter(lst)
    next(ahead)
    return [ x for x, y in zip_longest(lst, ahead) if x and x != y ]

  data = remove_consecutive_duplicates(data)

  # print(data)

  a = f'Pump # : 1'
  b = f'Pump # : 2'
  c = f'Pump # : 3'
  d = f'Pump # : 4'
  e = f'Pump # : 5'
  f = f'Pump # : 6'
  g = f'Pump # : 7'
  h = f'Pump # : 8'
  i = f'Pump # : 9 '
  j = f'Pump # : 10'

  for i in data: 
    if i == 'a':
      cycle_count += 1
      a2 = f'--- Cycle # : {cycle_count}'
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
    elif i == 'f':
      converted_data.append(f)
      total_puff_count += 1
    elif i == 'g':
      converted_data.append(g)
      total_puff_count += 1
    elif i == 'h':
      converted_data.append(h)
      total_puff_count += 1
    elif i == 'i':
      converted_data.append(i)
      total_puff_count += 1
    elif i == 'j':
      converted_data.append(j)
      total_puff_count += 1
  
  # converted_data.append(f'Run finished at {datetime.now()}')
  # converted_data.append(f'Total Puffs : {total_puff_count}')

  return converted_data

# convert_data(sample_data)
# converted_data = convert_data(sample_data)

def data_to_csv(data):
  with open("./data_report.csv",'a') as f:
    writer = csv.writer(f,delimiter=" ")
    for i in data: 
      writer.writerow([i])

# data_to_csv(converted_data)