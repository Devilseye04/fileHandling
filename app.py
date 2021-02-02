from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os , shutil

app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader_file():
    image = ['ras', 'xwd', 'bmp', 'jpe', 'jpg', 'jpeg', 'xpm', 'ief', 'pbm', 'tif', 'gif', 'ppm', 'xbm', 'tiff', 'rgb', 'pgm', 'png', 'pnm']
    if request.method == 'POST':
        try:
            f= request.files['file']
            filename = secure_filename(f.filename)
            f.save('tmp/'+filename)
            l = os.path.getsize("tmp/"+filename)
            if l == 0:
                os.remove("tmp/"+filename)
                return jsonify({"ErrorMessage":"File is empty","isError":"True"})
            ext = filename.split('.')[-1]
            print(ext)
            form = "<form action='http://localhost:5000/upload'><input type='submit' value='new upload'></form>"
            if ext == 'txt':
                shutil.move('tmp/'+filename,'txt/'+filename)
                f.save('txt/'+filename)
                return "file uploaded Successfully " + form
            elif ext in image:
                shutil.move('tmp/'+filename,'txt/'+filename)
                f.save('images/'+filename)
                return "file uploaded Successfully " + form
            elif ext == 'json':
                shutil.move('tmp/'+filename,'txt/'+filename)
                f.save('json/'+filename)
                return "file uploaded Successfully " + form
            #else:
            #    return jsonify({"ErrorMessage":"File Format Not Supported","isError":"True"})
        except Exception as e:
            os.remove("tmp/"+filename)
            return jsonify({"ErrorMessage":str(e),"isError":"True"})
if __name__ == '__main__':
    app.run(debug=True)
