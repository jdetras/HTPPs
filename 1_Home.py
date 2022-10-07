import streamlit as st

def intro():
    import streamlit as st

    st.write("# High-throughput Drone Phenotyping Hub")
    st.sidebar.success("Homepage")

    st.markdown(
        """
        The hub is a collection of resources for drone images, database and image analysis using machine learning. 
        """
    )
    
intro()

col1, col2, col3 = st.columns(3)

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
        [phenotype prediction](./pages/2_Phenotype_Prediction.py)
        """
    )
    st.markdown(
        """
        [disease identifier](./pages/3_Rice_Disease_Identifier.py)
        """
    )
