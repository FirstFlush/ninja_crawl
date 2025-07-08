from ...base import BaseEngine
import base64
import io
from pathlib import Path
import pdfplumber
from pdfplumber.pdf import PDF


class PdfToolkit(BaseEngine):

    _open_pdfs: list[PDF] = []

    def save_pdf(self, b64_data: str, file_name: str, mode: str = "w"):
        with open(file_name, mode) as f:
            f.write(b64_data)

    def open_pdf_from_file(self, path: Path, b64_encoded: bool = False) -> PDF:
        if not path.absolute():
            raise RuntimeError(f"Expected absolute path, got relative path: {path}")
        with open(path, "r") as f:
            pdf_data = f.read()
        if b64_encoded:
            pdf_binary = base64.b64decode(pdf_data)
        else:
            pdf_binary = pdf_data.encode()
        return self.open_pdf_from_stream(pdf_binary)

    def open_pdf_from_stream(self, data: bytes, **kwargs) -> PDF:
        try:
            pdf = pdfplumber.open(io.BytesIO(data), **kwargs)
        except Exception as e:
            msg = f"{e.__class__.__name__}: {self.__class__.__name__} received invalid PDF data of type `{type(data)}`"
            raise RuntimeError(msg) from e
        else:
            self._append_pdf(pdf)
            return pdf

    def _append_pdf(self, pdf: PDF):
        self._open_pdfs.append(pdf)

    def clean_up(self):
        for pdf in self._open_pdfs:
            pdf.close()
        self._open_pdfs.clear()