FROM python:3.7.12

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the Django application files
COPY . .

# Grant executable permissions to django.sh
COPY django.sh .
RUN chmod +x django.sh

EXPOSE 8000

ENTRYPOINT ["./django.sh"]
