#!/usr/bin/python
from PIL import Image, ImageOps as ops, ImageDraw as draw, ImageFont as font
import argparse


parser = argparse.ArgumentParser(description="Creates inspirational images")

parser.add_argument('--image', dest='image', help='The path to an inspirational image')
parser.add_argument('--heading', dest='heading', default='Awesome', help='A word that inspires and sums up your image')
parser.add_argument('--heading-size', dest='heading_size', type=int, default=75, help='How many pixels tall is your motivational word')
parser.add_argument('--description', dest='description', default='Yeah, I totally am', help='Describe your motivations')
parser.add_argument('--description-size', dest='description_size', type=int, default=50, help='How many pixels tall is your motivational word')

args = parser.parse_args()

def motivate_image(image, heading, heading_size, description, description_size):
    border_size = 35
    text_padding = 15

    # Get the image from the args
    motivation = Image.open(image)
    bordered_image = ops.expand(motivation, border=border_size, fill=0)

    # Fun with fonts
    heading_font = font.truetype('Glegoo-Regular.ttf', heading_size)
    description_font = font.truetype('Glegoo-Regular.ttf', description_size)
    heading_size = heading_font.getsize(heading)
    description_size = description_font.getsize(description)

    # Create an image large enough to hold the text and the motivational image
    background_image_width = bordered_image.size[0] # size[0] is the width of an Image
    background_image_height = heading_size[1] + description_size[1] + \
            text_padding * 2 + bordered_image.size[1]
    background_image_size = (background_image_width, background_image_height)

    background_image = Image.new('RGB', background_image_size, 'black')

    # Center our text
    heading_left_buffer = (background_image_width / 2) - (heading_size[0] / 2)
    description_left_buffer = (background_image_width / 2) - (description_size[0] / 2)

    description_bottom_buffer = background_image_height - text_padding - description_size[1]
    heading_bottom_buffer = description_bottom_buffer - text_padding - heading_size[1]

    # Print the text on the image
    dr = draw.Draw(background_image)

    dr.text((heading_left_buffer, heading_bottom_buffer),
            heading,
            font=heading_font,
            fill='#FFFFFF')

    dr.text((description_left_buffer, description_bottom_buffer),
            description,
            font=description_font,
            fill='#FFFFFF')

    # Paste our original image onto the background with text
    background_image.paste(bordered_image, (0, 0))

    # Save or show your image
    background_image.show()

if __name__ == '__main__':
    motivate_image(args.image, args.heading, args.heading_size, args.description, args.description_size)
