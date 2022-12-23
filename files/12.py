import signal
import sys
import random
import keyboard

keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
keyboard.add_hotkey("win", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + c", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + break", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + alt", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + alt + delete", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + f", lambda: None, suppress =True)
keyboard.add_hotkey("space", lambda: None, suppress =True)
keyboard.add_hotkey("c", lambda: None, suppress =True)

msize = ['2', '4', '6', '8']
mchoice = ['1', '2']
mx = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
      '11', '12', '13', '14', '15', '16', '17', '18', '19' ,'20',
      '21', '22', '23', '24', '25', '26', '27', '28', '29' ,'30',
      '31', '32', '33', '34', '35', '36', '37', '38', '39' ,'40',
      '41', '42', '43', '44', '45', '46', '47', '48', '49' ,'50',
      '51', '52', '53', '54', '55', '56', '57', '58', '59' ,'60',
      '61', '62', '63', '64', '65', '66', '67', '68', '69' ,'70',
      '71', '72', '73', '74', '75', '76', '77', '78', '79' ,'80',
      '81', '82', '83', '84', '85', '86', '87', '88', '89' ,'90',
      '91', '92', '93', '94', '95', '96', '97', '98', '99' ,'100']

############################# Выбор размера матрицы
print("Matrix size, 2, 4, 6, 8: ", end='')
while True:
    try:
        tempsize = str(input())
        if not (tempsize in msize):
            print("You entered the wrong value! Matrix size, 2, 4, 6, 8: " , end='')
        else:
            size = int(tempsize) 
            break
    except ValueError:
        pass
    except Exception:
        print("Don't press the ctrl key! Matrix size, 2, 4, 6, 8: " , end='')
    except KeyboardInterrupt:
        print("")
        print("Don't press the ctrl key! Matrix size, 2, 4, 6, 8: " , end='')


############################# Выбор вводимых значений
print("Would you like to enter the numbers yourself? 1 - Yes, 2 - No: ", end='')
while True:
    try:
        choice = str(input())
        if not (choice in mchoice):
            print("You entered the wrong value! Would you like to enter the numbers yourself? 1 - Yes, 2 - No: " , end='')
        else:
            size = int(tempsize) 
            break
    except ValueError:
        pass
    except Exception:
        print("Don't press the ctrl key! Would you like to enter the numbers yourself? 1 - Yes, 2 - No: " , end='')
    except KeyboardInterrupt:
        print("")
        print("Don't press the ctrl key! Would you like to enter the numbers yourself? 1 - Yes, 2 - No: " , end='')


############################# Создание матрицы
matrix = []

############################# Ввод своих чисел в матрицу 
count = 0
if choice == '1':
    while True:
        try:
            if count < size * size: 
                print("Enter a number: ", end='')
                x = str(input())
                if not (x in mx):
                    print("You entered the wrong value! ", end='')
                else:
                    matrix.append(int(x))
                    count += 1
            else:
                break
        except ValueError:
            pass
        except Exception:
            print("Don't press the ctrl key! " , end='')
        except KeyboardInterrupt:
            print("")
            print("Don't press the ctrl key! " , end='')   

############################# Ввод случайных чисел в матрицу 
if choice == '2':
    for i in range(size * size): 
        matrix.append(random.randint(1, 10))

print("Entered matrix:")
############################# Вывод матрицы
if size == 2:
  for i in range(0, 2):
      print(matrix[i], end=' ')
  print()
  for i in range(2, 4):
      print(matrix[i], end=' ')
  print("\n---------------------------------")
  print("Sorted Matrix:")
  matrix.sort(reverse=True)
  for i in range(0, 2):
      print(matrix[i], end=' ')
  print()
  for i in range(2, 4):
      print(matrix[i], end=' ')
############################################ 4 размер
if size == 4:
  for i in range(0, 4):
      print(matrix[i], end=' ')
  print()
  for i in range(4, 8):
      print(matrix[i], end=' ')
  print()
  for i in range(8, 12):
      print(matrix[i], end=' ')
  print()
  for i in range(12, 16):
      print(matrix[i], end=' ')
  print("\n---------------------------------")
  print("Sorted Matrix:")
  matrix.sort(reverse=True)
  for i in range(0, 4):
      print(matrix[i], end=' ')
  print()
  for i in range(4, 8):
      print(matrix[i], end=' ')
  print()
  for i in range(8, 12):
      print(matrix[i], end=' ')
  print()
  for i in range(12, 16):
      print(matrix[i], end=' ')
############################################ 6 размер
if size == 6:
  for i in range(0, 6):
      print(matrix[i], end=' ')
  print()
  for i in range(6, 12):
      print(matrix[i], end=' ')
  print()
  for i in range(12, 18):
      print(matrix[i], end=' ')
  print()
  for i in range(18, 24):
      print(matrix[i], end=' ')
  print()
  for i in range(24, 30):
      print(matrix[i], end=' ')
  print()
  for i in range(30, 36):
      print(matrix[i], end=' ')
  print("\n---------------------------------")
  print("Sorted Matrix:")
  matrix.sort(reverse=True)
  for i in range(0, 6):
      print(matrix[i], end=' ')
  print()
  for i in range(6, 12):
      print(matrix[i], end=' ')
  print()
  for i in range(12, 18):
      print(matrix[i], end=' ')
  print()
  for i in range(18, 24):
      print(matrix[i], end=' ')
  print()
  for i in range(24, 30):
      print(matrix[i], end=' ')
  print()
  for i in range(30, 36):
      print(matrix[i], end=' ')
############################################ 8 размер
if size == 8:
  for i in range(0, 8):
      print(matrix[i], end=' ')
  print()
  for i in range(8, 16):
      print(matrix[i], end=' ')
  print()
  for i in range(16, 24):
      print(matrix[i], end=' ')
  print()
  for i in range(24, 32):
      print(matrix[i], end=' ')
  print()
  for i in range(32, 40):
      print(matrix[i], end=' ')
  print()
  for i in range(40, 48):
      print(matrix[i], end=' ')
  print()
  for i in range(48, 56):
      print(matrix[i], end=' ')
  print()
  for i in range(56, 64):
      print(matrix[i], end=' ')
  print("\n---------------------------------")
  print("Sorted Matrix:")
  matrix.sort(reverse=True)
  for i in range(0, 8):
      print(matrix[i], end=' ')
  print()
  for i in range(8, 16):
      print(matrix[i], end=' ')
  print()
  for i in range(16, 24):
      print(matrix[i], end=' ')
  print()
  for i in range(24, 32):
      print(matrix[i], end=' ')
  print()
  for i in range(32, 40):
      print(matrix[i], end=' ')
  print()
  for i in range(40, 48):
      print(matrix[i], end=' ')
  print()
  for i in range(48, 56):
      print(matrix[i], end=' ')
  print()
  for i in range(56, 64):
      print(matrix[i], end=' ')

pause = str(input())
