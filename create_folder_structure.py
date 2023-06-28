import os

def create_folder(path):
    try:
        os.makedirs(path)
        print(f"Created folder: {path}")
    except FileExistsError:
        print(f"Folder already exists: {path}")

# Запрос пути к папке проекта
project_folder = input("Enter the path to the project folder: ")

# Запрос названия проекта
project_name = input("Enter the project name: ")

# Создание папки проекта
project_path = os.path.join(project_folder, project_name)
create_folder(project_path)

# Создание папки приложения
app_path = os.path.join(project_path, "app")
create_folder(os.path.join(app_path, "static"))
create_folder(os.path.join(app_path, "templates"))

# Создание папки конфигурации
create_folder(os.path.join(project_path, "config"))

# Создание папки базы данных и миграций
db_path = os.path.join(project_path, "db")
create_folder(os.path.join(db_path, "migrations"))

# Создание папки для тестов
create_folder(os.path.join(project_path, "tests"))

# Создание папки для виртуальной среды
create_folder(os.path.join(project_path, "venv"))

# Создание файла requirements.txt
requirements_path = os.path.join(project_path, "requirements.txt")
with open(requirements_path, "w") as requirements_file:
    requirements_file.write("Flask\n")  # Пример зависимости, добавьте необходимые пакеты

print("Folder structure created successfully.")

