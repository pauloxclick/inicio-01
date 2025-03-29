FROM python:3.11  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
COPY . .  
CMD ["python", "app.py"]
# Expose the port the app runs on