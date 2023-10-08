def add_time(start_time, duration_time, day="False"):
  week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
          "Sunday")
  full_time = ""
  later = 0

  st = start_time.split()
  st[0] = st[0].split(':')
  st = st[0] + [st[1]]
  dt = duration_time.split(":")

  st_h = int(st[0])
  st_m = int(st[1])
  st_ind = str(st[2])
  dt_h = int(dt[0])
  dt_m = int(dt[1])

  for _hour in range(dt_h):
    st_h += 1
    if st_h == 13:
      st_h = 1
      if st_ind == "PM":
        later += 1
        st_ind = "AM"
      elif st_ind == "AM":
        st_ind = "PM"

  for _minute in range(dt_m):
    st_m += 1
    if st_m == 60:
      st_m = 0
      st_h += 1
    if st_h == 12 and st_m == 1:
      if st_ind == "PM":
        later += 1
        st_ind = "AM"
      elif st_ind == "AM":
        st_ind = "PM"

  full_time += str(st_h) + ':'
  if st_m < 10:
    full_time += '0'
  full_time += str(st_m) + ' ' + str(st_ind)

  if day != "False":
    day = day.capitalize()  # Capitalize the input day
    if day in week:
      idx = week.index(day)
      for i in range(later):
        idx += 1
        if idx == 7:
          idx = 0
      full_time += ", " + week[idx]

  if later == 1:
    full_time += " (next day)"
  elif later > 1:
    full_time += " ({:d} days later)".format(later)

  return full_time

