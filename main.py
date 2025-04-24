from typing import List, Literal
from urllib.parse import urlparse

import pandas as pd
import streamlit as st
from streamlit_player import st_player

from embedding import BaseEmbedding
from utils import get_llm_response, get_transcript_from_url


def get_video_language_code(df):
    select_code = df[df["name"].isin(st.session_state["v_lng"])]["code"]
    st.session_state["language_code"] = select_code.tolist()


def get_video_translate_code(df):
    select_code = df[df["name"] == st.session_state["t_lng"]]["code"]
    st.session_state["translate_code"] = select_code.tolist()[0]


def onchange_input():
    parse_url = urlparse(st.session_state["url_field"])
    st.session_state["video_id"] = parse_url.query.split("=")[1]


def main():
    df = pd.read_json("country.json")
    with st.sidebar:
        url = st.text_input(
            "Video URL",
            placeholder="type you video url",
            on_change=onchange_input,
            key="url_field",
        )
        video_id = st.text(st.session_state.get("video_id", "no id"))
        st.multiselect(
            "transcript language",
            df["name"],
            on_change=get_video_language_code,
            key="v_lng",
            args=(df,),
        )
        st.selectbox(
            "Translate language",
            df["name"],
            on_change=get_video_translate_code,
            key="t_lng",
            args=(df,),
        )
        if st.button("Submit"):
            with st.spinner("video loading...."):
                st_player(url)
            with st.spinner("text loading...."):

                transcript, error = get_transcript_from_url(
                    url,
                    video_lng=st.session_state.get("language_code", ["en"]),
                    translate_lng=st.session_state.get("translate_code", ["en"]),
                )
                if not error:
                    embedding = BaseEmbedding(transcript, video_id=video_id)
                    embedding.save_embedding()
            if error:
                st.error(transcript)
            else:
                st.write(transcript[0].page_content)

    messages: List[tuple[Literal["user", "ai"], str]] = []
    st.title("Chat with youtube video")

    message = st.chat_input("type message")
    if message:
        messages.append(("user", message))
        with st.chat_message("user"):
            st.write(message)
        with st.chat_message("ai"):
            st.spinner()
            ai_response = get_llm_response(message)
            if ai_response:
                messages.append(("ai", ai_response))
                st.write(ai_response)


if __name__ == "__main__":
    main()
