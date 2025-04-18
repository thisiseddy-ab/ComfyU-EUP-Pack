
#### My Services's #####
from EUP.services.image import ImageService

class GetImageSize:

    def __init__(self):
        self.imageService = ImageService()
        

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT",)
    RETURN_NAMES = ("width", "height", "count")
    FUNCTION = "execute"
    CATEGORY = "EUP - Ultimate Pack/image"

    def execute(self, image):
        return self.imageService.getImageSize(image)