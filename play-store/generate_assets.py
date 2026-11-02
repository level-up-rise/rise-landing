from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

out_dir = Path(__file__).resolve().parent
out_dir.mkdir(parents=True, exist_ok=True)

src = Image.open(
    Path(r"C:\Users\kevin\Documents\GitHub\level-up-your-day\android\app\src\main\res\mipmap-xxxhdpi\ic_launcher_foreground.png")
).convert("RGBA")

# --- Play icon 512x512 ---
icon = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
draw = ImageDraw.Draw(icon)
for i in range(-512, 512, 18):
    draw.line([(i, 0), (i + 512, 512)], fill=(230, 236, 242, 255), width=1)
    draw.line([(i, 512), (i + 512, 0)], fill=(230, 236, 242, 255), width=1)

logo = src.copy()
bbox = logo.getbbox()
if bbox:
    logo = logo.crop(bbox)
max_side = int(512 * 0.68)
ratio = min(max_side / logo.width, max_side / logo.height)
logo = logo.resize(
    (max(1, int(logo.width * ratio)), max(1, int(logo.height * ratio))),
    Image.Resampling.LANCZOS,
)
x = (512 - logo.width) // 2
y = (512 - logo.height) // 2
icon.alpha_composite(logo, (x, y))
icon_path = out_dir / "play-icon-512.png"
icon.convert("RGB").save(icon_path, "PNG", optimize=True)
print("icon", icon_path, icon_path.stat().st_size)

# --- Feature graphic 1024x500 ---
W, H = 1024, 500
fg = Image.new("RGBA", (W, H), (10, 7, 18, 255))

glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gdraw = ImageDraw.Draw(glow)
gdraw.ellipse([520, -180, 1180, 480], fill=(168, 85, 247, 70))
gdraw.ellipse([-120, 200, 420, 700], fill=(94, 200, 232, 35))
glow = glow.filter(ImageFilter.GaussianBlur(60))
fg = Image.alpha_composite(fg, glow)

overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for x0 in range(0, W, 48):
    od.line([(x0, 0), (x0, H)], fill=(168, 85, 247, 22), width=1)
for y0 in range(0, H, 48):
    od.line([(0, y0), (W, y0)], fill=(168, 85, 247, 18), width=1)
fg = Image.alpha_composite(fg, overlay)

font_bold = r"C:\Windows\Fonts\segoeuib.ttf"
font_reg = r"C:\Windows\Fonts\segoeui.ttf"
if not Path(font_bold).exists():
    font_bold = r"C:\Windows\Fonts\arialbd.ttf"
if not Path(font_reg).exists():
    font_reg = font_bold


def load(path: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


title = load(font_bold, 96)
subtitle = load(font_bold, 36)
tag = load(font_reg, 28)
eyebrow = load(font_bold, 22)

draw = ImageDraw.Draw(fg)
draw.text((64, 88), "HUNTER TRAINING SYSTEM", fill=(168, 85, 247, 255), font=eyebrow)
draw.text((64, 150), "RISE", fill=(243, 238, 252, 255), font=title)
draw.text((64, 265), "HUNTER", fill=(94, 200, 232, 255), font=subtitle)
draw.text((64, 340), "Level up in real life.", fill=(154, 143, 179, 255), font=tag)
draw.rectangle([64, 320, 220, 323], fill=(232, 197, 71, 200))

def extract_blue_mark(img: Image.Image) -> Image.Image:
    """Keep cyan/blue logo pixels; drop white/light background."""
    rgba = img.convert("RGBA")
    px = rgba.load()
    w, h = rgba.size
    for yy in range(h):
        for xx in range(w):
            r, g, b, a = px[xx, yy]
            # keep vivid cyan/blue mark, kill pale bg
            if a < 10:
                continue
            if r > 200 and g > 200 and b > 200:
                px[xx, yy] = (0, 0, 0, 0)
            elif b > 140 and b >= r and (b - r) > 20:
                px[xx, yy] = (117, 197, 255, 255)
            elif max(r, g, b) < 40:
                px[xx, yy] = (0, 0, 0, 0)
            else:
                # soft grid / leftovers
                if r > 180 and g > 180 and b > 180:
                    px[xx, yy] = (0, 0, 0, 0)
    box = rgba.getbbox()
    return rgba.crop(box) if box else rgba


mark = extract_blue_mark(src)
max_side = 280
ratio = min(max_side / mark.width, max_side / mark.height)
mark = mark.resize(
    (max(1, int(mark.width * ratio)), max(1, int(mark.height * ratio))),
    Image.Resampling.LANCZOS,
)

lg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
lgd = ImageDraw.Draw(lg)
cx, cy = 820, 250
lgd.ellipse([cx - 180, cy - 180, cx + 180, cy + 180], fill=(117, 197, 255, 40))
lg = lg.filter(ImageFilter.GaussianBlur(40))
fg = Image.alpha_composite(fg, lg)
mx = cx - mark.width // 2
my = cy - mark.height // 2
fg.alpha_composite(mark, (mx, my))

feat_path = out_dir / "play-feature-1024x500.png"
fg.convert("RGB").save(feat_path, "PNG", optimize=True)
print("feature", feat_path, feat_path.stat().st_size)
print("done")
