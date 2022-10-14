import os


def encrypt(mode):

    if mode.lower() == 'image':
        print('')
        path = input(r'Enter path of Image : ')
        print('')
        print('Note: Max lenght of a key is 2 digits')
        try:
            key = int(input('Enter Key for encryption/decryption of Image : '))
        except:
            print('\nKey must be a number. Please try again. Example: 52')
            return
        print('\nThe path of file : ', path)
        print('\nKey for encryption : ', key)

        try:
            fin = open(path, 'rb')
            image = fin.read()
            fin.close()
        except:
            print(
                '\nBad image location input. Please try again. Example: C:\\User\\John\\Desktop\\image.jpg')
            return

        image = bytearray(image)

        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()

        print('\n[ Encryption\Decryption is Done! ]')

    elif mode.lower() == 'folder':
        print('')
        folder_path = input(r'Enter path of folder : ')
        print('')
        print('Note: Max lenght of a key is 2 digits')
        try:
            key = int(input('Enter Key for encryption/decryption : '))
        except:
            print('\nKey must be a number. Please try again')
            return

        print('\nThe path of file : ', folder_path)
        print('\nKey for encryption : ', key)

        try:
            dir_list = os.listdir(folder_path)
        except:
            print(
                '\nBad image location input. Please try again. Example: C:\\User\\John\\Desktop\\image.jpg')
            return

        count = 1
        for image in dir_list:
            if dir_list[-1] != '\\':
                path = folder_path + '\\' + image
            else:
                path = folder_path + image

            fin = open(path, 'rb')
            image = fin.read()
            fin.close()

            image = bytearray(image)

            for index, values in enumerate(image):
                image[index] = values ^ key

            fin = open(path, 'wb')
            fin.write(image)
            fin.close()

            print(f'\n[ {str(count)} Encryption\Decryption Done!]')

            count += 1
    else:
        print('Wrong mode. Please try again (image/folder)')


if __name__ == '__main__':

    mode = input('Select mode [folder/image]: ')

    encrypt(mode)
