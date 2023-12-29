from src.NetworkManager import ImageLoader
import unittest
from enum import Enum

class Messages(Enum):
    NO_URL = "Didn't receive URL"
    INVALID_NUMBER_OF_IMAGES = "Number of received URLs should be 20"


class DogAPITester(unittest.TestCase):
    loader = ImageLoader()

    def test_get_random_dogs(self):
        url = self.loader.get_random_image_url()
        self.assertGreater(len(url), 0, Messages.NO_URL.value)

    def test_multithreaded_get_random_dogs(self):
        images_num = self.loader.num_of_images
        results = self.loader.multithreaded_get_random_dogs()
        self.assertGreater(len(results), 0, Messages.NO_URL.value)
        self.assertEqual(len(results), images_num, Messages.INVALID_NUMBER_OF_IMAGES.value)


if __name__ == "__main__":
    unittest.main()

