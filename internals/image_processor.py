from PIL import Image, ImageDraw, ImageFont
from internals.models import EventConfig


ROW_1_Y_COLUMN = 454
ROW_2_Y_COLUMN = 824
ROW_3_Y_COLUMN = 1195
ROW_4_Y_COLUMN = 1566

PLACEMENT_1 = 130
PLACEMENT_2 = 750

FIGHTER_IMAGE_HEIGHT = 250
FIGHTER_IMAGE_WIDTH = 250
FIGHTER_SIZE_TUPLE = ((FIGHTER_IMAGE_WIDTH, FIGHTER_IMAGE_HEIGHT))

def _calculate_x_center(parent_image_width, child_image_width):
    return (parent_image_width-child_image_width)//2

# def _calculate_flag_position(photo_size, flag_size) -> tuple:
    # will_do_later()

     
     
class ImageProcessorClient:
    def __init__(self):
        font_path = "assets/fonts/Anton-Regular.ttf"
        self.poster_font = ImageFont.truetype(font_path, size = 80)

    def _paste_image(self, base_image : Image.Image, image_to_paste : Image.Image, position : tuple = 0.0):
        base_image.paste(image_to_paste, position, mask=image_to_paste)

    def _draw_text(self, base_image: Image.Image, text_to_paste : str, position : tuple = 0.0):
        drawable_image = ImageDraw.Draw(base_image)
        drawable_image.text(position, text_to_paste, font=self.poster_font, fill="white")

    def _create_fighter_unit(self, fighter_picture : Image.Image, fighter_name : str, fighter_flag : Image.Image):
            fighter_image_copy = fighter_picture.copy()
            canvas = Image.new("RGBA", FIGHTER_SIZE_TUPLE)
            drawing_context = ImageDraw.Draw(canvas)
            fighter_image_copy.thumbnail((FIGHTER_IMAGE_WIDTH, FIGHTER_IMAGE_HEIGHT))
            self._paste_image(canvas,fighter_image_copy, (_calculate_x_center(), ))
            self._draw_text(canvas, fighter_name, position)
            return canvas
    







        


        


        


    



