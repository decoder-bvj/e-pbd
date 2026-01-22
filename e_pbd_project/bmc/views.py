
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from .models import BMCProfile

def bmc_pdf(request, pk):
    bmc = get_object_or_404(BMCProfile, pk=pk)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="PBR_{bmc.panchayat_name}.pdf"'

    doc = SimpleDocTemplate(response)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal_style = styles["Normal"]

    elements.append(Paragraph("People's Biodiversity Register (PBR)", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Panchayat: {bmc.panchayat_name}", normal_style))
    elements.append(Paragraph(f"District: {bmc.district}", normal_style))
    elements.append(Paragraph(f"Block: {bmc.block}", normal_style))
    elements.append(Paragraph(f"Population: {bmc.population}", normal_style))

    doc.build(elements)
    return response
