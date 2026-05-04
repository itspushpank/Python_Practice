#Write  a  python  script  to  print  the  current  date  in  the  following  format  “WED  09 02:26:23   IST 2020”. 

import datetime

now= datetime.datetime.now()

formated_date= now.strftime("%a %d %H:%M:%S IST %Y").upper()

print(formated_date)