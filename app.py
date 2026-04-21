from flask import Flask, request
import boto3
import os

app = Flask(__name__)

S3_BUCKET_NAME = 'ccproj6054'
s3 = boto3.client('s3', region_name='ap-south-1')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
        message = ""
        if request.method == 'POST':
                if 'file' not in request.files:
                        message = "No file selected"
                file = request.files['file']
                if file.filename == '':
                        message = "Please choose a file"
                if file:

                        try:
                                s3.upload_fileobj(file, S3_BUCKET_NAME, file.filename)
                                message = "File uploaded successfully!"
                        except Exception as e:
                                message = f" {e}"
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Cloud File Upload</title>

<style>
body {{
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #0f2027, #2c5364);
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}}

.container {{
    background: white;
    padding: 35px;
    border-radius: 15px;
    width: 360px;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
    animation: fadeIn 0.7s ease;
}}

h1 {{
    margin-bottom: 20px;
    color: #333;
}}

.upload-area {{
    border: 2px dashed #aaa;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    transition: 0.3s;
}}
.upload-area:hover {{
    border-color: #007bff;
}}

input[type="file"] {{
    width: 100%;
    border: none;
}}

button {{
    width: 100%;
    padding: 12px;
    border: none;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    font-size: 16px;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s;
}}

button:hover {{
    transform: scale(1.05);
    background: linear-gradient(to right, #0072ff, #00c6ff);
}}

.message {{
    margin-top: 15px;
    font-weight: bold;
    font-size: 14px;
}}

.footer {{
    margin-top: 10px;
    font-size: 12px;
    color: #888;
}}

@keyframes fadeIn {{
    from {{opacity:0; transform:translateY(20px);}}
    to {{opacity:1; transform:translateY(0);}}
}}
</style>

</head>
<body>

<div class="container">
    <h1>☁️ Upload File</h1>

    <form method="POST" enctype="multipart/form-data">
        <div class="upload-area">
            <input type="file" name="file">
        </div>

        <button type="submit">Upload</button>
    </form>
 <div class="message">{message}</div>
    <div class="footer">AWS S3 Cloud Storage</div>
</div>

</body>
</html>
'''

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
