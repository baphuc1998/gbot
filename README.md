# train nlu
    rasa train
# test your bot in command
    rasa shell
# run NLU
    rasa shell nlu
# run GUI
    rasa x
# run your bot's actions
    rasa run actions
# run api
    rasa run
# to use you can run following commnad
    1. rasa train
    2. rasa run actions
    3. rasa run
    Use postma to test via api
    url : http://localhost:5005/webhooks/rest/webhook
    body:   {
                "sender": "token",
                "message": "hi"
            }

