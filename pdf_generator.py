from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(content, filename="study_pack.pdf"):
    os.makedirs("output", exist_ok=True)
    path = f"output/{filename}"

    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    story = []

    for line in content.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 10))

    doc.build(story)
    return path
