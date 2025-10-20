#!/usr/bin/env python3
"""
PyPDF Tutorial Script

This script demonstrates various features of the PyPDF library for working with PDF files.
It covers reading, writing, merging, splitting, and extracting text from PDFs.
"""
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os


def create_sample_pdf(output_path):
    """Create a sample PDF file for demonstration purposes."""
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter

    # Add some content
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, "Sample PDF Document")
    c.drawString(100, height - 130, "Created with PyPDF and ReportLab")

    # Add a second page
    c.showPage()
    c.drawString(100, height - 100, "This is the second page")
    c.save()


def read_pdf_metadata(pdf_path):
    """Read and display PDF metadata."""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        print("\n=== PDF Metadata ===")
        print(f"Number of pages: {len(reader.pages)}")
        print(f"Author: {reader.metadata.author}")
        print(f"Creator: {reader.metadata.creator}")
        print(f"Producer: {reader.metadata.producer}")
        print(f"Subject: {reader.metadata.subject}")
        print(f"Title: {reader.metadata.title}")


def extract_text_from_pdf(pdf_path):
    """Extract and display text from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        print("\n=== Extracted Text ===")
        for i, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            print(f"\n--- Page {i} ---")
            print(text[:200] + "..." if len(text) > 200 else text)


def merge_pdfs(pdf_paths, output_path):
    """Merge multiple PDFs into a single PDF."""
    merger = PdfMerger()

    for pdf in pdf_paths:
        merger.append(pdf)

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f"\nMerged {len(pdf_paths)} files into {output_path}")


def split_pdf(pdf_path, output_dir):
    """Split a PDF into individual pages."""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)

        for i, page in enumerate(reader.pages, 1):
            writer = PdfWriter()
            writer.add_page(page)

            output_filename = output_dir / f"page_{i}.pdf"
            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)

    print(f"\nSplit PDF into {len(reader.pages)} individual pages in {output_dir}")


def rotate_page(pdf_path, page_num, degrees, output_path):
    """Rotate a specific page in a PDF."""
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        if i == page_num - 1:  # Convert to 0-based index
            page.rotate(degrees)
        writer.add_page(page)

    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

    print(f"\nRotated page {page_num} by {degrees} degrees")


def main():
    # Create a directory for output files
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Create sample PDFs for demonstration
    sample1 = output_dir / "sample1.pdf"
    sample2 = output_dir / "sample2.pdf"
    create_sample_pdf(sample1)
    create_sample_pdf(sample2)  # Create a second sample with different content

    # Demonstrate reading PDF metadata
    read_pdf_metadata(sample1)

    # Demonstrate text extraction
    extract_text_from_pdf(sample1)

    # Demonstrate merging PDFs
    merged_pdf = output_dir / "merged.pdf"
    merge_pdfs([sample1, sample2], merged_pdf)

    # Demonstrate splitting a PDF
    split_dir = output_dir / "split_pages"
    split_dir.mkdir(exist_ok=True)
    split_pdf(merged_pdf, split_dir)

    # Demonstrate rotating a page
    rotated_pdf = output_dir / "rotated.pdf"
    rotate_page(sample1, 1, 90, rotated_pdf)  # Rotate first page 90 degrees

    print("\n=== All operations completed successfully! ===")
    print(f"Check the '{output_dir}' directory for output files.")


if __name__ == "__main__":
    # Install required packages if not already installed
    try:
        from PyPDF2 import PdfReader
        from reportlab.lib.pagesizes import letter
    except ImportError:
        print("Installing required packages...")
        import sys
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf2", "reportlab"])

    main()
