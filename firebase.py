import urllib
import pyrebase

firebaseConfig = {
"apiKey": "AIzaSyBYjQ204RuBhuJFnj0MyAZL6ObfLP0XV1M",
"authDomain": "indian-plagiarism-tool.firebaseapp.com",
"databaseURL": "https://indian-plagiarism-tool-default-rtdb.asia-southeast1.firebasedatabase.app",
"projectId": "indian-plagiarism-tool",
"storageBucket": "indian-plagiarism-tool.appspot.com",
"messagingSenderId": "204343244106",
"appId": "1:204343244106:web:0c11ca4b5de3abd204fdb3",
#"serviceAccount": "serviceAccountKey.json"
}

firebase=pyrebase.initialize_app(firebaseConfig)

#define storage
storage=firebase.storage()

#upload a file
file=input("Enter the name of the file you want to upload to storage")
cloudfilename=input("Enter the name for the file in storage")
storage.child(cloudfilename).put(file)

#get url of the file we just uploaded
print(storage.child(cloudfilename).get_url(None))

#download a file
storage.child(cloudfilename).download("downloaded.txt")


#to read from the file
path=storage.child(cloudfilename).get_url(None)
f = urllib.request.urlopen(path).read()
print(f)