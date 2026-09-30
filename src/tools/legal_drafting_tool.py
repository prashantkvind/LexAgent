import os
import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from config import GENERATED_DOCS_DIR

class LegalDraftingTool:
    """
    Tool 3: Legal Document Drafting Tool
    Generates formal legal documents (Notice, Form M Application, Petition) using python-docx.
    """
    name = "legal_drafting_tool"
    description = "Generates formal legal documents in .docx format with professional formatting."

    def __init__(self, output_dir: Path = GENERATED_DOCS_DIR):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self, 
            doc_type: str = "LEGAL NOTICE",
            client_name: str = "Shri Rajesh Sharma",
            opposite_party: str = "M/s Royal Palms Infrastructure Pvt Ltd",
            facts: str = "Failure to construct promised Swimming Pool as confirmed by PIO RTI Response No. PIO/RERA/2024/09842.",
            statutes: str = "Section 14 & Section 18 of the Real Estate (Regulation and Development) Act, 2016 (RERA)",
            demands: str = "1. Deliver and construct the swimming pool within 30 days.\n2. Pay interest at 10.75% p.a. for delay in common amenity handover.",
            output_filename: Optional[str] = None) -> Dict[str, Any]:
        """
        Creates a structured legal document (.docx).
        """
        doc = docx.Document()

        # Set Page Margins
        for section in doc.sections:
            section.top_margin = Inches(1.0)
            section.bottom_margin = Inches(1.0)
            section.left_margin = Inches(1.0)
            section.right_margin = Inches(1.0)

        # Document Header / Title
        title_p = doc.add_paragraph()
        title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        title_run = title_p.add_run(f"FORMAL {doc_type.upper()}")
        title_run.font.name = 'Calibri'
        title_run.font.size = Pt(16)
        title_run.font.bold = True
        title_run.font.color.rgb = RGBColor(15, 30, 70)  # Deep Navy

        # Subtitle / Statute Citation
        sub_p = doc.add_paragraph()
        sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        sub_run = sub_p.add_run(f"Issued under {statutes}")
        sub_run.font.size = Pt(11)
        sub_run.font.italic = True
        sub_run.font.color.rgb = RGBColor(100, 100, 100)

        doc.add_paragraph().paragraph_format.space_after = Pt(12)

        # Date & Reference Line
        date_str = datetime.date.today().strftime("%B %d, %Y")
        ref_p = doc.add_paragraph()
        ref_p.add_run(f"DATE: ").bold = True
        ref_p.add_run(f"{date_str}\n")
        ref_p.add_run(f"NOTICE REF NO: ").bold = True
        ref_p.add_run(f"LEX/{datetime.date.today().year}/NOTICE/042")

        doc.add_paragraph().paragraph_format.space_after = Pt(12)

        # Address Blocks
        add_p = doc.add_paragraph()
        add_p.add_run("BY REGISTERED POST A.D. / SPEED POST\n\n").bold = True
        add_p.add_run("TO,\n").bold = True
        add_p.add_run(f"THE MANAGING DIRECTOR / PROMOTER,\n")
        add_p.add_run(f"{opposite_party},\n")
        add_p.add_run("Registered Office: Sector 62, Commercial Complex, Noida, UP.\n\n")
        add_p.add_run("FROM LEGAL COUNSEL ON BEHALF OF:\n").bold = True
        add_p.add_run(f"{client_name},\n")
        add_p.add_run("Flat No. 402, Royal Palms Residency, Sector 62, Noida, UP.\n")

        # Subject Line
        subj_p = doc.add_paragraph()
        subj_p.paragraph_format.space_before = Pt(12)
        subj_p.paragraph_format.space_after = Pt(12)
        subj_run = subj_p.add_run(f"SUBJECT: LEGAL NOTICE FOR BREACH OF SANCTIONED PLAN & FAILURE TO DELIVER COMMON AMENITIES UNDER RERA ACT 2016")
        subj_run.font.bold = True
        subj_run.font.underline = True

        # Body - Paragraph 1: Facts
        doc.add_heading("1. STATEMENT OF FACTS", level=2)
        p_facts = doc.add_paragraph(facts)
        p_facts.paragraph_format.line_spacing = 1.15
        p_facts.paragraph_format.space_after = Pt(12)

        # Body - Paragraph 2: Statutory Breach
        doc.add_heading("2. STATUTORY VIOLATION & LEGAL STANDING", level=2)
        p_stat = doc.add_paragraph(
            f"That under {statutes}, the Promoter is strictly prohibited from altering sanctioned common amenities without explicit written consent. "
            "Furthermore, as per the binding precedent of the Hon'ble Supreme Court in Pioneer Urban Land & Infrastructure Ltd. v. Govindan Raghavan, "
            "failure to hand over promised amenities constitutes unfair trade practice and breach of developer obligations."
        )
        p_stat.paragraph_format.line_spacing = 1.15
        p_stat.paragraph_format.space_after = Pt(12)

        # Body - Paragraph 3: Demands
        doc.add_heading("3. REQUISITION & DEMANDS", level=2)
        p_dem = doc.add_paragraph(
            "Take notice that you are hereby called upon to comply with the following requisitions within thirty (30) days from the receipt of this notice:\n"
        )
        p_dem.paragraph_format.space_after = Pt(6)

        for d_line in demands.split("\n"):
            if d_line.strip():
                dp = doc.add_paragraph(d_line.strip(), style='List Bullet')
                dp.paragraph_format.space_after = Pt(4)

        # Warning & Signature Block
        doc.add_paragraph().paragraph_format.space_after = Pt(12)
        p_warn = doc.add_paragraph(
            "PLEASE TAKE FURTHER NOTICE that in the event of your failure to comply with the above demands within the stipulated period of 30 days, "
            "our Client has given strict instructions to initiate formal Complaint proceedings before the RERA Tribunal under Section 31 "
            "for penal proceedings and recovery of full damages at your sole cost and risk."
        )
        p_warn.paragraph_format.line_spacing = 1.15
        p_warn.paragraph_format.space_after = Pt(24)

        sig_p = doc.add_paragraph()
        sig_p.add_run("Yours faithfully,\n\n\n").bold = True
        sig_p.add_run("_____________________________\n")
        sig_p.add_run("ADVOCATE / LEGAL COUNSEL\n")
        sig_p.add_run("LexAgent RERA & High Court Advisory Practice")

        # Save File
        if not output_filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"Legal_Notice_{client_name.replace(' ', '_')}_{timestamp}.docx"

        file_path = self.output_dir / output_filename
        doc.save(str(file_path))

        return {
            "status": "success",
            "file_name": file_path.name,
            "file_path": str(file_path),
            "doc_type": doc_type,
            "summary": f"Generated formal {doc_type} document at {file_path.name}"
        }
