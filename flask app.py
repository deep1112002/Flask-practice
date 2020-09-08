from flask import *
import cv2
app=Flask(__name__)

@app.route('/',methods=["POST"])
def startit():
    f=request.files['file']
    f.save(f.filename)
    img=cv2.imread(f.filename)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return "Tu succesful hai BC "+f.filename

if __name__=='__main__':
    app.run(debug=True)