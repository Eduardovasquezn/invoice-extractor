import streamlit as st
from PIL import Image

from utils import load_prompt, generate_response_llm


def main():
    st.set_page_config("Invoice Extractor🚀")

    st.title("Invoice Extractor🚀🕵️")

    user_question = st.text_input("Input prompt", key = "input")

    st.sidebar.title("Invoice Image")

    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded image", use_column_width=True)

    prompt = load_prompt()

    if st.button("Send"):
        with st.spinner("Start processing..."):
            response = generate_response_llm(input_question= user_question, image = image, prompt = prompt)
            st.subheader("Response:")
            st.write(response)

if __name__ == "__main__":
    main()