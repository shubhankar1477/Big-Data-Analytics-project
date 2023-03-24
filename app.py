

from PIL import Image

import numpy as np

import streamlit as st
import boto3
import trp
from scripts.utils import ClsCommonUtils
from scripts.textract import ClsExtractor
from scripts.webui import clsUIComp


if __name__ == '__main__':
    objUi = clsUIComp()
    objUi.runUi()


