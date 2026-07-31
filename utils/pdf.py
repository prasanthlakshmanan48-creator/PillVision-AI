from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(report_text,
               filename="Medicine_Report.pdf"):

    styles=getSampleStyleSheet()

    doc=SimpleDocTemplate(filename)

    story=[]

    story.append(
        Paragraph(
            "<b>PillVision AI Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    report_text=report_text.replace("\n","<br/>")

    story.append(
        Paragraph(
            report_text,
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename
