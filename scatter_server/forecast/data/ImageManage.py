import os
import shutil
import plotly.io as pio
from django.conf import settings

class ImageManage():
    def __init__(self):
        self.root = os.path.join(settings.MEDIA_ROOT, "forecast_image")
    
    def clear_image_folder(self):
        # 이미지 저장 폴더 경로
        save_dir = self.root

        # 폴더가 존재하면 비우기
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)
            print(f"Cleared image folder: {save_dir}")


    def save_fig_as_png(self, fig, filename):
        # 이미지 저장 폴더 경로
        save_dir = self.root

        # 폴더가 존재하지 않으면 생성
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 이미지 파일 경로
        file_path = os.path.join(save_dir, filename)

        # 이미지로 저장
        fig.write_image(file_path, format="png")


