import numpy as np
import cv2
from PIL import Image, ImageOps
from glitch_this import ImageGlitcher


def vignette(image, saveas, opacity):
    input_image = cv2.imread(image)
    rows, cols = input_image.shape[:2]
    X_resultant_kernel = cv2.getGaussianKernel(cols, 310)
    Y_resultant_kernel = cv2.getGaussianKernel(rows, 160)
    resultant_kernel = Y_resultant_kernel * X_resultant_kernel.T
    mask = 400 * resultant_kernel / np.linalg.norm(resultant_kernel)
    output = np.copy(input_image)
    for i in range(3):
        output[:, :, i] = output[:, :, i] * mask
    cv2.imwrite(saveas, output)


def posterize_effect(filename, saveas):
    im1 = Image.open(filename)
    im2 = ImageOps.posterize(im1, 2)
    im2.save(saveas)


def pencil_sketch_effect(filename, saveas):
    img = cv2.imread(filename)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_IMG = cv2.divide(
        gray_image, inverted_blurred_img, scale=256.0)
    cv2.imwrite(saveas, pencil_sketch_IMG)


def negative_effect(filename, saveas):
    img = cv2.imread(filename)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    cv2.imwrite(saveas, inverted_gray_image)


def rainffects(image, blurtype, bluropacity, saveas):
    road = cv2.imread(image)
    raineffected = cv2.imread("images/raineffect.png")
    pascal = (road.shape[1], road.shape[0])
    raineffected_rush = cv2.resize(raineffected, pascal)
    hola = cv2.add(raineffected_rush, road)
    kernel_size = bluropacity  # bluropacity
    kernel_v = np.zeros((kernel_size, kernel_size))
    kernel_h = np.copy(kernel_v)
    kernel_v[:, int((kernel_size - 1)/2)] = np.ones(kernel_size)
    kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size)
    kernel_v /= kernel_size
    kernel_h /= kernel_size
    if blurtype == "horizontal":
        horizonal_mb = cv2.filter2D(hola, -10, kernel_h)
        cv2.imwrite(saveas, horizonal_mb)
    elif blurtype == "vertical":
        prefix = cv2.filter2D(hola, -10, kernel_v)
        cv2.imwrite(saveas, prefix)


def textureadd(image, texture, src_weight, src2_weight, saveas):
    road = cv2.imread(image)
    raineffected = cv2.imread(texture)
    pascal = (road.shape[1], road.shape[0])
    raineffected_rush = cv2.resize(raineffected, pascal)
    blend = cv2.addWeighted(
        road, src_weight, raineffected_rush, src2_weight, 0)
    cv2.imwrite(saveas, blend)


img = Image.open(r'png_to_gif.gif')
glitcher = ImageGlitcher()
glitch_img, src_gif_duration, src_gif_frames = glitcher.glitch_gif(
    img, 4, color_offset=True)

DURATION = 200      # Set this to however many centiseconds each frame should be visible for
LOOP = 0            # Set this to how many times the gif should loop
# LOOP = 0 means infinite loop

# You could also use the `src_gif_duration` returned by `glitch_gif`
# To keep the GIF exactly the same duration wise

glitch_img[0].save(r'glitcharts.gif',
                   format='GIF',
                   append_images=glitch_img[1:],
                   save_all=True,
                   duration=DURATION,
                   loop=LOOP)


# """
# rainffects("keerthy.jpg","vertical",10,"effects/hvarticalrain.jpg")
# rainffects("keerthy.jpg","horizontal",7,"effects/horizontal.jpg")
# vignette("keerthy.jpg","effects/kindahell.jpg",0)
# negative_effect("keerthy.jpg","effects/neg.png")
# pencil_sketch_effect("keerthy.jpg","effects/pen.png")
# posterize_effect("keerthy.jpg","effects/postered3.jpg")

# """

rainffects("images/baby-with-teddy.jpg", "horizontal", 10, "output.jpg")
