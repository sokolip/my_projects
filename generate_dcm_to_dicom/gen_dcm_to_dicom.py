import os
from dotenv import load_dotenv
load_dotenv()

# Указываем путь к папке с файлами и папку для новых файлов
source_folder = os.getenv("SOURCE_FOLDER")
destination_folder = os.getenv("DESTINATION_FOLDER")

# Создаем новую папку, если она не существует
os.makedirs(destination_folder, exist_ok=True)
print("Преобразование начато")
# Проходим по всем файлам в папке
for filename in os.listdir(source_folder):
    if filename.endswith(".dcm"):  # Проверяем, что файл имеет нужное расширение
        old_path = os.path.join(source_folder, filename)
        new_filename = os.path.splitext(filename)[0] + ".dicom"
        new_path = os.path.join(destination_folder, new_filename)
        with open(old_path, "rb") as src, open(new_path, "wb") as dst:
            dst.write(src.read())

print("Преобразование завершено.")
