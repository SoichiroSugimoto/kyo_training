cd cloudtech_quiz_bot
python -m pip install LINE-bot-sdk pynamodb -t .
cd ..
powershell.exe -NoProfile -ExecutionPolicy Unrestricted -File .\setup_lambda.ps1
