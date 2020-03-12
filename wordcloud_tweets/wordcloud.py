import datetime
import os
from wordcloud import WordCloud

from .config import DAYS
from .tweettext import tweet_text
from .freq import wl
from .logger import logger

def run():
    logger.info("Start creating wordcloud...")
    draw_from_frequency(wl, DAYS)
    logger.info("Waiting for the next day...")

def draw_from_frequency(wl, days):
    sorted_word_list = dict(sorted(wl.items(), key=lambda x: x[1], reverse=True))

    wc = WordCloud(
        font_path="data/Alibaba-PuHuiTi-Regular.ttf",
        background_color="white",
        max_words=200,
        max_font_size=200,
        random_state=42,
        width=1200, height=800, margin=2,
    )

    wc.generate_from_frequencies(sorted_word_list)
    if not os.path.exists('images'):
        os.mkdir('images')
    image_path = "images/wordcloud-" + datetime.date.today().strftime("%Y-%m-%d") + "-" + str(days) + "days.png"
    wc.to_file(image_path)