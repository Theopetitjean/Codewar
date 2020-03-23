def filter_list(l):
  'return a new list with the strings filtered out'
  list_2 = [i for i in l if isinstance(i, (int, float))]
  return(list_2)
