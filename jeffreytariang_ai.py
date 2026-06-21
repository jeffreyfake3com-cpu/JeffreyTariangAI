from PIL import Image, ImageEnhance

print("JeffreyTariang AI Photo Enhancer")

photo = input("Enter image name: ")

img = Image.open(photo)

sharp = ImageEnhance.Sharpness(img)
img = sharp.enhance(2.0)

contrast = ImageEnhance.Contrast(img)
img = contrast.enhance(1.2)

img.save("JeffreyTariang_Enhanced.jpg")

print("Photo enhanced successfully!")
