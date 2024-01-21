
FROM python:3.8


WORKDIR /test_automation


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . /test_automation


CMD ["pytest", "--html=report/report.html", "test", "-n", "6"]
