from flask import Flask, request, send_file, render_template_string
import onnxruntime as ort
import numpy as np
import soundfile as sf
import io
import os

app = Flask(__name__)
# sess_options = onnxruntime.SessionOptions()
# session = ort.InferenceSession("./finetuning_pretrained_vi_female_epoch=4785.onnx",sess_options)  # Thay bằng đường dẫn tới mô hình ONNX của bạn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        # inputs = {"input": text,"scales": 0.67,"input_lengths": len(text)}  # Điều chỉnh đầu vào theo mô hình của bạn
        # outputs = session.run(None, inputs)
        # waveform = outputs[0]  # Giả định đầu ra là dạng sóng âm thanh
        # buffer = io.BytesIO()
        # sf.write(buffer, waveform, samplerate=22050, format='WAV')
        # buffer.seek(0)
        os.system("""echo {text} | \
  piper -m ./finetuning_pretrained_vi_female_epoch=4785.onnx --output_file ./test_v2.wav""")
        return "test"
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="vi">
        <head>
            <meta charset="UTF-8">
            <title>Chuyển Văn Bản Thành Giọng Nói</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                input { padding: 10px; width: 300px; }
                button { padding: 10px 20px; margin-left: 10px; }
                audio { margin-top: 20px; }
            </style>
        </head>
        <body>
            <h1>Nhập văn bản để chuyển thành giọng nói</h1>
            <form method="POST">
                <input type="text" name="text" placeholder="Nhập văn bản...">
                <button type="submit">Chuyển đổi</button>
            </form>
            <audio controls src="{{ url_for('index') }}"></audio>
        </body>
        </html>
    ''')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)