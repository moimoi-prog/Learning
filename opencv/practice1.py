import cv2
import urllib.request as req
import matplotlib.pyplot as plt

# 練習１ 画像データのダウンロードと表示
# urllib ... URLを扱うモジュール群
# https://docs.python.org/ja/3/library/urllib.html
# urlretrieve ... urlで示すオブジェクトをローカルに保存する

# 画像のダウンロード
url = "http://uta.pw/shodou/img/28/214.png"
req.urlretrieve(url, "test.png")

# cv2.imread() ... 画像ファイルを読み込み
# 第二引数に[cv2.IMREAD_GRAYSCALE]を指定すると
# グレースケールで表示される。
img = cv2.imread("face.jpg")
img2 = cv2.imread("face.jpg", cv2.IMREAD_GRAYSCALE)

# 画像を表示
# cvtColor 第二引数...OpenCV(BGR) → matplotlib(RGB)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


