def arithmetic_arranger(strings, solver="False"):
  operators = "+-"
  if len(strings) > 5:
    print("Error: Too many problems.")
    return

  fir_nums = []
  oper = []
  sec_nums = []

  for string in strings:
    fir_nums.append(string.split(" ")[0])
    oper.append(string.split(" ")[1])
    sec_nums.append(string.split(" ")[2])

  all_nums = fir_nums + sec_nums

  for num in all_nums:
    if not str(num).isdigit():
        print("Error: Numbers must only contain digits.")
        return

    if len(str(num)) > 4:
        print("Error: Numbers cannot be more than four digits.")
        return

  for op in oper:
    if op not in operators:
      print("Error: Operator must be '+' or '-'.")
      return

  tab = []
  
  for i in range(len(fir_nums)):
    tab.append(max(len(fir_nums[i]) + 2, len(sec_nums[i]) + 2))

  i = 0
  for num in fir_nums:
    if len(num) < tab[i]:
      print((tab[i] - len(num)) * " ", end="")
    print(num, end= 4 * " ")
    i += 1
  
  print("")
  
  i = 0
  for num in sec_nums:
    if len(num) + 2 < tab[i]:
      print(oper[i] + ((tab[i] - len(num)) - 2) * " " , end=" ")
    else:
      print(oper[i], end=" ")
    print(num, end= 4 * " ")
    i += 1

  print("")

  for i in tab:
    print(i * "-", end=4 * " ")

  print("")

  if solver == True:
    for i in range(len(fir_nums)):
      if oper[i] == '+':
        calc = int(fir_nums[i]) + int(sec_nums[i])
      elif oper[i] == '-':
        calc = int(fir_nums[i]) - int(sec_nums[i])
      if len(str(calc)) < tab[i]:
        print( (tab[i] - len(str(calc))) * " ", end="")
      print(calc, end= 4 * " ")

