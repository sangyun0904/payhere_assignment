FROM python:3.9.7 
EXPOSE 8000 
WORKDIR /payhere_assignment
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir 
COPY . .
ENTRYPOINT [ "python3" ]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]