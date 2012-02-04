#!/usr/bin/python
from PIL import Image, ImageOps as ops, ImageDraw as draw, ImageFont as font
import argparse


parser = argparse.ArgumentParser(description="Creates inspirational images")

parser.add_argument('--image', dest='image', help='The path to an inspirational image')
parser.add_argument('--heading', dest='heading', default='Awesome', help='A word that inspires and sums up your image')
parser.add_argument('--heading-size', dest='heading_size', type=int, default=125, help='How many pixels tall is your motivational word')
parser.add_argument('--description', dest='description', default='Yeah, I totally am', help='Describe your motivations')

args = parser.parse_args()

def motivate_image(image, heading, heading_size, description):
    # Get the image from the args
    im = Image.open(image)

    # Add a border around the image
    border_size = 380
    bim = ops.expand(im, border=border_size, fill=0)

    # TODO: Create an image of equal width to the image, black background, height of 400 px
    # TODO: Paste the text background image to the bottom of the image
    # TODO: Create a large (400px or more) font object with an offset of at least 200

    # Fun with fonts
    description_size = 75

    heading_font = font.truetype('Glegoo-Regular.ttf', heading_size)
    description_font = font.truetype('Glegoo-Regular.ttf', description_size)
    heading_size = heading_font.getsize(heading)
    description_size = description_font.getsize(description)

    # Figure out where the text goes
    heading_left_buffer = (bim.size[0] / 2) - heading_size[0] / 2
    description_left_buffer = (bim.size[0] / 2) - description_size[0] / 2

    description_bottom_buffer = (bim.size[1] - 20 - description_size[1])
    heading_bottom_buffer = description_bottom_buffer - 20 - heading_size[1]

    # Print the text on the image
    dr = draw.Draw(bim)
    dr.text((heading_left_buffer, heading_bottom_buffer), heading, font=heading_font, fill='#FFFFFF')
    dr.text((description_left_buffer, description_bottom_buffer), description, font=description_font, fill='#FFFFFF')

    # Save or show your image
    bim.show()

if __name__ == '__main__':
    motivate_image(args.image, args.heading, args.heading_size, args.description)
