

class ImageService():
    
    def getImageSize(image):
        """
        Get the size of an image.
        """
        # width, height, count
        return (image.shape[2], image.shape[1], image.shape[0])