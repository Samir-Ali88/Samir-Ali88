import datetime

USER = "Samir-Ali88"
OUTPUT_FILE = "dist/mario-graph.svg"
DAYS = 7 * 10
BLOCK_SIZE = 12
MARIO_SIZE = 14

commits = [0,1,2,0,3,0,1]*10

def block_color(count):
    if count == 0:
        return "#ebedf0"
    elif count == 1:
        return "#9be9a8"
    elif count == 2:
        return "#40c463"
    else:
        return "#30a14e"

svg = []
svg.append(f'<svg width="{DAYS*BLOCK_SIZE+20}" height="{BLOCK_SIZE*7+40}" xmlns="http://www.w3.org/2000/svg">')

for i, count in enumerate(commits):
    x = i * BLOCK_SIZE + 10
    y = (i % 7) * BLOCK_SIZE + 10
    color = block_color(count)
    svg.append(f'<rect x="{x}" y="{y}" width="{BLOCK_SIZE}" height="{BLOCK_SIZE}" fill="{color}" rx="2" ry="2"/>')

mario_x = 10
mario_y = 10
svg.append(f'<rect x="{mario_x}" y="{mario_y}" width="{MARIO_SIZE}" height="{MARIO_SIZE}" fill="red"/>')

svg.append('</svg>')

with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(svg))
