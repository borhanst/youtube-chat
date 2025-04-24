from typing import List

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_google_genai import GoogleGenerativeAI
from youtube_transcript_api import NoTranscriptFound

from embedding import BaseEmbedding

load_dotenv()


def get_transcript_from_url(url: str, video_lng=["en"], translate_lng="en"):
    try:
        loader = YoutubeLoader.from_youtube_url(
            url, add_video_info=False, language=video_lng
        )
        return loader.load(), False
    except NoTranscriptFound:
        return "No Transcript Fount With Selected language", True


prompt = PromptTemplate(
    template="you are helpful assistance to replay use form youtube video transcript bellow attached user question relevant transcript and question \n\n{transcript} \n\n question: {question}",
    input_variables=["transcript", "question"],
)


def get_related_transcript(documents: List[Document]):
    return "\n\n".join([item.page_content for item in documents])


def get_llm_response(question):
    LLM_MODEL = GoogleGenerativeAI(model="gemini-2.0-flash")
    retriever = BaseEmbedding().retriever
    parallel_chain = RunnableParallel(
        {
            "transcript": retriever | RunnableLambda(get_related_transcript),
            "question": RunnablePassthrough(),
        }
    )
    chain = parallel_chain | prompt | LLM_MODEL | StrOutputParser()
    return chain.invoke(question)
