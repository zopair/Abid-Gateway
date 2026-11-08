from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

W, H = 1280, 720
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "frames"
OUT.mkdir(exist_ok=True)
FONT = "/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf"
BOLD = "/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf"
LATIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LATIN_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(size, bold=False, latin=False):
    path = (LATIN_B if bold else LATIN) if latin else (BOLD if bold else FONT)
    return ImageFont.truetype(path, size)

def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def text(draw, xy, value, size=24, color="#fff", bold=False, anchor="mm", latin=False):
    draw.text(xy, value, font=font(size, bold, latin), fill=color, anchor=anchor,
              direction=None if latin else "rtl", language=None if latin else "ar")

def background(kicker, title, subtitle):
    image = Image.new("RGB", (W, H), (10, 12, 24))
    pixels = image.load()
    for y in range(H):
        for x in range(W):
            glow = max(0, 1 - math.sqrt(((x - 930) / 850) ** 2 + ((y - 40) / 650) ** 2))
            pixels[x, y] = (int(10 + 24 * glow), int(12 + 7 * glow), int(28 + 55 * glow))
    draw = ImageDraw.Draw(image)
    for x in range(0, W, 80):
        draw.line((x, 0, x, H), fill=(22, 24, 43), width=1)
    for y in range(0, H, 80):
        draw.line((0, y, W, y), fill=(22, 24, 43), width=1)
    rounded(draw, (72, 68, 370, 112), 20, "#2b2058", "#5b45a0")
    text(draw, (221, 90), kicker, 18, "#e8dcff", True, latin=True)
    text(draw, (W - 72, 190), title, 48, "#ffffff", True, "ra")
    text(draw, (W - 72, 265), subtitle, 24, "#c6c5d8", False, "ra")
    return image, draw

def phone(draw, y=330):
    x0, y0, x1, y1 = 115, y, 500, y + 340
    rounded(draw, (x0, y0, x1, y1), 34, "#f8fafc", "#ffffff", 3)
    rounded(draw, (x0, y0, x1, y0 + 72), 32, "#4b248c")
    draw.rectangle((x0, y0 + 38, x1, y0 + 72), fill="#4b248c")
    rounded(draw, (x0 + 20, y0 + 18, x0 + 202, y0 + 52), 10, "#f97316")
    text(draw, (x0 + 111, y0 + 35), "Insta Freelancer", 17, "#fff", True, latin=True)
    text(draw, (x1 - 20, y0 + 36), "علي حسين فكري", 13, "#fff", True, "ra")
    return x0, y0, x1, y1

def scene0():
    image, draw = background("INSTA FREELANCER / DEMO", "حل أبسط لاستلام عائدات العمل الحر",
        "تصور واجهة موبايل يربط مستحقات العمل الحر بالدورة المصرفية المحلية")
    x0, y0, x1, y1 = phone(draw, 320)
    rounded(draw, (x0 + 20, y0 + 88, x1 - 20, y0 + 180), 18, "#ffffff", "#e5e7eb")
    text(draw, (x1 - 40, y0 + 110), "حساب العمل الحر الدولي", 17, "#475569", True, "ra")
    text(draw, (x1 - 40, y0 + 151), "$1,250.00", 30, "#172554", True, "ra", True)
    rounded(draw, (x0 + 20, y0 + 195, x1 - 20, y0 + 305), 18, "#182b54")
    text(draw, (x1 - 42, y0 + 220), "تحويل مستحقاتك إلى الجنيه", 17, "#dbeafe", True, "ra")
    text(draw, (x1 - 42, y0 + 267), "49.20 EGP لكل دولار", 22, "#fff", True, "ra", True)
    text(draw, (W - 72, 390), "منصة عرض توضيحي", 18, "#fbbf24", True, "ra")
    return image

