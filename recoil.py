from time import sleep

import mouse

import win32api

orig_x = 960
orig_y = 540
recoil = [
    (960, 540),
    (924, 574),
    (931, 620),
    (876, 659),
    (839, 728),
    (848, 753),
    (919, 782),
    (948, 803),
    (1021, 816),
    (1053, 842),
    (1071, 870),
    (1069, 896),
]

count = 0
while True:
    x, y = win32api.GetCursorPos()
    # print(x, y)
    if win32api.GetAsyncKeyState(0xA2):
        print('On')
        count = 0
        while mouse.is_pressed(button='left'):
            print(recoil[count][0], recoil[count][1])
            if count < len(recoil):
                win32api.SetCursorPos((recoil[count][0], recoil[count][1]))
                count = count + 1
            else:
                count = 0
            sleep(0.1)
    sleep(0.1)
