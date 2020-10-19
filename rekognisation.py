import csv
import boto3

with open('new_user_credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

#photo = 'hot_air_ballon.jpg'
#photo = 'beyonce.jpg'
#photo = 'smiling_girl.jpg'
#photo = 'random_guy.jpg'
#photo = 'elon_musk.jpg'
#source_photo = 'priyanka.jpg'
#target_photo = 'priyanka_group.jpg'
#target_photo = 'deepika_aishwariya.jpg'
photo = 'quote.jpg'
client = boto3.client('rekognition', aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key, region_name = 'us-east-1')


#with open(photo,'rb') as source_image:
#    source_bytes = source_image.read()

#response = client.detect_labels(Image={'Bytes': source_bytes}, MaxLabels=2, MinConfidence=95)
#response = client.detect_moderation_labels(Image={'S3Object': {'Bucket': 'palak-ac', 'Name': photo}})
#response = client.detect_faces(Image={'S3Object': {'Bucket':'palak-ac', 'Name': photo}}, Attributes = ['ALL'])
#for key, value in response.items():
#    if key == 'FaceDetails':
#       for people_att in value:
#            print(people_att)
#            print("===============")
#response = client.recognize_celebrities(Image={'S3Object': {'Bucket':'palak-ac', 'Name': photo}})
#for key, value in response.items():
#    if key == 'CelebrityFaces':
#        for people_att in value:
#            print(people_att)
#            print("===============")
#response = client.compare_faces(SourceImage = {'S3Object': {'Bucket':'palak-ac', 'Name': source_photo}},
#                               TargetImage = {'S3Object': {'Bucket':'palak-ac', 'Name': target_photo}} )
#for key, value in response.items():
#    if key in ('FaceMatches','UnmatchedFaces'):
#        print(key)
#           print(people_att)
response = client.detect_text(Image={'S3Object': {'Bucket':'palak-ac', 'Name': photo}})
print(response)