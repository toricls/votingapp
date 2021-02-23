FROM python:3.9.2-slim
COPY requirements.txt app.py /
RUN pip install -r requirements.txt

RUN groupadd -r restaurantgroup && useradd -r -g restaurantgroup restaurantuser
USER restaurantuser
CMD ["python", "-u", "app.py"]
