from unittest import TestCase
from com.juliofss.media import Media


class TestMedia(TestCase):
    def setUp(self):
        self.media = Media()

    def test_media(self):
        self.assertEqual(self.media.media_ar([8,5,2]), 5, "Should be 5")