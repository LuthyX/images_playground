from PIL import Image, ImageFilter
img = Image.open('./pokedex/pikachu.jpg')


filtered_img= img.convert('L')
crooked = filtered_img.rotate(180)
box= (100, 100, 400, 400)
region = filtered_img.crop(box)
resize= filtered_img.resize((300,300))
region.save("grey.png", 'png')
region.show() 