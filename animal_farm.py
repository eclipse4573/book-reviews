import streamlit as st

st.set_page_config(
    page_title="Animal Farm", 
    page_icon="📚",
    layout="centered"
)

BOOK_TITLE = "Animal Farm"
BOOK_AUTHOR = "George Orwell"
BOOK_OPINION = """
ADD MY OPINION HERE LATER
"""

PDF_PATH = r"C:\Users\tanis\Downloads\School\Thesis Final Draft Grade 9.pdf"

st.title(f"📚 {BOOK_TITLE}")
st.subheader(f"by {BOOK_AUTHOR}")
st.markdown("---")

st.header("My Opinion")
st.write(BOOK_OPINION)

st.markdown("---")
st.header("Related Document")

with open(r'C:/Users/tanis/Downloads/School/AnimalFarmThesis.pdf', "rb") as pdf_file:
    file = pdf_file.read()

st.download_button(
    label="Download PDF",
    data=file,
    file_name="thesis_animal-farm.pdf",
    mime="application/pdf"
)

st.markdown("---")
# st.caption("Last updated: [Add your date here]")
