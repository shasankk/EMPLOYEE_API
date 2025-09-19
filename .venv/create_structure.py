import os

folders = [
    "employee_api/app/api/v1/endpoints",
    "employee_api/app/core",
    "employee_api/app/models",
    "employee_api/app/repositories",
    "employee_api/app/services",
    "employee_api/app/schemas",
    "employee_api/app/utils",
]

files = {
    "employee_api/app/main.py": "",
    "employee_api/app/api/v1/endpoints/auth.py": "",
    "employee_api/app/api/v1/endpoints/employee.py": "",
    "employee_api/app/core/config.py": "",
    "employee_api/app/core/database.py": "",
    "employee_api/app/core/logger.py": "",
    "employee_api/app/core/middleware.py": "",
    "employee_api/app/core/security.py": "",
    "employee_api/app/models/user.py": "",
    "employee_api/app/models/employee.py": "",
    "employee_api/app/repositories/user_repository.py": "",
    "employee_api/app/repositories/employee_repository.py": "",
    "employee_api/app/services/auth_service.py": "",
    "employee_api/app/services/employee_service.py": "",
    "employee_api/app/schemas/employee.py": "",
    "employee_api/app/schemas/user.py": "",
    "employee_api/app/schemas/token.py": "",
    "employee_api/app/utils/response.py": "",
    "employee_api/docker-compose.yml": "",
    "employee_api/Dockerfile": "",
    "employee_api/requirements.txt": "",
    "employee_api/.env.example": "",
    "employee_api/employee_api.postman_collection.json": "",
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file, content in files.items():
    with open(file, "w") as f:
        f.write(content)

print("✅ Project structure created!")
