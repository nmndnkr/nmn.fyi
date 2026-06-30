from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "DataSelf-Product-Case-Study.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = letter
MARGIN = 0.55 * inch
CONTENT_W = PAGE_W - (2 * MARGIN)

INK = HexColor("#11120f")
PAPER = HexColor("#f1f0e8")
WHITE = HexColor("#fffef8")
MUTED = HexColor("#666960")
LINE = HexColor("#c8c8c0")
ACID = HexColor("#c7ff18")
NIGHT = HexColor("#131510")


def style(name, size, leading=None, color=INK, font="Helvetica", **kwargs):
    return ParagraphStyle(
        name,
        fontName=font,
        fontSize=size,
        leading=leading or size * 1.25,
        textColor=color,
        alignment=TA_LEFT,
        spaceAfter=0,
        **kwargs,
    )


BODY = style("body", 8.1, 10.4, MUTED)
BODY_DARK = style("body-dark", 8.1, 10.4, HexColor("#c6c8bf"))
LEAD = style("lead", 10.1, 12.5, INK)
SMALL = style("small", 6.5, 8.3, MUTED)
LABEL = style("label", 6.2, 7.5, MUTED, "Helvetica-Bold")
H2 = style("h2", 16, 17.2, INK, "Helvetica-Bold")
H2_LIGHT = style("h2-light", 16, 17.2, PAPER, "Helvetica-Bold")
H3 = style("h3", 9.2, 10.7, INK, "Helvetica-Bold")
H3_LIGHT = style("h3-light", 9.2, 10.7, PAPER, "Helvetica-Bold")


def para(c, text, x, top, width, paragraph_style=BODY):
    p = Paragraph(text, paragraph_style)
    _, height = p.wrap(width, PAGE_H)
    p.drawOn(c, x, top - height)
    return top - height


def label(c, text, x, y, color=MUTED):
    c.setFont("Helvetica-Bold", 6.2)
    c.setFillColor(color)
    c.drawString(x, y, text.upper())


def line(c, y, x=MARGIN, width=CONTENT_W, color=LINE):
    c.setStrokeColor(color)
    c.setLineWidth(0.55)
    c.line(x, y, x + width, y)


def footer(c, page_number):
    line(c, 29, color=HexColor("#b7b8b0"))
    c.setFont("Helvetica", 6.2)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, 18, "NAMAN DHANKHAR  /  DATASELF PRODUCT CASE")
    page = f"0{page_number} / 02"
    c.drawRightString(PAGE_W - MARGIN, 18, page)


