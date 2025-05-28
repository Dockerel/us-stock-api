# Python 베이스 이미지 선택
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Python 앱 실행
CMD ["python", "app/main.py"]