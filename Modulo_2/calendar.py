calendar = {
  'january': '31',
  'febuary': '28',
  'march': '30',
  'april': '31',
  'may': '30',
  'june': '31',
  'july': '30',
  'august': '31',
  'september': '30',
  'october': '31',
  'november': '30',
  'december': '31'
}
key_list = calendar.keys()
value_list = calendar.values()
calendar_list = zip(key_list, value_list)

for key, value in calendar_list:
  formated_calendar = f'{key} - {value}'
  print(formated_calendar)