#! /bin/bash

# remove
rm cloudtech_quiz_bot.zip

cd cloudtech_quiz_bot
pip3 install LINE-bot-sdk pynamodb -t .
cd ..

# compress
zip -r cloudtech_quiz_bot.zip ./cloudtech_quiz_bot/*
