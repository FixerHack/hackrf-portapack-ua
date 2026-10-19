import sys; sys.path.insert(0, "scripts")
from annolib import annotate
P, O = "assets/photos/", "assets/annotated/"
annotate(P + "device-side-clk-usb.jpg", O + "device-side-clk-usb.jpg", [
    dict(n=1, box=(405, 490, 540, 610), tag=(470, 700)),
    dict(n=2, box=(605, 490, 725, 610), tag=(665, 700)),
    dict(n=3, box=(830, 510, 945, 565), tag=(888, 640)),
    dict(n=4, box=(925, 420, 1010, 495), tag=(1080, 470)),
    dict(n=5, box=(535, 285, 660, 355), tag=(450, 240)),
])
annotate(P + "device-front.jpg", O + "device-front.jpg", [
    dict(n=1, box=(240, 285, 810, 690), tag=(520, 790)),
    dict(n=2, box=(835, 255, 1035, 430), tag=(1100, 300)),
    dict(n=3, box=(845, 510, 1025, 700), tag=(1100, 740)),
    dict(n=4, box=(0, 600, 215, 700), tag=(110, 780)),
    dict(n=5, box=(1115, 490, 1155, 650), tag=(1210, 570)),
    dict(n=6, box=(365, 232, 765, 268), tag=(560, 160)),
])
annotate(P + "device-side-ant-sd.jpg", O + "device-side-ant-sd.jpg", [
    dict(n=1, box=(355, 372, 515, 408), tag=(300, 330)),
    dict(n=2, box=(358, 440, 412, 492), tag=(300, 560)),
    dict(n=3, box=(447, 488, 474, 512), tag=(440, 620)),
    dict(n=4, box=(500, 440, 552, 492), tag=(540, 590)),
    dict(n=5, box=(578, 486, 806, 514), tag=(700, 640)),
    dict(n=6, box=(855, 435, 990, 540), tag=(1070, 600)),
])
