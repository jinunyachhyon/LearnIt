from flask import Flask, request, jsonify, render_template
from ytvids.ytvids import download_video_mp4, create_audio_file
import ffmpeg
from pytube import YouTube


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('pdflink') == 'pdflink':
            return render_template('pdflink.html')
        if request.form.get('ytlink') == 'ytlink':
            return render_template('ytlink.html')
        if request.form.get('upload') == 'upload':
            return render_template('upload.html')

    return render_template('index.html')



@app.route('/ytlink', methods=['GET', 'POST'])
def ytlink():
    '''
    For rendering results on HTML GUI
    '''
    
    return render_template('ytlink.html')

@app.route('/pdflink', methods=['GET', 'POST'])
def pdflink():
    '''
    For rendering results on HTML GUI
    '''
    return render_template('pdflink.html')
    

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    '''
    For rendering results on HTML GUI
    '''
    return render_template('upload.html')


@app.route("/ytlink/output", methods=['GET', 'POST'])
def output():
    px = request.form['output']
    download_video_mp4(px)
    name = 'How Old Is The Water You Drink.mp4'
    create_audio_file(name)
    return render_template('output.html')

     

    





@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)