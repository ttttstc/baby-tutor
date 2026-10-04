import sys, os
import pymupdf

# usage: python render.py <pdf> <start> <end> <outdir> [dpi]
pdf = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
outdir = sys.argv[4]
dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 150
os.makedirs(outdir, exist_ok=True)

doc = pymupdf.open(pdf)
zoom = dpi / 72.0
mat = pymupdf.Matrix(zoom, zoom)
for p in range(start, end + 1):
    page = doc[p - 1]
    pix = page.get_pixmap(matrix=mat, colorspace=pymupdf.csRGB)
    out = os.path.join(outdir, f"p{p:04d}.png")
    pix.save(out)
    print(out)
print("DONE", end - start + 1, "pages")
