import pyzbar.pyzbar as pyzbar
import cv2
import time

# 바코드가 포함된 이미지 경로
image_path = "C:\\Users\\min12\\Desktop\\barcode_catalog_4.png"

# 이미지 로드
img = cv2.imread(image_path)
if img is None:
    print("Error: Cannot load the image.")
    exit()

# 그레이스케일 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 바코드 디코딩 및 시간 측정
start_time = time.time_ns()
decoded = pyzbar.decode(gray)
end_time = time.time_ns()

# 결과 처리
found = False
for d in decoded:
    barcode_data = d.data.decode("utf-8")
    if barcode_data == "54314eeee":
        found = True
        x, y, w, h = d.rect

        print(f"Barcode Data: {barcode_data}")
        print(f"Coordinates: Top-left ({x}, {y}), Width: {w}, Height: {h}")
        print(f"Corners: ({x}, {y}), ({x+w}, {y}), ({x}, {y+h}), ({x+w}, {y+h})")
        break

if not found:
    print("Barcode '54314eeee' not found in the image.")

# 시간 출력
elapsed_time_ns = end_time - start_time
print(f"Processing Time: {elapsed_time_ns} ns")

# 결과 이미지 출력
if found:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, "54314eeee", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
