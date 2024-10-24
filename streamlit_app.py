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

# スライダーを作成し、値を選択
birth_date = st.date_input('生年月日を入力してください')

# 補足メッセージ
st.caption("十字キー（左右）でも調整できます。")


binary_representation=['鳥','魚','人間','猫']
# 選択した数値を2進数に変換 # 'bin'関数で2進数に変換し、先頭の'0b'を取り除く
st.info(f'🔢 あなたは来世「{binary_representation}」になります。 🔢')  # 2進数の表示をハイラ