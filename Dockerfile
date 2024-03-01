FROM python:3.10

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar las pruebas unitarias
RUN python tests/testing.py

CMD ["python", "main.py"]
