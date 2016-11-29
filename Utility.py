import random, string
import logging, warnings, re

class Utility:
    def __init__(self, driver):
        self.driver = driver

    def verify_text(self, originalvalue, value, message):
        try:
            assert (originalvalue == value), message
        except Exception:
            print (message)
            warnings.warn(message)

    def create_random_string(self, size=6, chars = string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))
    
