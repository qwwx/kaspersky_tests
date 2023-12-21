FROM joyzoursky/python-chromedriver:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

CMD python -m pytest -s