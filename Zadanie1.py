import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Student\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def read_text_with_opencv(image_path):
    try:
        img = cv2.imread(image_path)

        if img is None:
            raise FileNotFoundError(f"Nie można wczytać obrazu: {image_path}")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        processed = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )

        text = pytesseract.image_to_string(processed, lang="eng")
        return text

    except FileNotFoundError as fnfe:
        return f"Błąd: {fnfe}"
    except Exception as e:
        return f"Wystąpił błąd: {e}"


if __name__ == "__main__":
    image_path = r"C:\Users\Student\Desktop\Judy.jpg"
    result = read_text_with_opencv(image_path)
    print("Odczytany tekst:")
    print(result)
