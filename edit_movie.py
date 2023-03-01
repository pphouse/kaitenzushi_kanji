import cv2

# 入力動画の読み込み
cap = cv2.VideoCapture("iRPReplay_Final1677630031 2.mp4")

# 出力動画の作成
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, cap.get(cv2.CAP_PROP_FPS), (2778, 1284))

# フレームごとにループ処理
while cap.isOpened():
    # フレームの読み込み
    ret, frame = cap.read()

    if ret:
        # 解像度の変更
        frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_CUBIC)

        # 変換されたフレームを書き込み
        out.write(frame)

        # 表示
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# 終了処理
cap.release()
out.release()
cv2.destroyAllWindows()
