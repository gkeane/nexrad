import astral
import pytz
from datetime import datetime
dt = date_object = datetime.strptime('20140703','%Y%m%d')
loc=astral.Location( ('0','0',34.772,-76.8761,0,'') )
print(loc.longitude)



print(loc.dawn(dt,local=False))
dawn=loc.dawn(dt,local=False)
print(loc.dusk(dt,local=False))
dusk=loc.dusk(dt,local=False)

import os
import fnmatch
pattern = '*.gz'
for subdir, dirs, files in os.walk('./'):
    for file in fnmatch.filter(files, pattern):
      sub=file[-22:-8]
      #print file[-28:-22]
      #print sub
      dat=dt.strptime(sub,'%Y%m%d_%H%M%S')
      datware=pytz.utc.localize(dat)
      print str(dat)
      print str(datware)
      print str(dawn)
      if datware<dawn:
          print "remove"
          #os.remove(file)
      #print dat
      print file

