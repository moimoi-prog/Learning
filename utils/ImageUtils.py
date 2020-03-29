import cv2


# モザイクをかける
# 第一引数: 画像データ
# 第二引数: 座標データ(始点x, 始点y, 終点x, 終点y)
# 第三引数: モザイク大きさ
def mosaic(img, rect, size):
    # モザイクをかける領域を取得
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]

    # モザイクを作成する
    # 生成ロジック
    # 縮小して拡大
    i_small = cv2.resize(i_rect, (size, size))
    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)

    # 画面にモザイクを重ねる
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2
