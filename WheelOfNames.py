import http.config

# https://wheelofnames.stoplight.io/docs/wheelofnames/ck5d76uhtsg3s-update-a-wheel

conn = http.client.HTTPSConnection("wheelofnames.com")

payload = "{\n  \"config\": {\n    \"displayWinnerDialog\": true,\n    \"slowSpin\": false,\n    \"pageBackgroundColor\": \"#FFFFFF\",\n    \"description\": \"string\",\n    \"animateWinner\": false,\n    \"winnerMessage\": \"string\",\n    \"title\": \"string\",\n    \"type\": \"color\",\n    \"autoRemoveWinner\": true,\n    \"path\": \"string\",\n    \"customPictureName\": \"string\",\n    \"customCoverImageDataUri\": \"string\",\n    \"playClickWhenWinnerRemoved\": false,\n    \"duringSpinSound\": \"ticking-sound\",\n    \"maxNames\": 1000,\n    \"centerText\": \"string\",\n    \"afterSpinSoundVolume\": 50,\n    \"spinTime\": 10,\n    \"hubSize\": \"S\",\n    \"coverImageName\": \"string\",\n    \"entries\": [\n      {\n        \"text\": \"string\",\n        \"image\": \"string\",\n        \"color\": \"string\",\n        \"weight\": 1,\n        \"id\": \"string\",\n        \"enabled\": true,\n        \"sound\": \"string\",\n        \"message\": \"string\"\n      }\n    ],\n    \"isAdvanced\": true,\n    \"galleryPicture\": \"string\",\n    \"customPictureDataUri\": \"string\",\n    \"showTitle\": true,\n    \"displayHideButton\": true,\n    \"afterSpinSound\": \"string\",\n    \"colorSettings\": [\n      {\n        \"color\": \"#FFFFFF\",\n        \"enabled\": true\n      }\n    ],\n    \"duringSpinSoundVolume\": 50,\n    \"displayRemoveButton\": true,\n    \"pictureType\": \"none\",\n    \"allowDuplicates\": true,\n    \"coverImageType\": \"\",\n    \"drawOutlines\": false,\n    \"launchConfetti\": true,\n    \"drawShadow\": true\n  }\n}"

headers = {
    'x-api-key': "",
    'Content-Type': "application/json",
    'Accept': "application/json, application/xml"
}


conn.request("PUT", "/api/v1/wheels/private", payload, headers)


res = conn.getresponse()
data = res.read()


print(data.decode("utf-8"))
