import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def load_prompt():
    input_prompt = """
                   You are a financial advisor with an expertise in understanding invoices.
                   You will receive input images as invoices &
                   you will have to answer questions based on the input image
                   If you don't know the answer, please refrain from speculating.
                   """
    return input_prompt

def generate_response_llm(input_question, prompt, image):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content([input_question, prompt, image])
    return response.text