def scene1():
    image, draw = background("01 / HOME", "واجهة مألوفة وسهلة",
        "الحساب الأساسي والخدمات اليومية في شاشة واحدة")
    x0, y0, x1, y1 = phone(draw, 300)
    rounded(draw, (x0 + 18, y0 + 88, x1 - 18, y0 + 183), 18, "#ffffff", "#e5e7eb")
    text(draw, (x1 - 38, y0 + 111), "الحساب الأساسي - البنك الأهلي المصري", 14, "#475569", True, "ra")
    text(draw, (x1 - 38, y0 + 153), "48,250.00 EGP", 22, "#172554", True, "ra", True)
    rounded(draw, (x0 + 18, y0 + 195, x1 - 18, y0 + 255), 15, "#1e2f59")
    text(draw, (x1 - 35, y0 + 225), "إرسال نقود    طلب دفع    دفع فواتير", 14, "#fff", True, "ra")
    rounded(draw, (x0 + 18, y0 + 268, x1 - 18, y0 + 322), 14, "#ffffff")
    text(draw, (x1 - 35, y0 + 295), "آخر المعاملات - حوالة دولارية واردة", 14, "#334155", True, "ra")
    return image

def scene2():
    image, draw = background("02 / GLOBAL FREELANCE", "مستحقاتك الدولية بالدولار",
        "رصيد العمل الحر ظاهر بوضوح مع بيانات الحساب الافتراضي")
    x0, y0, x1, y1 = phone(draw, 300)
    rounded(draw, (x0 + 18, y0 + 88, x1 - 18, y0 + 320), 20, "#101f43", "#334e83", 2)
    rounded(draw, (x0 + 36, y0 + 106, x0 + 160, y0 + 136), 9, "#2563eb")
    text(draw, (x0 + 98, y0 + 121), "ميزة جديدة", 13, "#fff", True)
    text(draw, (x1 - 38, y0 + 160), "حساب العمل الحر الدولي", 16, "#dbeafe", True, "ra")
    text(draw, (x1 - 38, y0 + 214), "$1,250.00", 36, "#ffffff", True, "ra", True)
    text(draw, (x1 - 38, y0 + 238), "رقم الحساب الافتراضي", 12, "#cbd5e1", False, "ra")
    text(draw, (x1 - 38, y0 + 260), "EG38NBE0000001294821", 12, "#cbd5e1", False, "ra", True)
    text(draw, (x1 - 38, y0 + 287), "سعر الصرف", 12, "#bfdbfe", True, "ra")
    text(draw, (x0 + 42, y0 + 287), "1 USD = 49.20 EGP", 12, "#bfdbfe", True, "la", True)
    return image

def scene3():
    image, draw = background("03 / CONVERSION", "تحويل واضح بخطوة واحدة",
        "محاكاة حسابية توضح قيمة المستحقات بالجنيه المصري")
    rounded(draw, (100, 330, 1180, 575), 28, "#121f3c", "#334e83", 2)
    text(draw, (640, 380), "الرصيد بالدولار", 20, "#cbd5e1", True)
    text(draw, (640, 430), "$1,250.00", 46, "#ffffff", True, latin=True)
    text(draw, (640, 485), "× 49.20 EGP", 28, "#fbbf24", True, latin=True)
    draw.line((270, 525, 1010, 525), fill="#52658d", width=2)
    text(draw, (640, 552), "61,500.00 EGP", 42, "#86efac", True, latin=True)
    rounded(draw, (400, 605, 880, 660), 18, "#f97316")
    text(draw, (640, 632), "تحويل وإيداع في الحساب الأساسي", 19, "#ffffff", True)
    return image

def scene4():
    image, draw = background("04 / THE PROPOSAL", "تجربة أبسط للمستقل المصري",
        "تصور مقترح لتيسير تدفق عائدات العمل الحر للمستقل المصري")
    rounded(draw, (100, 340, 1180, 575), 28, "#171b32", "#5b45a0", 2)
    text(draw, (640, 405), "حساب أساسي بالجنيه  +  حساب عمل حر بالدولار", 30, "#ffffff", True)
    text(draw, (640, 475), "خدمات سريعة  -  سجل معاملات  -  تحويل بسعر صرف معروض", 21, "#d7d5e7", True)
    text(draw, (640, 535), "واجهة تجريبية للعرض — الأرصدة وأسعار الصرف افتراضية", 17, "#fbbf24", True)
    text(draw, (640, 635), "INSTA FREELANCER", 26, "#ffffff", True, latin=True)
    return image

scenes = [scene0(), scene1(), scene2(), scene3(), scene4()]
for index, image in enumerate(scenes):
    image.save(OUT / f"scene_{index:02d}.png")
print(f"Rendered {len(scenes)} demo scenes")
