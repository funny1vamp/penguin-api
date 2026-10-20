FROM python:3.11-slim
WORKDIR /app

# 直接用 pip 安装你需要的包，版本号和你在本地测试时一致
RUN pip install --no-cache-dir fastapi[standard] pandas joblib scikit-learn==1.6.1

# 复制代码和模型
COPY main.py model.joblib index.html ./

EXPOSE 8000

# 直接使用 uvicorn 启动（fastapi[standard] 里自带了 uvicorn）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]