from PIL import Image

import numpy as np

import streamlit as st
import boto3
import trp.trp2 as t2
from scripts.utils import ClsCommonUtils
from scripts.textract import ClsExtractor

class clsUIComp:
    def __init__(self):
        self.process =True
        self.error = ''
        self.byte_array = None
  
    def runUi(self):
        try:
            st.title(':blue[Intelligent Document Processing]')
            img_file_buffer = st.file_uploader(label="Upload image", type=['jpg', 'png','jpeg'])

    # Checking the Format of the page
            if img_file_buffer:
                if img_file_buffer is not None:
                    image_bytes = ClsCommonUtils.pil_image_to_byte_array(Image.open(img_file_buffer))
                    image_array = np.array(Image.open(img_file_buffer))
                    self.byte_array = image_bytes

            st.header("Review and Extract Data")
            query = st.text_input("Enter Your Query")
            button = st.button("Extract Data")
            if button:
                response = self._extract_data(query)
                st.write(response)
                d = t2.TDocumentSchema().load(response)
                page = d.pages[0]
                query_answers = d.get_query_answers(page=page)
                st.write(query_answers)
                
        except Exception as e:
            self.process = False
            self.error = "Error In  Running Ui Compnent"
        return 1
    @st.cache   
    def _extract_data(self,query):
        resp = boto3.client("textract").analyze_document(Document={"Bytes": self.byte_array},
                                                            FeatureTypes=['QUERIES'],
                                                            QueriesConfig={"Queries": [{
                                                                            "Text": query,
                                                                            "Alias": "SSN"}]})
        return resp
    
    @st.cache
    def _extract_metadata(self):
        print("Processing Image")
        response = boto3.client("textract").analyze_document(Document={"Bytes": self.byte_array},FeatureTypes=['FORMS'])
        print(response)
        return response

    



