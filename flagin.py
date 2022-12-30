import os
import re
import glob

source_flag = '/var/www/flaga/static/flag_image/*' # = os.path.join(os.getcwd(), '/var/www/flaga/static/flag_image/
#print(source_flag)
#file_list = os.listdir(source_flag)
file_list = glob.glob(source_flag)
print(type(file_list),"\n")
for file_i in file_list:
    print(file_i + '.jpg')
    #os.rename(file_i , file_i + '.jpg')
print("\nlalala:")