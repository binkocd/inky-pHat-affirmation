from inky import InkyPHAT
import requests
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

print("Grabbing something good!\n")

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

header = ImageFont.truetype(FredokaOne, 22)
font = ImageFont.truetype(FredokaOne, 14)

# Top and bottom y-coordinates for the white strip

y_top = int(inky_display.HEIGHT * (5.0 / 10.0))
y_bottom = y_top + int(inky_display.HEIGHT * (4.0 / 10.0))

padding = 0

r = requests.get('https://www.affirmations.dev')
data = r.json()
message = data['affirmation']

# Better way:
# Find length of string (including spaces)
# Take first 21 characters (including spaces)
# Split by words that add up to 21 characters (including middle spaces)
# Cut trailing space off (character 21-22 should not be a space and carry over)
# with font size set to 22, that is the distance across for header.
# for message of the day, smaller size = more characters per line...


print("Printing Affirmation!\nPlease Hold!")


if len(message) < 28:

    affirmation_w, affirmation_h = header.getsize("Daily Affirmation:")
    affirmation_x = int((inky_display.WIDTH - affirmation_w) / 2)
    affirmation_y = 0 + padding
    draw.text((affirmation_x, affirmation_y), "Daily Affirmation:\n", inky_display.RED, header)

    name_w, name_h = font.getsize(message)
    name_x = int((inky_display.WIDTH - name_w) / 2)
    name_y = int(y_top + ((y_bottom - y_top - name_h) / 4))
    draw.text((name_x, name_y), message, inky_display.RED, font)
    
    inky_display.set_image(img)
    inky_display.show()


elif len(message) > 28 and len(message) < 56:
    
    message1 = message[0:28]
    message2 = message[28:]

    affirmation_w, affirmation_h = header.getsize("Daily Affirmation:")
    affirmation_x = int((inky_display.WIDTH - affirmation_w) / 2)
    affirmation_y = 0 + padding
    draw.text((affirmation_x, affirmation_y), "Daily Affirmation:", inky_display.RED, header)

    mynameis_w, mynameis_h = font.getsize(message1)
    mynameis_x = int((inky_display.WIDTH - mynameis_w) / 2)
    mynameis_y = affirmation_h + padding
    draw.text((mynameis_x, mynameis_y), message1, inky_display.RED, font)

    name_w, name_h = font.getsize(message2)
    name_x = int((inky_display.WIDTH - name_w) / 2)
    name_y = int(y_top + ((y_bottom - y_top - name_h) / 2))
    draw.text((name_x, name_y), message2, inky_display.RED, font)

    inky_display.set_image(img)
    inky_display.show()

else:
    
    message1 = message[0:28]
    message2 = message[28:46]
    message3 = message[46:]

    affirmation_w, affirmation_h = header.getsize("Daily Affirmation:")
    affirmation_x = int((inky_display.WIDTH - affirmation_w) / 2)
    affirmation_y = 0 + padding
    draw.text((affirmation_x, affirmation_y), "Daily Affirmation:", inky_display.RED, header)

    mynameis_w, mynameis_h = font.getsize(message1)
    mynameis_x = int((inky_display.WIDTH - mynameis_w) / 2)
    mynameis_y = affirmation_h + padding
    draw.text((mynameis_x, mynameis_y), message1, inky_display.RED, font)

    name_w, name_h = font.getsize(message2)
    name_x = int((inky_display.WIDTH - name_w) / 2)
    name_y = int(y_top + ((y_bottom - y_top - name_h) / 2))
    draw.text((name_x, name_y), message2, inky_display.RED, font)

    message3_w, message3_h = font.getsize(message3)
    message3_x = int((inky_display.WIDTH - message3_w) / 2)
    message3_y = int(y_top + (y_bottom - y_top - message3_h))
    draw.text((message3_x, message3_y), message3, inky_display.RED, font)

    inky_display.set_image(img)
    inky_display.show()