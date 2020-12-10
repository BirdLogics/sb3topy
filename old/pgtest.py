import pygame as pg
import time
import timeit


def main():
    pg.init()
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)

    color = pg.Color(255, 0, 0)
    color2 = pg.Color(0, 255, 0)

    # def change_effect(img, value):  # Not looping through entire image only a diagonal line
    #     array = pg.PixelArray(img)
    #     for x, y in zip(range(array.shape[0]), range(array.shape[1])):
    #         array[x, y] += 1
    #     return array.make_surface()

    #image = pg.image.load("./assets/Mural.png")
    #change_effect(image.convert_alpha(), 20)
    # print("Hue1:", timeit.timeit(lambda: change_hue(image, 20), number=count))
    # for _ in range(2):
    #     print("Hue1:", timeit.timeit(lambda: change_hue(image, 20), number=count))
    #     print("Hue2:", timeit.timeit(lambda: change_hue2(image, 20), number=count))
    # print("Brightnesss:", timeit.timeit(lambda: change_brighten(image, 20), number=count))
    # print("Darkness:", timeit.timeit(lambda: change_darken(image, 20), number=count))
    # print("Ghost:", timeit.timeit(lambda: change_ghost(image, 20), number=count))
    #print("RotoZoom:", timeit.timeit(lambda: pg.transform.rotozoom(image, 45, 1.5), number=1000))
    # print(timeit.timeit(lambda: change_effect(image, 20), number=1))

    # image = change_hue(image, 40)
    # image = change_darken(image, 50)
    image = pg.image.load(
        "./assets/106798711d0220a08cca12e750468e2b.png").convert_alpha()
    #image = pg.image.load("./assets/Mural.png").convert_alpha()

    count = 1000
    #image = pg.transform.rotozoom(image, 0, 8)
    # print("A:", timeit.timeit(lambda: rotozoom(image, 45, 4), number=count))
    # #image = pg.transform.scale2x(image)
    # print("B:", timeit.timeit(lambda: rotozoom2(image, 45, 4), number=count))
    # print("C:", timeit.timeit(lambda: pg.transform.rotozoom(image, 45, 4), number=count))
    #print("D:", timeit.timeit(lambda: rotozoom2(image, 45, 0.5), number=count))
    print(pg.transform.get_smoothscale_backend())

    # image1 = pg.transform.rotozoom(image, 45, 2)
    # image2 = rotozoom2(image, 45, 2)

    image1 = change_hue(image, 40)
    while True:
        pg.event.pump()

        if round(time.monotonic() % 2):
            screen.fill(color)
            screen.blit(image1, (0, 0))
        else:
            screen.fill(color2)
            screen.blit(image, (0, 0))

        # hsva = color.hsva
        # color.hsva = (hsva[0] + 1, hsva[1], hsva[2], 100)

        pg.display.flip()
        time.sleep(0.05)

    pg.quit()


def rotozoom(image, angle, zoom):
    return pg.transform.rotate(pg.transform.scale(image, (int(image.get_width() * zoom), int(image.get_height() * zoom))), angle)


def rotozoom2(image, angle, zoom):
    return pg.transform.rotate(pg.transform.smoothscale(image, (int(image.get_width() * zoom), int(image.get_height() * zoom))), angle)


def rotozoom3(image, angle, zoom):
    return pg.transform.rotate(pg.transform.scale2x(image), angle)


def change_hue(image, value):
    """Changes the hue of an image"""
    # Gets a copy of the alpha channel
    transparency = image.convert_alpha()
    transparency.fill((255, 255, 255, 0), special_flags=pg.BLEND_RGBA_MAX)

    # Get an 8-bit surface with a color palette
    image = image.convert(8)

    # Change the hue of the palette
    for index in range(256):
        # Get the palette color at index
        color = pg.Color(*image.get_palette_at(index))

        # Get the new hue
        hue = color.hsva[0] + value
        if hue > 360:
            hue -= 360

        # Update the hue
        color.hsva = (hue, *color.hsva[1:3])
        image.set_palette_at(index, color)

    # Return the image transparency
    image.set_alpha()
    image = image.convert_alpha()
    image.blit(transparency, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    return image


def change_brighten(image, value):
    """Changes the brightness of an image"""
    image = image.convert_alpha()
    image.fill((value, value, value), special_flags=pg.BLEND_RGB_ADD)
    return image


def change_darken(image, value):
    """Changes the brightness of an image"""
    image = image.convert_alpha()
    image.fill((value, value, value), special_flags=pg.BLEND_RGB_SUB)
    return image


def change_ghost(image, value):
    """Changes the ghost of an image"""
    image = image.convert_alpha()
    image.fill((255, 255, 255, value), special_flags=pg.BLEND_RGBA_MULT)
    return image


if __name__ == '__main__':
    main()
