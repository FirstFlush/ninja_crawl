from .base import BaseTool
import base64
import io
import logging
from pathlib import Path
import pdfplumber
from pdfplumber.pdf import PDF

logger = logging.getLogger(__name__)

class PdfToolkit(BaseTool):

    _open_pdfs: list[PDF] = []

    def save_pdf(self, b64_data: str, file_name: str, mode: str = "w"):
        with open(file_name, mode) as f:
            f.write(b64_data)

    def open_pdf_from_file(self, path: Path, b64_encoded: bool = False) -> PDF:
        if not path.absolute():
            raise ValueError(f"Expected absolute path, got relative path: {path}")
        with open(path, "r") as f:
            pdf_data = f.read()
        if b64_encoded:
            pdf_binary = base64.b64decode(pdf_data)
        else:
            pdf_binary = pdf_data.encode()
        return self.open_pdf_from_stream(pdf_binary)
        
    def open_pdf_from_stream(self, data: bytes) -> PDF:
        try:
            pdf = pdfplumber.open(io.BytesIO(data))
        except Exception as e:
            msg = f"{e.__class__.__name__}: {self.__class__.__name__} received invalid PDF data of type `{type(data)}`"
            logger.error(msg, exc_info=True)
            raise
        else:
            self._append_pdf(pdf)
            return pdf

    def _append_pdf(self, pdf: PDF):
        self._open_pdfs.append(pdf)
        logger.debug("Opened PDF in memory with pdfplumber")


    def clean_up(self):
        for pdf in self._open_pdfs:
            logger.debug(f"{self.__class__.__name__}: closing open pdf")
            pdf.close()
        self._open_pdfs.clear()