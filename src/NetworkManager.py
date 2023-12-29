from threading import Thread
from functools import lru_cache
import httpx
"""
    Custom class for making api calls
"""
class ImageLoader:
    def __init__(self):
        self.baseUrl = "https://random.dog/woof.json"
        self.num_of_images = 20

    @lru_cache(maxsize=256)
    def get_random_image_url(self):
        try:
            response = httpx.get(self.baseUrl)
            image_url = response.json()['url']
            return image_url
        except:
            print("Could not fetch data")
            exit(0)

    def multithreaded_get_random_dogs(self):

        results = []
        def thread_target():
            results.append(self.get_random_image_url())

        threads = []
        for i in range(self.num_of_images):
            thread = Thread(target=thread_target)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return results

