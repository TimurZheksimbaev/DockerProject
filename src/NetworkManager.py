from threading import Thread
from functools import lru_cache
import httpx
"""
    Custom class for making api calls
"""
class ImageLoader:
    def __init__(self):
        self.baseUrl = "https://random.dog/woof.json"

    @lru_cache(maxsize=256)
    def get_random_image_url(self):
        try:
            response = httpx.get(self.baseUrl)
            image_url = response.json()['url']
            return image_url
        except:
            print("Could not fetch data")
            exit(0)

    def multithreaded_api_call(self):

        def thread_target():
            results.append(self.get_random_image_url())


        num_threads = 20
        threads = []
        results = []
        for i in range(num_threads):
            thread = Thread(target=thread_target)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return results
