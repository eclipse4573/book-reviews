import streamlit as st
import base64

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

st.title(f"📚 {BOOK_TITLE}")
st.subheader(f"by {BOOK_AUTHOR}")
st.markdown("---")

st.header("My Opinion")
st.write(BOOK_OPINION)

st.markdown("---")
st.header("Related Document")

with open('AnimalFarmThesis.pdf', "rb") as pdf_file:
    file = pdf_file.read()

st.download_button(
    label="Download PDF",
    data=file,
    file_name="thesis_animal-farm.pdf",
    mime="application/pdf"
)

def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.markdown("---")
# st.caption("Last updated: [Add your date here]")
