import streamlit as st

def intro():
    import streamlit as st

    st.write("# High-throughput Drone Phenotyping Hub")
#    st.sidebar.success("Homepage")

    st.markdown(
        """
        The hub is a collection of resources for drone images, database and image analysis using machine learning. 
        """
    )
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.header("Imagebreed")
    st.image("./images/imagebreedlogo_noBackground.png")
    st.markdown(
        """
        [Imagebreed](https://imagebreed.org)
        """
        )

with col2:
    st.header("CropGalaxy")
    st.image("./images/GS-Galaxy_logo.jpg")
    st.markdown(
        """
        [cropgalaxy](http://cropgalaxy.excellenceinbreeding.org/)
        """
    )

with col3:
    st.header("AI/ML")
    st.image("./images/aiml.png")
    st.markdown(
        """
        [phenotype prediction](http://localhost:8501/Phenotype_Prediction)
        """
    )
    st.markdown(
        """
        [disease identifier](http://localhost:8501/Rice_Disease_Identifier)
        """
    )

intro()