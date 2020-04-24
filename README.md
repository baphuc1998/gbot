# train
    rasa train
# run cmd
    rasa shell
# run NLU
    rasa shell nlu
# run GUI
    rasa x
# run actions
    rasa run actions
# run api
    rasa run
# use
    1. rasa train
    2. run redis (if use rasa x, this step is unnecessary) port 6379
    3. cmd: rasa run actions
    4. choose one way to chat with bot
        GUI: rasa x (easiest but slow)
        run api: rasa run
            cmd: python run.py
            postman:
                http://localhost:5005/webhooks/rest/webhook
                {
                    "sender": "token",
                    "message": "hi"
                }

