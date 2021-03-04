from xhtml2pdf.document import pisaDocument
from StringIO import StringIO
import subprocess

# example adapted from http://obroll.com/generate-pdf-with-xhtml2pdf-pisa-in-django-examples/


html_input_filename = 'pisa-inputfile.html'
pdf_output_filename = 'pisa-outputfile.pdf'
tmp_io = StringIO()
with open(html_input_filename) as html_input_fileobj,\
      open(pdf_output_filename, 'w') as pdf_output_fileobj:
      pdfprocess = pisaDocument(html_input_fileobj, 
                                dest = tmp_io)
      pdf_output_fileobj.write(tmp_io.getvalue())

subprocess.call(['acroread', pdf_output_filename])

# Remarks:

# a) the StingIO() object 'tmp_io' keeps the pdf content in memory.
# b) Unicode error  sometime happens. pdfprocess.err say contains an error signal




      
            
