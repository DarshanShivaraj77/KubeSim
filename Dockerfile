FROM python:3.8-slim
WORKDIR /app
COPY node.py .
RUN pip install requests
CMD ["python3", "node.py"]