def metric_card(c, x, top, width, value, text):
    height = 48
    c.setFillColor(WHITE)
    c.setStrokeColor(LINE)
    c.rect(x, top - height, width, height, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(INK)
    c.drawString(x + 7, top - 19, value)
    para(c, text, x + 7, top - 27, width - 14, SMALL)


def decision_row(c, y, choice, rejected, reason, cost, dark=False):
    bg = NIGHT if dark else WHITE
    text = PAPER if dark else INK
    muted = HexColor("#b7b9b0") if dark else MUTED
    c.setFillColor(bg)
    c.setStrokeColor(HexColor("#393b35") if dark else LINE)
    c.rect(MARGIN, y - 45, CONTENT_W, 45, fill=1, stroke=1)

    label(c, "Chose", MARGIN + 8, y - 12, muted)
    para(c, f"<b>{choice}</b>", MARGIN + 8, y - 17, 118, style("dc", 7.8, 9.2, text))
    label(c, "Over", MARGIN + 140, y - 12, muted)
    para(c, rejected, MARGIN + 140, y - 17, 105, style("dr", 7.4, 8.8, text))
    label(c, "Why", MARGIN + 260, y - 12, muted)
    para(c, reason, MARGIN + 260, y - 17, 183, style("dw", 7.2, 8.5, text))
    label(c, "Cost", MARGIN + 458, y - 12, muted)
    para(c, cost, MARGIN + 458, y - 17, CONTENT_W - 466, style("dco", 6.8, 8.1, muted))
    return y - 45


def page_one(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    label(c, "DataSelf / Product case / 2026", MARGIN, PAGE_H - 35)
    label(c, "Product - Prototype - Validation", PAGE_W - MARGIN - 142, PAGE_H - 35)
    c.setFillColor(ACID)
    c.rect(MARGIN, PAGE_H - 48, CONTENT_W, 4, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 31)
    c.setFillColor(INK)
    c.drawString(MARGIN, PAGE_H - 87, "DataSelf")
    c.setFont("Times-Italic", 18)
    c.setFillColor(MUTED)
    c.drawString(MARGIN, PAGE_H - 111, "Your AI learns how you work. You should be able to take that with you.")

    para(
        c,
        "A local memory layer that turns real LLM sessions into portable working rules - "
        "without storing the conversation itself.",
        MARGIN,
        PAGE_H - 132,
        420,
        LEAD,
    )

    repo_text = "github.com/nmndnkr/dataself"
    repo_x = PAGE_W - MARGIN - stringWidth(repo_text, "Helvetica-Bold", 7.2)
    c.setFont("Helvetica-Bold", 7.2)
    c.setFillColor(INK)
    c.drawString(repo_x, PAGE_H - 145, repo_text)
    c.linkURL(
        "https://github.com/nmndnkr/dataself",
        (repo_x, PAGE_H - 149, PAGE_W - MARGIN, PAGE_H - 136),
    )

    cards_top = PAGE_H - 175
    card_gap = 6
    card_width = (CONTENT_W - (4 * card_gap)) / 5
    metrics = [
        ("01", "primary user"),
        ("0", "raw chats retained"),
        ("8", "first-session memories"),
        ("4/5", "behaviors transferred"),
        ("19/19", "tests passing"),
    ]
    for index, (value, text) in enumerate(metrics):
        metric_card(c, MARGIN + index * (card_width + card_gap), cards_top, card_width, value, text)

    y = cards_top - 68
    label(c, "01 / The product turn", MARGIN, y)
    y -= 15
    y = para(c, "I built the counter first. It exposed the better product.", MARGIN, y, 255, H2)
    para(
        c,
        "The hackathon version counted prompts, responses, copies, and corrections. "
        "That made activity visible, but activity was not the thing worth carrying between providers.",
        MARGIN + 280,
        y + 34,
        CONTENT_W - 280,
        BODY,
    )
    y -= 13
    c.setFillColor(ACID)
    c.rect(MARGIN, y - 43, CONTENT_W, 43, fill=1, stroke=0)
    label(c, "Product insight", MARGIN + 10, y - 13, INK)
    para(
        c,
        "<b>The useful unit is not a prompt. It is a reusable working rule:</b> how someone "
        "researches, what they verify, what they delegate, and what done means.",
        MARGIN + 112,
        y - 8,
        CONTENT_W - 124,
        style("insight", 8.6, 10.3, INK),
    )

    y -= 62
    col_gap = 20
    col_w = (CONTENT_W - col_gap) / 2
    label(c, "02 / User + job", MARGIN, y)
    label(c, "03 / MVP loop", MARGIN + col_w + col_gap, y)
    y -= 16
    left_y = para(c, "One user. One painful reset.", MARGIN, y, col_w, H2)
    right_y = para(c, "Five steps. One portable artifact.", MARGIN + col_w + col_gap, y, col_w, H2)

    left_y -= 9
    left_y = para(
        c,
        "<b>First user</b><br/>An individual whose LLM becomes more useful as it learns how they operate.",
        MARGIN,
        left_y,
        col_w,
        BODY,
    )
    left_y -= 8
    left_y = para(
        c,
        "<b>Job to be done</b><br/>When I change LLMs, bring how I work so I do not have to teach the new one from zero.",
        MARGIN,
        left_y,
        col_w,
        BODY,
    )
    left_y -= 8
    para(
        c,
        "<b>Why not teams first?</b><br/>Permissions and shared truth widen the system before the core transfer is proven.",
        MARGIN,
        left_y,
        col_w,
        BODY,
    )

    steps = [
        ("1", "Start", "Toggle the macOS menu app."),
        ("2", "Work", "Use the active LLM normally."),
        ("3", "Extract", "Request a strict memory patch."),
        ("4", "Validate", "Reject unsafe or invalid output."),
        ("5", "Move", "Export dataself-context.md."),
    ]
    sx = MARGIN + col_w + col_gap
    for number, heading, body in steps:
        c.setFillColor(INK)
        c.circle(sx + 7, right_y - 12, 7, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 5.6)
        c.setFillColor(ACID)
        c.drawCentredString(sx + 7, right_y - 14, number)
        para(c, f"<b>{heading}</b> - {body}", sx + 22, right_y - 5, col_w - 22, BODY)
        right_y -= 26

    y = min(left_y, right_y) - 27
    label(c, "04 / First three product decisions", MARGIN, y)
    y -= 12
    y = decision_row(
        c,
        y,
        "Behavioral rules",
        "Raw transcripts",
        "Portable and legible without retaining the most sensitive material.",
        "Less nuance.",
    )
    y = decision_row(
        c,
        y,
        "Active LLM extraction",
        "A second model",
        "The provider already has the session, so no second copy is needed.",
        "UI dependency.",
    )
    decision_row(
        c,
        y,
        "Local Markdown",
        "Cloud account",
        "The user can inspect, edit, move, or delete every memory.",
        "No sync.",
    )

    footer(c, 1)


def page_two(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    label(c, "DataSelf / Decisions, evidence, next test", MARGIN, PAGE_H - 35)
    c.setFillColor(ACID)
    c.rect(MARGIN, PAGE_H - 48, CONTENT_W, 4, fill=1, stroke=0)

    y = PAGE_H - 70
    label(c, "04 / Product decisions continued", MARGIN, y)
    y -= 12
    y = decision_row(
        c,
        y,
        "Automatic + provisional",
        "Approve every item",
        "A menu-bar tool cannot become another inbox; users can still edit or undo.",
        "Weak memory may appear.",
    )
    y = decision_row(
        c,
        y,
        "One context file",
        "Provider connectors",
        "Markdown works everywhere and made migration testable in one week.",
        "Manual first step.",
    )

    y -= 24
    col_gap = 18
    col_w = (CONTENT_W - col_gap) / 2
    label(c, "05 / Controlled migration test", MARGIN, y)
    label(c, "06 / Success metrics", MARGIN + col_w + col_gap, y)
    y -= 16
    left_y = para(c, "I tested behavior, not whether the file opened.", MARGIN, y, col_w, H2)
    right_y = para(c, "Success is less re-explanation.", MARGIN + col_w + col_gap, y, col_w, H2)

    left_y -= 10
    left_y = para(
        c,
        "Two fresh anonymous ChatGPT sessions received the same vague product request. "
        "One had no memory; one received DataSelf's context.",
        MARGIN,
        left_y,
        col_w,
        BODY,
    )
    left_y -= 10
    c.setFillColor(WHITE)
    c.setStrokeColor(LINE)
    c.rect(MARGIN, left_y - 61, col_w, 61, fill=1, stroke=1)
    label(c, "Without DataSelf", MARGIN + 8, left_y - 13)
    para(
        c,
        "Selected a direction, proposed a broad multi-week build, and asked several questions at once.",
        MARGIN + 8,
        left_y - 20,
        col_w - 16,
        BODY,
    )
    left_y -= 67
    c.setFillColor(ACID)
    c.rect(MARGIN, left_y - 61, col_w, 61, fill=1, stroke=1)
    label(c, "With DataSelf", MARGIN + 8, left_y - 13, INK)
    para(
        c,
        "Made no product assumption, asked one focused question, kept scope narrow, and reserved execution.",
        MARGIN + 8,
        left_y - 20,
        col_w - 16,
        style("pass", 8.1, 10.4, INK),
    )
    left_y -= 73
    para(
        c,
        "<b>Result: 4 of 5 behaviors transferred without correction.</b> The completion-handoff "
        "behavior was not exercised because the test stopped at definition.",
        MARGIN,
        left_y,
        col_w,
        LEAD,
    )

    metrics = [
        ("North star", "Less workflow re-explanation", "Outcome"),
        ("Known preferences", "At least 4 of 5", "Passed: 4/5"),
        ("Raw chat retained", "0 bytes", "Passed"),
        ("Evidence links", "100%", "Passed"),
        ("First update", "Under 10 minutes", "Unproven"),
        ("Corrective messages", "Below baseline", "Next test"),
    ]
    mx = MARGIN + col_w + col_gap
    for metric, target, status in metrics:
        c.setStrokeColor(LINE)
        c.line(mx, right_y, mx + col_w, right_y)
        label(c, metric, mx, right_y - 12)
        para(c, f"<b>{target}</b>", mx + 106, right_y - 5, 105, BODY)
        para(c, status, mx + col_w - 65, right_y - 5, 65, SMALL)
        right_y -= 32
    c.line(mx, right_y, mx + col_w, right_y)

    y = min(left_y - 40, right_y - 28)
    c.setFillColor(NIGHT)
    c.rect(0, 0, PAGE_W, y, fill=1, stroke=0)
    label(c, "07 / What is proven - and what is not", MARGIN, y - 20, HexColor("#aeb0a7"))

    dark_top = y - 38
    dark_left_y = para(
        c,
        "Built evidence is not market evidence.",
        MARGIN,
        dark_top,
        col_w,
        H2_LIGHT,
    )
    dark_left_y -= 9
    para(
        c,
        "The prototype proves that behavioral memory can transfer. It does not prove that "
        "enough people feel the reset, trust automatic extraction, or keep using the system.",
        MARGIN,
        dark_left_y,
        col_w,
        BODY_DARK,
    )

    nx = MARGIN + col_w + col_gap
    para(c, "<b>Next experiment</b>", nx, dark_top, col_w, H3_LIGHT)
    para(
        c,
        "Five heavy LLM users, three sessions each. Measure setup time, memory edit/deletion "
        "rate, corrective messages with and without context, and repeat migration.",
        nx,
        dark_top - 18,
        col_w,
        BODY_DARK,
    )
    para(c, "<b>Risks to watch</b>", nx, dark_top - 76, col_w, H3_LIGHT)
    para(
        c,
        "Provider UI churn / confident but wrong memory / context growth becoming noise / "
        "convenience mattering more than portability.",
        nx,
        dark_top - 94,
        col_w,
        BODY_DARK,
    )

    label(
        c,
        "Product definition  /  prioritization  /  privacy  /  prototyping  /  experiment design  /  metrics",
        MARGIN,
        y - 174,
        ACID,
    )

    footer(c, 2)


def build():
    c = canvas.Canvas(str(OUTPUT), pagesize=letter)
    c.setTitle("DataSelf - Product Case Study")
    c.setAuthor("Naman Dhankhar")
    c.setSubject("Two-page APM product case study")
    page_one(c)
    c.showPage()
    page_two(c)
    c.showPage()
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
