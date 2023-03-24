from scripts.utils import  ClsCommonUtils
import streamlit as st
class ClsExtractor:
    __objTextract = None
    def __init__(self,Uiobject) -> None:
        if ClsExtractor.__objTextract == None:
            ClsExtractor.__objTextract = ClsCommonUtils.get_textract_object()
        else:
            print("Already Loaded")
        self.Uiobject = Uiobject
    def extract(self,query):
        print(True if (self.Uiobject.byte_array) else False)
        try:
            if self.Uiobject.process == False:
                return 
            else:
                response = self.objTextract.analyze_document(Document={"Bytes": self.Uiobject.byte_array},
                                                            FeatureTypes=['QUERIES'],
                                                            QueriesConfig={"Queries": [{
                                                                            "Text": query}]})
            return response
        except Exception as e:
            self.Uiobject.process = False

    def _process_image(self):
        print("Processing Image")
        response = self.objTextract.analyze_document(Document={"Bytes": self.Uiobject.byte_array},FeatureTypes=['FORMS'])
        return response

