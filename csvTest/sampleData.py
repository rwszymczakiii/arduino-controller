sample_data = ['','a','','','','b', '','','c','','','','d', '','','e','a','','','','b', '','','c','','','','d', '','','e']

def convert_data(data):
  converted_data = []
  cycle_count = 1
  total_puff_count = 0
  a = f'--- Cycle # : {cycle_count} --- '
  a2 = 'Pump # : 1'
  b = 'Pump # : 2'
  c = 'Pump # : 3'
  d = 'Pump # : 4'
  e = 'Pump # : 5'

  while ('' in data):
    data.remove('')

  for i in data: 
    if i == 'a':
      cycle_count += 1
      converted_data.append(a)
      converted_data.append(a2)
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

  print(converted_data, total_puff_count)

convert_data(sample_data)


