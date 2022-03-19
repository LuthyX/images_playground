from PIL import Image, ImageFilter
# img = Image.open('./pokedex/pikachu.jpg')


# filtered_img= img.convert('L')
# crooked = filtered_img.rotate(180)
# box= (100, 100, 400, 400)
# region = filtered_img.crop(box)
# resize= filtered_img.resize((300,300))
# region.save("grey.png", 'png')
# region.show() 

img2=Image.open('./astro.jpg')
img2.thumbnail((400,400))
img2.save('thumbnail.jpg')
img2.show()