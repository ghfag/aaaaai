# Streamlitライブラリをインポート
import streamlit as st
import random


# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('Streamlitのサンプルアプリ')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.text_input('あなたの名前を入力してください')

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 こんにちは、{user_input}さん! 🌟')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示
st.caption("十字キー（左右）でも調整できます。")

birth_date = st.date_input("生年月日を選択してください")
futures =['鳥','魚','人間','猫']
future=random.choice(futures)
st.write("あなたの来世は" + future + "です")