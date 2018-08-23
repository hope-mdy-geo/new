import unittest
import uni2win

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        win = u'''pdwfwdkh&Sdjuí'''
        unicode = u'''စိတ်တို့ရှိကြ၍'''
        result = uni2win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article One")

    def test_article_three(self):
        win = u'''vlwdkif;ü touf½Sif&ef vGwfvyfrIcGihfESihf vkHûcHpdwfcscGihf ½Sdonf/'''
        unicode = u'''လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
        result = uni2win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Three")

if __name__ == "__main__":
    unittest.main()
