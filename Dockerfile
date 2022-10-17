FROM python:3.7-slim-buster
ADD generate_and_evaluate.py /
CMD [ "python3", "generate_and_evaluate.py" ]