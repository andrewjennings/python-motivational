#!/usr/bin/python
from PIL import Image, ImageOps, ImageDraw, ImageFont
import argparse


parser = argparse.ArgumentParser(description="Creates inspirational images")

parser.add_argument('--image', '-i', dest='image', help='The path to an inspirational image', required=True)
parser.add_argument('--motivation', '-m', dest='motivation', default='Awesome', help='A word that inspires and sums up your image')
parser.add_argument('--motivation-size', '-ms', dest='motivation_size', type=int, default=50, help='How many pixels tall is your motivational word')
parser.add_argument('--description', '-d', dest='description', default='Yeah, I totally am', help='Describe your motivations')
parser.add_argument('--description-size', '-ds', dest='description_size', type=int, default=30, help='How many pixels tall is your description')
parser.add_argument('--output', '-o', dest='output', help='Where to save your motivational image')

args = parser.parse_args()

def motivate_image(image, motivation, motivation_size, description, description_size, output):
    border_size = 35
    text_padding = 15

    # Get the image from the args
    motivational_image = Image.open(image)
    bordered_image = ImageOps.expand(motivational_image, border=border_size, fill=0)

    # Fun with fonts
    motivation_font = ImageFont.truetype('Glegoo-Regular.ttf', motivation_size)
    description_font = ImageFont.truetype('Glegoo-Regular.ttf', description_size)
    motivation_size = motivation_font.getsize(motivation)
    description_size = description_font.getsize(description)

    # Create an image large enough to hold the text and the motivational image
    background_image_width = bordered_image.size[0] # size[0] is the width of an Image
    background_image_height = motivation_size[1] + description_size[1] + \
            text_padding * 2 + bordered_image.size[1]
    background_image_size = (background_image_width, background_image_height)

    background_image = Image.new('RGB', background_image_size, 'black')

    # Figure out where to center our text
    motivation_left_buffer = (background_image_width / 2) - (motivation_size[0] / 2)
    description_left_buffer = (background_image_width / 2) - (description_size[0] / 2)

    description_bottom_buffer = background_image_height - text_padding - description_size[1]
    motivation_bottom_buffer = description_bottom_buffer - text_padding - motivation_size[1]

    # Print the text on the image
    dr = ImageDraw.Draw(background_image)

    dr.text((motivation_left_buffer, motivation_bottom_buffer),
            motivation,
            font=motivation_font,
            fill='#FFFFFF')

    dr.text((description_left_buffer, description_bottom_buffer),
            description,
            font=description_font,
            fill='#FFFFFF')

    # Paste our original image onto the background with text
    background_image.paste(bordered_image, (0, 0))

    # Save or show your image
    if output:
        try:
            background_image.save(output)
        except:
            print("Sorry, couldn't save your image. Check to make sure the output path is accessible")
            background_image.show()
    else:
        background_image.show()

if __name__ == '__main__':
    motivate_image(args.image, args.motivation, args.motivation_size, args.description, args.description_size, args.output)
