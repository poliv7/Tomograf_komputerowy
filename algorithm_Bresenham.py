def bresenham_for_sinogram(x1, y1, x2, y2, input_image, visited):
    # zmienne pomocnicze
    (d, dx, dy, ai, bi, xi, yi, x, y) = (0, 0, 0, 0, 0, 0, 0, x1, y1)
    suma = 0

    # ustalenie kierunku rysowania (poziomo)
    if x1 < x2:
        xi = 1
        dx = x2 - x1
    else:
        xi = -1
        dx = x1 - x2

    # ustalenie kierunku rysowania (pionowo)
    if y1 < y2:
        yi = 1
        dy = y2 - y1
    else:
        yi = -1
        dy = y1 - y2

    # zaznaczenie pierwszego piksela
    suma += input_image[x][y]
    visited[x][y] += 1

    # oś wiodąca OX
    if dx > dy:
        ai = (dy - dx) * 2
        bi = dy * 2
        d = bi - dx

        # pętla po kolejnych x
        while x != x2:

            # test współczynnika
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                x += xi

            suma += input_image[x][y]
            visited[x][y] += 1

    # oś wiodąca OY
    else:
        ai = (dx - dy) * 2
        bi = dx * 2
        d = bi - dy

        # pętla po kolejnych y
        while y != y2:

            # test współczynnika
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                y += yi

            suma += input_image[x][y]
            visited[x][y] += 1

    return suma



def bresenham_for_output_image(x1, y1, x2, y2, sinogram_value, output_image):
    # zmienne pomocnicze
    (d, dx, dy, ai, bi, xi, yi, x, y) = (0, 0, 0, 0, 0, 0, 0, x1, y1)
    suma = 0

    # ustalenie kierunku rysowania (poziomo)
    if x1 < x2:
        xi = 1
        dx = x2 - x1
    else:
        xi = -1
        dx = x1 - x2

    # ustalenie kierunku rysowania (pionowo)
    if y1 < y2:
        yi = 1
        dy = y2 - y1
    else:
        yi = -1
        dy = y1 - y2

    # zaznaczenie pierwszego piksela
    output_image[x][y] += sinogram_value

    # oś wiodąca OX
    if dx > dy:
        ai = (dy - dx) * 2
        bi = dy * 2
        d = bi - dx

        # pętla po kolejnych x
        while x != x2:

            # test współczynnika
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                x += xi

            output_image[x][y] += sinogram_value

    # oś wiodąca OY
    else:
        ai = (dx - dy) * 2
        bi = dx * 2
        d = bi - dy

        # pętla po kolejnych y
        while y != y2:

            # test współczynnika
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                y += yi

            output_image[x][y] += sinogram_value
