import os

folder_path = input('Input folder path >> ')
count = int(input('Enter number to start naming from: '))

try:
    dir_list = os.listdir(folder_path)
except:
    print('Bad image location input. Please try again. Example: C:\\User\\John\\Desktop\\image.jpg')
for image in dir_list:

    if dir_list[-1] != '\\':
        path = folder_path + '\\' + image
    else:
        path = folder_path + image

    type = image.split('.')[-1]

    os.rename(path, folder_path+'\\'+str(count)+'.'+type)
    count += 1

print('All done')
