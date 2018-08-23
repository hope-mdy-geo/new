import unittest
import uni2win

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        win = u'''vlwdkif;onf wlnD vGwfvyfaom *kPfodu©mjzihf vnf;aumif;? wlnDvGwfvyfaom tcGihfta&;rsm;jzihf vnf;aumif;? arG;zGm;vmolrsm; jzpfonf/ 
        xdkolwdkYü ydkif;jcm; a0zefwwfaom ÓPfESihf usihf0wf odwwfaom pdwfwdkY½SdMuí xdkolwdkYonf tcsif;csif; arwÅmxm;í qufqHusihfokH;oihf\/'''
        unicode = u'''လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။ 
        ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။'''
        result = uni2win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article One")

    def test_article_three(self):
        win = u'''vlwdkif;ü touf½Sif&ef vGwfvyfrIcGihfESihf vkHûcHpdwfcscGihf ½Sdonf/'''
        unicode = u'''လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
        result = uni2win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article Three")

if __name__ == "__main__":
    unittest.main()
