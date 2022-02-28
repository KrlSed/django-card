FROM python:3.10.2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /django-card/django_card

COPY req.txt /django-card/django_card
RUN pip install -r req.txt

COPY .. /django-card/django_card

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

