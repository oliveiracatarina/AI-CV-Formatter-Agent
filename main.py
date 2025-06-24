from google.adk import Agent
# Adicionar as bibliotecas necessárias para PDF e DOCX
import pdfplumber
from docx import Document
import os


class AICVFormatterAgent(Agent):
    def __init__(self):
        super().__init__(
            name="AI CV Formatter Agent",
            description="Automates the analysis, rewriting, and formatting of resumes. Receives a PDF and generates a DOCX."
        )

    def process_cv(self, pdf_path, output_docx_path):
        """
        Receives a resume in PDF format and generates a formatted Word (DOCX) file.
        """
        print(f"Processing PDF resume: {pdf_path}")
        # TODO: Read the PDF (e.g., using pdfplumber or PyPDF2)
        # TODO: Extract and normalize information
        # TODO: Generate the DOCX file (e.g., using python-docx)
        print(f"Formatted resume saved at: {output_docx_path}")
        pass

if __name__ == "__main__":
    agent = AICVFormatterAgent()
    agent.process_cv("caminho/para/curriculo.pdf", "caminho/saida/curriculo_formatado.docx")
