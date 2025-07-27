import cv2
import os

video_path = "your_video_url"  # 다운로드한 영상 경로
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ 영상 열기에 실패했습니다.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)  # 프레임 속도 (ex: 30.0)
frame_interval = int(fps)        # 1초마다 저장 = fps만큼 건너뜀

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()
cv2.destroyAllWindows()
print(f"✅ 총 {saved_count}개의 프레임이 저장되었습니다.")

