
import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import os

cred=credentials.Certificate('././serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'mrfox-26445.appspot.com',
   'databaseURL': 'https://mrfox-26445-default-rtdb.firebaseio.com/'
})

bucket = storage.bucket()

ref = db.reference('/')
home_ref = ref.child('file')

def store_file(fileLoc):

    filename=os.path.basename(fileLoc)

    # Store File in FB Bucket
    blob = bucket.blob(filename)
    outfile=fileLoc
    blob.upload_from_filename(outfile)

def push_db(fileLoc, time):

  filename=os.path.basename(fileLoc)
  # Push file reference to image in Realtime DB
  home_ref.push({
      'image': filename,
      'timestamp': time}
  )


#if __name__ == "__main__":
#    f = open("./test1.txt", "w")
#    f.write("a demo upload file to test Firebase Storage")
#    f.close()
#    store_file('./test1.txt')

if __name__ == "__main__": 
   f = open("./test1.txt", "w") 
   f.write("a demo upload file to test Firebase Storage") 
   f.close() 
   store_file('./test1.txt') 
   push_db('./test1.txt', '14/11/2020 9:00' )
