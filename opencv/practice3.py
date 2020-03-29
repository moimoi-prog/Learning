import matplotlib.pyplot as plt
import cv2
import os
import utils.ImageUtils as iu

# 顔にモザイクをかける

# 検出器を生成
# カスケードファイルを生成
cascade_file = "../download/haarcascade_frontalface_alt.xml"
# カスケードインスタンスを生成
cascade = cv2.CascadeClassifier(cascade_file)

# 画像をグレイスケールに変換
img = cv2.imread("subaru.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 顔認識を実行
face_list = cascade.detectMultiScale(img_gray)

# 結果を確認
if len(face_list) == 0:
    print("失敗")
    quit()

# 認識した部分に印をつける
for (x, y, w, h) in face_list:
    img = iu.mosaic(img, (x, y, x + w, y + h), 10)

# 画像を出力
cv2.imwrite("opencv/face_match.jpg", img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
