import io
from fileinput import filename
import pdfkit

import win_unicode_console

win_unicode_console.enable()
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from io import StringIO
import xhtml2pdf.pisa as pisa


def html_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.CreatePDF(io.BytesIO(html.encode('UTF-8')), result, encoding='UTF-8')
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=app.pdf'
        return response
    else:
        return HttpResponse('error')
