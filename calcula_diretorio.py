import os

dir_info = open('.dir_info.txt', 'w')

def calcula_diretorio():

    try:

        diretorio_atual = os.listdir('.')
        
        total_size = 0

        dir_info.write('--No diretório ' + os.getcwd() + '--\n\n')
        print('No diretório ' + os.getcwd() + '\n')

        for file in diretorio_atual:
            if os.path.isdir(os.path.join(os.path.dirname('.'), file)):
                dir_info.write('\n')
                print()
                os.chdir(os.path.join(os.path.dirname('.'), file))
                total_size += calcula_diretorio()
                os.chdir('..')

            size = os.path.getsize(os.path.join(os.path.dirname('.'), file))
            dir_info.write(os.getcwd() + ' -> O arquivo ' + file + ' possui: ' + format(size, ',d') + ' bytes de tamanho\n')
            print(os.getcwd() + ' -> O arquivo ' + file + ' possui: ' + format(size, ',d') + ' bytes de tamanho')
            total_size = total_size + size

        dir_info.write('\n')
        print()

        if total_size < 1024:
            dir_info.write('--Soma total dos tamanhos dos arquivos em ' + os.getcwd() + ': ' + format(total_size, ',d') + ' bytes--\n')
            print('\nSoma total dos tamanhos dos arquivos em ' + os.getcwd() + ': ' + format(total_size, ',d') + ' bytes')
        elif total_size >= 1024 and total_size < 1024*(10**3):
            dir_info.write('--Soma total dos tamanhos dos arquivos em ' + os.getcwd() + ': ' + format(total_size/1024, ',.2f') + 'KB--\n')
            print('--Soma total dos tamanhos dos arquivos em ' + os.getcwd() + ': ' + format(total_size/1024, ',.2f') + 'KB--')
        elif total_size >= 1024*(10*3) and total_size < 1024*(10**6):
            dir_info.write('--Soma total dos tamanhos dos arquivos em ' + os.getcwd() + ': ' + format(total_size/(1024*(10**3)), ',.2f') + 'MB--\n')
            print('Soma total dos tamanhos dos arquivos em ' + os.getcwd() + ': ' + format(total_size/(1024*(10**3)), ',.2f') + 'MB')
        elif total_size >= 1024*(10**6):
            dir_info.write('--Soma total dos tamanhos dos arquivos em ' + os.getcwd() + ': ' + format(total_size/(1024*(10**6)), ',.2f') + 'GB--\n')
            print('Soma total dos tamanhos dos arquivos em ' + os.getcwd() + ': ' + format(total_size/(1024*(10**6)), ',.2f') + 'GB')

        dir_info.write('\n')
        print()

        return total_size

    except PermissionError:
        dir_info.write('--Permission denied.--\n\n')
        print('Permission denied.')
        return 0
    except FileNotFoundError:
        dir_info.write('--File not found.--\n\n')
        print('File not found.')
        return 0

calcula_diretorio()
dir_info.close()