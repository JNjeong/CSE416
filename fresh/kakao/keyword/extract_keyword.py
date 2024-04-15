import pdb
import pandas as pd
import os
from pathlib import Path 
import spacy
import langid
from konlpy.tag import Okt

# path
kakao_path = Path(os.getcwd())
keyword_path = kakao_path / 'keyword'

# read csv
test_csv = pd.read_csv(keyword_path / 'cse416_report_test.csv')

# param
commend_col = test_csv['commend']
load_en = spacy.load("en_core_web_sm")
load_kor = Okt()
phrases_list = []
filter_list = ['어디에', '왜', '언제', '무엇을']
new_filter = []

for filter in filter_list:
  filtered = load_kor.nouns(filter)
  new_filter.extend(filtered)


# get commend col
for commend in commend_col:
    lang, _ = langid.classify(commend)  
    if lang == 'ko':
      nouns = load_kor.nouns(commend)
      for noun in nouns:
        if noun in new_filter:
          nouns.remove(noun)
      phrases_list.append(nouns)
    elif lang == 'en':
      sentence = load_en(commend)
      phrases = [chunk.text for chunk in sentence.noun_chunks]
      phrases_str = ", ".join(phrases)
      phrases_list.append(phrases_str)

test_csv['Phrases'] = phrases_list

output_path = keyword_path / 'cse416_report_test_updated.csv'
test_csv.to_csv(output_path, index=False)