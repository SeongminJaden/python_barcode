import cv2
import subprocess
import time
from pyzbar.pyzbar import decode
import numpy as np

# 시간 측정 시작
start_time = time.time()

# 1. gphoto2 명령어로 카메라에서 이미지 캡처
capture_start_time = time.time()
subprocess.run(["gphoto2", "--capture-image-and-download", "--filename", "captured_image.jpg"], check=True)
capture_end_time = time.time()

# 2. 이미지 로드
image_load_start_time = time.time()
image = cv2.imread("captured_image.jpg")
image_load_end_time = time.time()

# 3. 바코드 인식
barcode_start_time = time.time()
barcodes = decode(image)
barcode_end_time = time.time()

# 4. 바코드가 인식된 경우 처리
for barcode in barcodes:
    barcode_data = barcode.data.decode("utf-8")
    barcode_type = barcode.type
    print(f"Detected {barcode_type} barcode: {barcode_data}")

    # 바코드 위치를 이미지에 표시
    rect_points = barcode.polygon
    if len(rect_points) == 4:
        pts = np.array(rect_points, dtype="int32")
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 2)

    # 바코드 데이터 텍스트 추가
    x, y, w, h = barcode.rect
    cv2.putText(image, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 결과 이미지 출력
cv2.imshow("Barcode Scanner", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 전체 소요 시간
end_time = time.time()

# 각 단계별 소요 시간 출력
print(f"Time taken for image capture: {capture_end_time - capture_start_time:.2f} seconds")
print(f"Time taken for image loading: {image_load_end_time - image_load_start_time:.2f} seconds")
print(f"Time taken for barcode decoding: {barcode_end_time - barcode_start_time:.2f} seconds")
print(f"Total time taken: {end_time - start_time:.2f} seconds")
