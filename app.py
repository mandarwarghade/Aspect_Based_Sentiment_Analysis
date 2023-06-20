import streamlit as st
st.set_page_config(layout="wide")



from pyabsa import ATEPCCheckpointManager

aspect_extractor = ATEPCCheckpointManager.get_aspect_extractor(checkpoint='english',
                                   auto_device=True  # False means load model on CPU
                                   )

# You can inference from a list of setences or a DatasetItem from PyABSA 


def data(text):

    examples = [text]
    inference_source = examples
    atepc_result = aspect_extractor.extract_aspect(inference_source=inference_source,  #
                            pred_sentiment=True,  # Predict the sentiment of extracted aspect terms
                            )

    dict={}
    for i in range(len(atepc_result[0]['aspect'])):
        dict[atepc_result[0]['aspect'][i]]=atepc_result[0]['sentiment'][i]

    return dict    


st.markdown("<h1 style='text-align: center; color: white;'>Aspect_Based_Sentiment_Analysis</h1>", unsafe_allow_html=True)
text = st.text_input('Enter your text: ', ' ')

result=data(text)

if st.button('Predict Aspect Based Sentiment Analysis'):
    new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">{text}</p>'
    st.write(result)


