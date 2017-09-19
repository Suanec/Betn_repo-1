import os,sys

file_object = open('xxx-1_9100.csv')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )

lines = all_the_text.split('\r')
for i in range(len(lines)) :
  print i
  pairs = lines[i].split(',')
  dirName = pairs[0].split('/')[-1]
  os.system("mkdir " + dirName)
  os.system('wget -cP ' + os.path.abspath('.') + '/' + dirName + '/ ' + pairs[0])
  os.system('wget -cP ' + os.path.abspath('.') + '/' + dirName + '/ ' + pairs[1])
  print 'finished term of ' + str(i)


# scala
# rename MP4 files
# val dirs = "ls -1 ./" !!
# dirs.map{
#   dir =>
#     val dir_files = "ls -1 ./" + dir !!
#     val file = dir_files.split('\n').filter(_.contains(".mp4")).head
#     s"mv ${dir}/${file} ${dir}/${file.split('?').head}" !
# }

