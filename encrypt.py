import os


def prepare_key(key, encrypt_or_decrypt):

    # The key is split into a list of numbers by pairs =========================
    key = str(key)
    keys_str = [key[i:i+2] for i in range(0, len(key), 2)]

    # Check if it's encryption or decryption ===================================
    # All pairs of keys should have a pair.
    for i in keys_str:
        if len(i) < 2:
            i = i + '0'

    keys = [int(i) for i in keys_str]

    # Decryption must use the entered key in reverse ===========================
    if encrypt_or_decrypt == 'dec':
        keys.reverse()
        return (keys)
    elif encrypt_or_decrypt == 'enc':
        return (keys)
    else:
        print('Wrong input. Please specify "enc" for encryption and "dec" for decryption')
        return


def check_path(path):

    if '.' in path:
        return 'file'
    else:
        return 'folder'


def encrypt_file():
    pass


def encrypt(encrypt_or_decrypt):

    print('')
    path = input(r'Enter path of Image or Folder : ')
    print('')

    try:
        key = int(input('Enter Key for encryption/decryption of Image : '))
    except:
        print('\nKey must be a number. Please try again. Example: 52')
        return

    print('\nThe path of file : ', path)
    print('\nKey for encryption : ', key)

    try:
        keys = prepare_key(key, encrypt_or_decrypt)
    except:
        print('Wrong input. Please specify "enc" for encryption and "dec" for decryption')
        return

    mode = check_path(path)

    print('\nThe path of file : ', path)
    print('\nKey for encryption : ', key)

    if mode == 'file':

        pass_count = 1
        for i in keys:
            try:
                fin = open(path, 'rb')
                image = fin.read()
                fin.close()
            except:
                print(
                    '\nBad path input. Please try again. Example: C:\\User\\John\\Desktop\\image.jpg')
                return

            image = bytearray(image)

            for index, values in enumerate(image):
                image[index] = values ^ i

            fin = open(path, 'wb')
            fin.write(image)
            fin.close()

            print(f'\n[ Pass [{pass_count}] Encryption\Decryption is Done! ]')
            pass_count += 1

    elif mode == 'folder':

        pass_count = 1
        for i in keys:
            try:
                dir_list = os.listdir(path)
            except:
                print(
                    '\nBad path input. Please try again. Example: C:\\User\\John\\Desktop\\image.jpg')
                return

            count = 1
            for image in dir_list:
                if dir_list[-1] != '\\':
                    img_path = path + '\\' + image
                else:
                    img_path = path + image

                fin = open(img_path, 'rb')
                image = fin.read()
                fin.close()

                image = bytearray(image)

                for index, values in enumerate(image):
                    image[index] = values ^ i

                fin = open(img_path, 'wb')
                fin.write(image)
                fin.close()

                print(
                    f'\n[ Pass [{pass_count}] Encryption\Decryption on image #{count} Done!]')

                img_path = ''
                count += 1


if __name__ == '__main__':

    encrypt_or_decrypt = input('Encrypt or Decrypt? [enc/dec]: ')

    encrypt(encrypt_or_decrypt)
