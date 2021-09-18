import requests

url = "https://australiaeast.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US"

headers = {
  'Content-type': 'audio/wav;codec="audio/pcm";',
  'Ocp-Apim-Subscription-Key': 'YOUR_SUBSCRIPTION_KEY',
  # OR 'Authorization: Bearer ACCESS_TOKEN'
}

with open('{FILE_PATH\\Welcome.wav','rb') as payload:
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
