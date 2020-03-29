import cv2
import matplotlib.pyplot as plt

# 画像の輪郭を抽出する

# 画像の読み込み
img = cv2.imread("../images/eievui.jpg")

# 色空間を二値化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
