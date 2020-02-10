import time, os.path
from string import Template
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
    idpattern = '(?a:[a-z][a-z0-9]*)' #(?a:[_a-z][_a-z0-9]*) default
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')


t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))