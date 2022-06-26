curl --request POST http://localhost:5000/api/timeline_post -d 'name=Ryson&email=fake@gmail.com&content=This is a Message'

curl --request GET http://localhost:5000/api/timeline_post

curl --request DELETE http://localhost:5000/api/timeline_post
