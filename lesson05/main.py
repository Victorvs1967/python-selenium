import time
from PIL import Image


def create_image(image_path):
  image_pixel_list = []
  img = Image.open(image_path)
  pixels = img.load()
  
  for w in range(1920):
    vertical_line = []
    
    for h in range(1080):
      vertical_line.append(pixels[w, h])
      
    image_pixel_list.insert(0, vertical_line)
    
  for w in range(1920):
    for h in range(1080):
      pixels[w, h] = image_pixel_list[w][h]
  
  img.save(f'lesson05/result/{int(time.time())}.jpeg')

def main():
  create_image('lesson05/cat.jpg')

if __name__ == '__main__':
  main()