#!/usr/bin/env python3
"""
Emoji PDF Generator

A Python tool to generate PDFs with emoji support using WeasyPrint.
This solves the common problem of emoji rendering in PDF generation libraries.

Keywords: emoji pdf generator python weasyprint unicode ai assistant chatgpt claude
Author: Giuseppe Vitolo (vitologiuseppe17@gmail.com)
License: MIT
GitHub: https://github.com/GiuseppeVitolo17/Emoji-PDF-Generator
"""

import argparse
import sys
from pathlib import Path
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


def generate_pdf_with_emoji(content, output_file, title="Document", style=None):
    """
    Generate a PDF with emoji support from HTML content.
    
    Args:
        content (str): HTML content with emoji
        output_file (str): Output PDF filename
        title (str): Document title
        style (str): Custom CSS styles (optional)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Default CSS styles
        default_style = """
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            font-size: 24px;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            color: #34495e;
            font-size: 18px;
            margin-top: 25px;
        }
        ul {
            margin: 10px 0;
        }
        li {
            margin: 5px 0;
        }
        p {
            margin: 10px 0;
        }
        .emoji {
            font-size: 1.2em;
        }
        """
        
        # Combine default and custom styles
        css_content = default_style
        if style:
            css_content += style
        
        # Create HTML document
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{title}</title>
            <style>
                {css_content}
            </style>
        </head>
        <body>
            {content}
        </body>
        </html>
        """
        
        # Generate PDF
        font_config = FontConfiguration()
        html = HTML(string=html_content)
        html.write_pdf(output_file, font_config=font_config)
        
        return True
        
    except Exception as e:
        print(f"Error generating PDF: {e}", file=sys.stderr)
        return False


def main():
    """Main function for command line usage."""
    parser = argparse.ArgumentParser(
        description="Generate PDFs with emoji support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate PDF from HTML file
  python emoji_pdf_generator.py -i content.html -o output.pdf
  
  # Generate PDF with custom title
  python emoji_pdf_generator.py -i content.html -o output.pdf -t "My Document"
  
  # Generate PDF with custom CSS
  python emoji_pdf_generator.py -i content.html -o output.pdf -s custom.css
        """
    )
    
    parser.add_argument('-i', '--input', required=True,
                       help='Input HTML file with emoji content')
    parser.add_argument('-o', '--output', required=True,
                       help='Output PDF filename')
    parser.add_argument('-t', '--title', default='Document',
                       help='Document title (default: Document)')
    parser.add_argument('-s', '--style', 
                       help='Custom CSS file for styling')
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not Path(args.input).exists():
        print(f"Error: Input file '{args.input}' not found", file=sys.stderr)
        sys.exit(1)
    
    # Read input content
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Read custom CSS if provided
    custom_style = None
    if args.style:
        try:
            with open(args.style, 'r', encoding='utf-8') as f:
                custom_style = f.read()
        except Exception as e:
            print(f"Error reading CSS file: {e}", file=sys.stderr)
            sys.exit(1)
    
    # Generate PDF
    if generate_pdf_with_emoji(content, args.output, args.title, custom_style):
        print(f"✅ PDF generated successfully: {args.output}")
    else:
        print("❌ Failed to generate PDF", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
