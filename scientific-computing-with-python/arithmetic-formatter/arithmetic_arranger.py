def arithmetic_arranger(strings, solver="False"):
  operators = "+-"
  if len(strings) > 5:
    return "Error: Too many problems."

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
      return "Error: Numbers must only contain digits."

    if len(str(num)) > 4:
      return "Error: Numbers cannot be more than four digits."

  for op in oper:
    if op not in operators:
      return "Error: Operator must be '+' or '-'."

  tab = []

  for i in range(len(fir_nums)):
    tab.append(max(len(fir_nums[i]) + 2, len(sec_nums[i]) + 2))

  ar_for = ""
  i = 0

  for num in fir_nums:
    if len(num) < tab[i]:
      ar_for += (tab[i] - len(num)) * " "
    ar_for += str(num) + 4 * " "
    i += 1

  ar_for = ar_for[:-4]
  ar_for += "\n"
  i = 0

  for num in sec_nums:
    if len(num) + 2 < tab[i]:
      ar_for += oper[i] + ((tab[i] - len(num)) - 2) * " " + " "
    else:
      ar_for += oper[i] + " "
    ar_for += str(num) + 4 * " "
    i += 1

  ar_for = ar_for[:-4]
  ar_for += "\n"

  for i in tab:
    ar_for += (i * "-") + 4 * " "

  ar_for = ar_for[:-4]
  ar_for += "\n"

  if solver is True:
    for i in range(len(fir_nums)):
      if oper[i] == '+':
        calc = int(fir_nums[i]) + int(sec_nums[i])
      elif oper[i] == '-':
        calc = int(fir_nums[i]) - int(sec_nums[i])
      if len(str(calc)) < tab[i]:
        ar_for += (tab[i] - len(str(calc))) * " "
      ar_for += str(calc) + 4 * " "
    ar_for = ar_for[:-4]

  return ar_for.rstrip()

