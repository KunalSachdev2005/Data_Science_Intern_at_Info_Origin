import spacy
from spacy import displacy
from bs4 import BeautifulSoup
import streamlit as st
import json

# Loading trained model
nlp_ner = spacy.load("./model-best")

# reading css style
with open('./style.css') as readfile:
    css = readfile.read()

# Custom CSS to change the background color and add tabs styling
st.markdown(
    f"""
    <style>
    {css}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app

# Navigation tabs
tabs = ["Optimize Resume", "Analyzed Job Description"]
selected_tab = st.selectbox("Select Tab", tabs, index=1)

# Analyzed Job Description Tab
if selected_tab == "Analyzed Job Description":
    st.markdown('<p class="stTitle">Job Description NER Annotator</p>', unsafe_allow_html=True)
    st.markdown('<p><span style="color: black;">Paste a job description below and click "Submit" to see the annotations.</span></p>', unsafe_allow_html=True)

    # Text area for user input
    job_description = st.text_area("Job Description", height=300)

    if st.button("Submit"):
        if job_description:

            # Process the job description with the NER model
            doc = nlp_ner(job_description)

            ents_dict = {'YEARS_OF_EXPERIENCE': [],
                         'EDUCATION': [],
                         'ROLE': [],
                         'TOOLS_TECH': [],
                         'CERTIFICATIONS': [],
                         'LOC': [],
                         'CONCEPTS': [],
                         'SOFT_SKILLS': [],
                         'DOMAIN': []
                         }
            
            for ent in doc.ents:
                ents_dict[ent.label_].append(ent.text)

            # Saving identified entities for later comparison with resumes
            with open('./jd_entities.json', 'w') as json_file:
                json.dump(ents_dict, json_file, indent = 4)
            
            
            # Define the colors for the labels
            colors = {'YEARS_OF_EXPERIENCE': "red",
                      'EDUCATION': "blue",
                      'ROLE': "green",
                      'TOOLS_TECH': "#FFC300",
                      'CERTIFICATIONS': "orange",
                      'LOC': "purple",
                      'CONCEPTS': "brown",
                      'SOFT_SKILLS': "pink",
                      'DOMAIN': "violet"}
            options = {"colors": colors}

            # Render the annotated text
            html = displacy.render(doc, style="ent", options=options, jupyter=False)

            # Modify the HTML to remove the entity names and change the font color
            soup = BeautifulSoup(html, 'html.parser')

            for entity in soup.find_all('mark'):
                entity_text = entity.text
                entity_color = entity.get('style').split(';')[0].split(':')[1].strip()
                entity_span_tags = entity.find_all('span')
                for span_tag in entity_span_tags:
                    span_tag.decompose()
                entity['style'] = f"text-decoration: none; color: {entity_color}; background: none; font-weight: bold"
            
            # Convert back to HTML string
            modified_html = f'<div class="annotated-text">{str(soup)}</div>'

            # Define the entity labels with their respective colors
            entity_labels_html = """
            <div style="margin-bottom: 10px;">
                <span style="color: red; font-weight: bold; text-decoration: underline;">Years of Experience</span> &nbsp;
                <span style="color: blue; font-weight: bold; text-decoration: underline;">Education</span> &nbsp;
                <span style="color: green; font-weight: bold; text-decoration: underline;">Role</span> &nbsp;
                <span style="color: #FFC300; font-weight: bold; text-decoration: underline;">Tools & Tech</span> &nbsp;
                <span style="color: orange; font-weight: bold; text-decoration: underline;">Certifications</span> &nbsp;
                <span style="color: purple; font-weight: bold; text-decoration: underline;">Location</span> &nbsp;
                <span style="color: brown; font-weight: bold; text-decoration: underline;">Concepts</span> &nbsp;
                <span style="color: pink; font-weight: bold; text-decoration: underline;">Soft Skills</span> &nbsp;
                <span style="color: violet; font-weight: bold; text-decoration: underline;">Domain</span>
            </div>
            """

            # Display the entity labels before the annotated text
            st.markdown(entity_labels_html, unsafe_allow_html=True)
            
            st.write(modified_html, unsafe_allow_html=True)

        else:
            st.write("Please enter a job description.")
