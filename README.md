# Emoji PDF Generator 🚀

A Python tool to generate PDFs with full emoji support. This solves the common problem of emoji rendering in PDF generation libraries like ReportLab and fpdf2.

## The Problem

Most PDF generation libraries in Python have issues with emoji support:
- **ReportLab**: Font compatibility issues with emoji fonts
- **fpdf2**: Limited Unicode support, emoji appear as squares or missing glyphs
- **Other libraries**: Various encoding and font rendering problems

## The Solution

This tool uses **WeasyPrint** to convert HTML to PDF, which provides excellent emoji support out of the box.

## Features ✨

- 🎯 **Perfect emoji rendering** - All emoji display correctly
- 📱 **Cross-platform** - Works on Linux, macOS, and Windows
- 🎨 **Customizable styling** - Support for custom CSS
- 📄 **HTML input** - Use familiar HTML markup
- 🛠️ **Command-line interface** - Easy to integrate into workflows
- 🐍 **Python API** - Use as a library in your projects

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/emoji-pdf-generator.git
cd emoji-pdf-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Command Line Usage

1. Create an HTML file with emoji content:
```html
<!-- example.html -->
<h1>📘 My Document</h1>
<p>This is a test with emoji: 🎉 🚀 💻 📱</p>
<ul>
    <li>✅ First item</li>
    <li>✅ Second item</li>
    <li>✅ Third item</li>
</ul>
```

2. Generate the PDF:
```bash
python emoji_pdf_generator.py -i example.html -o output.pdf
```

### Python API Usage

```python
from emoji_pdf_generator import generate_pdf_with_emoji

# HTML content with emoji
content = """
<h1>📘 My Document</h1>
<p>This is a test with emoji: 🎉 🚀 💻 📱</p>
<ul>
    <li>✅ First item</li>
    <li>✅ Second item</li>
    <li>✅ Third item</li>
</ul>
"""

# Generate PDF
success = generate_pdf_with_emoji(
    content=content,
    output_file="output.pdf",
    title="My Document"
)

if success:
    print("PDF generated successfully!")
```

## Examples

### Basic Usage
```bash
python emoji_pdf_generator.py -i content.html -o document.pdf
```

### With Custom Title
```bash
python emoji_pdf_generator.py -i content.html -o document.pdf -t "My Awesome Document"
```

### With Custom CSS
```bash
python emoji_pdf_generator.py -i content.html -o document.pdf -s custom.css
```

## Command Line Options

- `-i, --input`: Input HTML file (required)
- `-o, --output`: Output PDF filename (required)
- `-t, --title`: Document title (default: "Document")
- `-s, --style`: Custom CSS file for styling (optional)

## Supported Emoji

All Unicode emoji are supported, including:
- 😀 😃 😄 😁 😆 😅 😂 🤣 😊 😇
- 🎉 🎊 🎈 🎁 🎀 🎂 🍰 🧁 🍭 🍬
- 📱 💻 🖥️ ⌨️ 🖱️ 🖨️ 📷 📹 🎥 📺
- 🚀 🛸 🛰️ 🌟 ⭐ 🌙 ☀️ 🌈 ⚡ 🔥
- And many more!

## Why WeasyPrint?

After testing multiple approaches:
- ❌ **ReportLab**: Font compatibility issues
- ❌ **fpdf2**: Poor Unicode support
- ✅ **WeasyPrint**: Perfect emoji rendering

WeasyPrint converts HTML/CSS to PDF and handles emoji natively, making it the ideal solution.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [WeasyPrint](https://weasyprint.org/) for excellent HTML to PDF conversion
- The Python community for various PDF generation libraries that helped us understand the problem

## Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'weasyprint'"**
   - Make sure you've installed the requirements: `pip install -r requirements.txt`

2. **Emoji not displaying correctly**
   - Ensure your system has emoji fonts installed
   - On Linux: `sudo apt install fonts-noto-color-emoji`
   - On macOS: Emoji fonts are included by default
   - On Windows: Emoji fonts are included by default

3. **Permission errors**
   - Make sure you have write permissions in the output directory

### Getting Help

If you encounter issues:
1. Check the [Issues](https://github.com/yourusername/emoji-pdf-generator/issues) page
2. Create a new issue with details about your problem
3. Include your Python version, operating system, and error messages