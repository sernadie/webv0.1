import os
import tempfile
from docx2pdf import convert
from django.http import HttpResponse
from django.views import View
from django.core.files.storage import default_storage

class WordToPDFView(View):
    def post(self, request):
        word_file = request.FILES['word_file']
        _, temp_word_path = tempfile.mkstemp()
        
        # Guarda el archivo en un directorio temporal
        with open(temp_word_path, 'wb') as f:
            for chunk in word_file.chunks():
                f.write(chunk)

        _, temp_pdf_path = tempfile.mkstemp()
        convert(temp_word_path, temp_pdf_path)

        # Envía el archivo PDF como respuesta
        with open(temp_pdf_path, 'rb') as f:
            pdf_data = f.read()

        os.remove(temp_word_path)
        os.remove(temp_pdf_path)

        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{word_file.name}.pdf"'
        return response
