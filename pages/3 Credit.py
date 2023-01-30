import streamlit as st


def credit_page():
    st.title("Credits")
    st.write("Collaborators:")
    st.write("- Dr. Unaizah Hanum Binti Obaidellah, Project Supervisor")
    st.write("- Raja Arif Aizuddin bin Raja Kamarudin, Collaborator")
    st.write("- Adrian Danial Bin Ashraf Martinus, Collaborator")
    st.write("- Mohammad Firdaus Azmi bin Mohammad Faizal , Collaborator")
    st.write("- Muaz Rabbani bin Muzamir, Collaborator")
    st.write()
    image_url = "MF logo.jpg"

    st.image(image_url, width=100)
    st.write("Midnight Fusic")


if __name__ == '__main__':
    credit_page()
