from pdfplumber.pdf import PDF
from .base import BaseEngine


class PdfEngine(BaseEngine):

    def __init__(self, pdf: PDF):
        self.pdf = pdf