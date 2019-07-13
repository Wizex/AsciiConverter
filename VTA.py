import math


def convert_image_to_ascii(img, compress_var=0, det=0):

    img_in_ascii = []

    compress_img = []

    x = 0

    main_img = compress_img if compress_var != 0 else img

    main_width = int(img.shape[0] / compress_var) if compress_var != 0 else img.shape[0]
    main_height = int(img.shape[1] / compress_var) if compress_var != 0 else img.shape[1]

    if compress_var != 0:

        for i in range(0, img.shape[0]):

            if i % compress_var == 0:

                compress_img.append([])

                for e in range(0, img.shape[1]):

                    if e % compress_var == 0:

                        compress_img[x].append(img[i][e])

                x += 1

    x = 0

    if det != 0:

        arr = [chr(i) for i in range(34, 48)]

        save_pixels = dict()

        counter = 0

        save_pixels[0] = {arr[counter]: [main_img[0][0][0], main_img[0][0][1], main_img[0][0][2]]}

        for i in range(0, main_width):

            img_in_ascii.append([])

            for e in range(0, main_height):

                counter_second = 0
                pos = 0

                for z in range(0, len(save_pixels)):

                    for q in range(0, 3):

                        number = int(math.fabs(int(main_img[i][e][q]) - int(save_pixels[z][arr[z]][q])))

                        if number > det:
                            counter_second += 1

                            break

                        pos = z

                if counter_second == len(save_pixels):

                    counter += 1

                    if counter < len(arr):

                        save_pixels[len(save_pixels)] = {
                            arr[counter]: [main_img[i][e][0], main_img[i][e][1], main_img[i][e][2]]}

                        img_in_ascii[x].append(arr[counter])

                    elif counter >= len(arr):

                        is_found = True

                        det_second = 10

                        while is_found:

                            for u in range(0, len(save_pixels)):

                                for g in range(0, 3):

                                    second_number = int(
                                        math.fabs(int(main_img[i][e][g]) - int(save_pixels[u][arr[u]][g])))

                                    if second_number < det_second:
                                        img_in_ascii[x].append(arr[u])

                                        is_found = False

                            det_second += 20

                elif counter_second != len(save_pixels):

                    img_in_ascii[x].append(arr[pos])

            x += 1

    elif det == 0:

        for i in range(0, main_width):

            img_in_ascii.append([])

            for e in range(0, main_height):

                number = ((int(main_img[i][e][0]) + int(main_img[i][e][1]) + int(main_img[i][e][2])) / int(12)) + 33

                img_in_ascii[x].append(chr(int(number)))

            x += 1

    file = open("converted_pict.txt", "w")

    for i in range(0, main_width):

        for e in range(0, main_height):

            file.write(img_in_ascii[i][e])

        file.write('\n')

    pass

