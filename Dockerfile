FROM python

WORKDIR /tg_bot_nupodymym

COPY . .

EXPOSE 8001

RUN pip install -r requirements.txt

CMD ["python", "tg-bot-posts-nupodymym.py"]
