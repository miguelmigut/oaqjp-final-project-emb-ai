from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("I'm glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = emotion_detector("I'm really angry about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = emotion_detector("I'm disgusted just hearing about it")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = emotion_detector("I'm so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = emotion_detector("I'm really afraid this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()