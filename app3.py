pip install streamlit nltk pandas sklearn
import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def analyze_text(text):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    return ss

st.title("文本分析アプリ")
text = st.text_area("入力してください")
if st.button("分析"):
    result = analyze_text(text)
    st.success(result)
