import re

import jieba
from .tweettext import tweet_text
from .config import USER_DICT, STOPWORD

class WordCount():

    def __init__(self, tweet_text, user_dict, stopword):
        self.tweet_text = tweet_text
        self.user_dict = user_dict
        self.stopword = stopword
        
        output = ' '.join(self.tweet_text)
        jieba.enable_paddle()
        jieba.re_han_default = re.compile(r"([\u4E00-\u9FD5a-zA-Z0-9+#&\._% ]+)", re.U)
        jieba.load_userdict(self.user_dict)

        text = self._remove_urls(output)
        text = self._remove_at(text)
        for hashtag in self._get_hashtags(text):
            jieba.add_word(hashtag)

        segs = "/".join(jieba.cut(text))
        self._wordlist = self._strip_word(segs)
    
    def get_wordlist(self):
        return self._wordlist
        
    def _remove_urls(self, text):
        return re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)

    def _remove_at(self, text):
        return re.sub(r'@[0-9a-zA-Z_]+\b', '', text, flags=re.MULTILINE)

    def _get_hashtags(self, text):
        return(re.findall(r'#[0-9a-zA-Z_]+\b', text))

    def _strip_word(self, segs):
        wordlist = {}
        with open(self.stopword, "r", encoding="utf-8") as stpwd:
            stopword = {}.fromkeys(stpwd.read().split('\n'))
                    
        for seg in segs.split('/'):
            word = seg.strip()
            if not word.isupper():
                word = word.lower()
            if word not in stopword and len(word)>1 and not word.isdigit():
                if word not in wordlist:
                    wordlist[word] = 1
                else:
                    wordlist[word]+=1
        return wordlist

wl = WordCount(tweet_text, USER_DICT, STOPWORD).get_wordlist()
