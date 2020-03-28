import cv2
import urllib.request as req
import matplotlib.pyplot as plt

# 練習2 画像データの編集
#　画像の保存
# cv2.imwrite
# 第一引数: 保存後のファイル名
# 第二引数: 画像オブジェクト

# 読み込み
img1 = cv2.imread("opencv/face.jpg")

# 画像のリサイズ
# cv2.resize()
# 第一引数: 画像のオブジェクト
# 第二引数: 返還後のサイズ(横 * 縦)

# リサイズ
img1_2 = cv2.resize(img1, (100, 100))
# 保存
cv2.imwrite("opencv/face2.jpg", img1_2)

# 画像の切り取り
# 配列のスライシングを利用する

# 切り取り
img1_3 = img1[20:170, 50:150]

# サイズを変更
img1_3 = cv2.resize(img1_3, (100, 150))

# 保存
cv2.imwrite("face3.jpg", img1_3)

# 表示
plt.imshow(cv2.cvtColor(img1_3, cv2.COLOR_BGR2RGB))
plt.show()


