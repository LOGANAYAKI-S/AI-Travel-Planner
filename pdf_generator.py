from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(travel_plan, filename="travel_plan.pdf"):
    pdf = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Travel Planner", styles['Title']))
    content.append(Paragraph(travel_plan.replace("\n", "<br/>"), styles['BodyText']))

    pdf.build(content)

    return filename