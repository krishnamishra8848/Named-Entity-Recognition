import streamlit as st
import spacy
from spacy import displacy

# Load the pre-trained spaCy model for English
nlp = spacy.load("en_core_web_md")  # Use a larger model for better performance

# Mapping of short entity labels to full names
ENTITY_LABELS = {
    "PERSON": "Person",
    "NORP": "Nationalities or Religious/Political Groups",
    "FAC": "Facilities",
    "ORG": "Organization",
    "GPE": "Country",
    "LOC": "Location",
    "PRODUCT": "Product",
    "EVENT": "Event",
    "WORK_OF_ART": "Work of Art",
    "LAW": "Law",
    "LANGUAGE": "Language",
    "DATE": "Date",
    "TIME": "Time",
    "PERCENT": "Percentage",
    "MONEY": "Money",
    "QUANTITY": "Quantity",
    "ORDINAL": "Ordinal",
    "CARDINAL": "Cardinal",
}

# Streamlit app title
st.title("Advanced Named Entity Recognition (NER) App")

# Text input for user
user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input:
        # Process the input text with spaCy
        doc = nlp(user_input)
        
        # Display recognized entities
        st.write("### Recognized Entities:")
        entities = [(ent.text, ENTITY_LABELS.get(ent.label_, ent.label_)) for ent in doc.ents]
        
        # Display entities in a more organized way
        for entity, label in entities:
            st.write(f"**{entity}**: {label}")
        
        # Optional: visualize the entities in the text
        st.write("### Entity Visualization:")
        html = displacy.render(doc, style="ent", jupyter=False)
        st.components.v1.html(html, height=300, scrolling=True)
    else:
        st.warning("Please enter some text for analysis.")
