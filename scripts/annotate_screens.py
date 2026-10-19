import sys; sys.path.insert(0, "scripts")
from annolib import annotate
from PIL import Image
S, O = "assets/screens/", "assets/annotated/"

# 1. Головне меню
annotate(S + "001.jpg", O + "ui-main-menu.jpg", [
    dict(n=1, box=(55, 40, 505, 70), tag=(30, 25)),
    dict(n=2, box=(56, 72, 268, 157), tag=(30, 115)),
    dict(n=3, box=(56, 158, 505, 590), tag=(30, 400)),
    dict(n=4, box=(62, 596, 165, 622), tag=(30, 650)),
    dict(n=5, box=(385, 596, 505, 622), tag=(500, 650)),
])
# 2. Рядок заголовка (збільшено)
im = Image.open(S + "001.jpg").crop((50, 36, 515, 76)); im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS); im.save(O + "_tb.png")
annotate(O + "_tb.png", O + "ui-title-bar.jpg", [
    dict(n=1, box=(30, 12, 440, 100), tag=(60, 200)),
    dict(n=2, box=(560, 12, 660, 100), tag=(610, 200)),
    dict(n=3, box=(660, 12, 745, 100), tag=(700, 200)),
    dict(n=4, box=(745, 12, 835, 100), tag=(790, 200)),
    dict(n=5, box=(835, 12, 920, 100), tag=(880, 200)),
    dict(n=6, box=(920, 12, 1010, 100), tag=(965, 200)),
    dict(n=7, box=(1010, 12, 1070, 100), tag=(1040, 200)),
    dict(n=8, box=(1070, 12, 1130, 100), tag=(1100, 200)),
    dict(n=9, box=(1130, 12, 1190, 100), tag=(1160, 200)),
    dict(n=10, box=(1190, 12, 1255, 100), tag=(1225, 200)),
])
# 3. Приймач (Scanner)
annotate(S + "033.jpg", O + "ui-receiver-scanner.jpg", [
    dict(n=1, box=(65, 42, 500, 68), tag=(25, 55)),
    dict(n=2, box=(65, 73, 500, 98), tag=(25, 85)),
    dict(n=3, box=(65, 100, 500, 127), tag=(25, 115)),
    dict(n=4, box=(65, 127, 240, 146), tag=(25, 140)),
    dict(n=5, box=(408, 140, 500, 228), tag=(375, 185)),
    dict(n=6, box=(65, 238, 500, 336), tag=(30, 290)),
    dict(n=7, box=(62, 362, 500, 440), tag=(30, 400)),
    dict(n=8, box=(62, 455, 500, 482), tag=(30, 470)),
    dict(n=9, box=(60, 493, 500, 625), tag=(30, 560)),
])
# 4. Передавач (POCSAG TX)
annotate(S + "066.jpg", O + "ui-transmitter-pocsag.jpg", [
    dict(n=1, box=(65, 128, 505, 158), tag=(30, 143)),
    dict(n=2, box=(60, 215, 410, 330), tag=(30, 270)),
    dict(n=3, box=(58, 372, 270, 512), tag=(30, 440)),
    dict(n=4, box=(85, 545, 475, 582), tag=(500, 520)),
    dict(n=5, box=(65, 650, 370, 680), tag=(30, 625)),
    dict(n=6, box=(55, 682, 340, 710), tag=(30, 735)),
    dict(n=7, box=(370, 650, 505, 712), tag=(470, 740)),
])
# 5. Приймач із списком (SubGhzD)
annotate(S + "028.jpg", O + "ui-receiver-list-subghzd.jpg", [
    dict(n=1, box=(68, 135, 500, 162), tag=(40, 115)),
    dict(n=2, box=(68, 164, 215, 188), tag=(40, 200)),
    dict(n=3, box=(245, 164, 350, 188), tag=(300, 215)),
    dict(n=4, box=(358, 160, 420, 175), tag=(450, 200)),
    dict(n=5, box=(68, 195, 165, 238), tag=(40, 270)),
    dict(n=6, box=(205, 190, 285, 222), tag=(310, 250)),
    dict(n=7, box=(68, 237, 495, 268), tag=(40, 300)),
])
