from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import cv2
import datetime
import numpy as np


# from pythoch
# import base64
# import tempfile
# from PIL import Image
# import io
# import numpy as np
# import os
# from mlmodel.test import cycle_gan

app = Flask(__name__)

MODEL_FILE = 'horse2zebra.t7'
# model = load_model(MODELFILE, compile=False)

# def generate():
#         fake_B_buffer = ReplayBuffer()
#         real_img_A = data["A"].to(device)
#         fake_img_B = netG_A2B(real_img_A)
#         fake_img_B = fake_B_buffer.push_and_pop(fake_img_B)
#         grdi_imgs = vutils.make_grid(fake_imgs.detach())
#         grdi_imgs_arr = grdi_imgs.cpu().numpy()
#         plt.imshow(np.transpose(grdi_imgs_arr, (1, 2, 0)))
#         plt.show()

# @app.route("/", methods=["GET", "POST"])
# def index():
#         if request.method == "GET":
#                 return render_template("index.html")
        # if request.method == 'POST':
        # # ファイルがなかった場合の処理
        #         # if 'file' not in request.files:
        #         #         flash('ファイルがありません')
        #         #         return redirect(request.url)
        #         # # データの取り出し
        #         file = request.files['file']
        #         # # ファイル名がなかった時の処理
        #         # if file.filename == '':
        #         #         flash('ファイルがありません')
        #         #         return redirect(request.url)    
        #         # # ファイルのチェック
        #         # if file and allwed_file(file.filename):
        #         #         # 危険な文字を削除（サニタイズ処理）
        #         #         filename = secure_filename(file.filename)
        #         filename = file.filename
        #         # ファイルの保存
        #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #         # アップロード後のページに転送
        #         return redirect(url_for('uploaded_file', filename=filename))

#         if request.method == "POST":
#                 return render_template("index.html")
                        # # アプロードされたファイルをいったん保存する
                        # f = request.files["file"]
                        # folderpath = tempfile.mkdtemp()
                        # filepath = os.path.join(folderpath,"a.png")
                        # #filepath = "{}/".format(tempfile.gettempdir()) + datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
                        
                        # f.save(filepath)
                        # image = Image.open(filepath)
                        
                        # # 画像処理部分
                        # image = np.asarray(image)
                        # width = len(image[0])
                        # height = len(image)      
                        # filtered = Image.fromarray(cycle_gan(folderpath))
                        # filtered = filtered.resize(size=(width,height), resample=Image.LANCZOS)
                        
                        # # base64でエンコード
                        # buffer = io.BytesIO()
                        # filtered.save(buffer, format="PNG")
                        # img_string = base64.b64encode(buffer.getvalue()).decode().replace("'", "")
                        
                        # result = "image size {}×{}".format(width, height)
                        # return render_template("index.html", filepath=filepath, result=result, img_data=img_string)

# 画像のアップロード先のディレクトリ
# UPLOAD_FOLDER = './uploads'
# # アップロードされる拡張子の制限
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def uploaded_file():
        img_dir = "static/imgs/"
        if request.method == 'GET': img_path=None
        elif request.method == 'POST':
                #### POSTにより受け取った画像を読み込む
                stream = request.files['img'].stream
                img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
                img = cv2.imdecode(img_array, 1)
                #### 現在時刻を名前として「imgs/」に保存する
                dt_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                img_path = img_dir + dt_now + ".jpg"
                cv2.imwrite(img_path, img)
                #### 保存した画像ファイルのpathをHTMLに渡す
        # return render_template('index.html') 
        return render_template('index.html', img_path=img_path) 

@app.route("/image", methods=["GET"])
def plotView():
        return render_template("image.html", success_message = '画像できたよ')
#         # Generate plot
#         fig = Figure()
#         axis = fig.add_subplot(1, 1, 1)
#         axis.set_title("title")
#         axis.set_xlabel("x-axis")
#         axis.set_ylabel("y-axis")
#         axis.grid()
#         axis.plot(range(5), range(5), "ro-")
        
#         # Convert plot to PNG image
#         pngImage = io.BytesIO()
#         FigureCanvas(fig).print_png(pngImage)
        
#         # Encode PNG image to base64 string
#         pngImageB64String = "data:image/png;base64,"
#         pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        
#         return render_template("image.html", image=pngImageB64String)

if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')
else:
        application = app
