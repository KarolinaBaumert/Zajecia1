import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Student\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def read_text_with_opencv(image_path):
    try:
        img = cv2.imread(image_path)

        if img is None:
            raise FileNotFoundError(f"Nie można wczytać obrazu: {image_path}")

        scale_percent = 150
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

        processed = cv2.adaptiveThreshold(
            denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )

        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed, config=custom_config, lang="eng")

        return text

    except FileNotFoundError as fnfe:
        return f"Błąd: {fnfe}"
    except Exception as e:
        return f"Wystąpił błąd: {e}"


if __name__ == "__main__":
    input_paths = r"C:\Users\Student\Desktop\Judy.jpg,C:\Users\Student\Desktop\cos2.jfif,C:\Users\Student\Desktop\cos3.jpg,C:\Users\Student\Desktop\cos4.jpg,C:\Users\Student\Desktop\cos5.jfif"

    image_paths = [path.strip() for path in input_paths.split(",")]

    for path in image_paths:
        print(f"\nPrzetwarzanie obrazu: {path}")
        result = read_text_with_opencv(path)
        print("Odczytany tekst:")
        print(result)
