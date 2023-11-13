import os
import shutil
import plotly.io as pio
from django.conf import settings

class ImageManage:
    def clear_image_folder():
        # 이미지 저장 폴더 경로
        save_dir = "images"

        # 폴더가 존재하면 비우기
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)
            print(f"Cleared image folder: {save_dir}")

    def clear_html_folder():
        # HTML 저장 폴더 경로
        html_dir = "html_files"

        # 폴더가 존재하면 비우기
        if os.path.exists(html_dir):
            shutil.rmtree(html_dir)
            print(f"Cleared image folder: {html_dir}")


    def save_fig_as_png(fig, filename):
        # 이미지 저장 폴더 경로
        root = os.path.join(settings.MEDIA_ROOT, "forcast_image")
        save_dir = "images"

        # 폴더가 존재하지 않으면 생성
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 이미지 파일 경로
        file_path = os.path.join(save_dir, filename)

        # 이미지로 저장
        fig.write_image(file_path, format="png")

        
    def save_fig_as_html(fig, filename):
        # 이미지 저장 폴더 경로
        save_dir = "html_files"

        # 폴더가 존재하지 않으면 생성
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 이미지 파일 경로
        file_path = os.path.join(save_dir, filename)
        
        pio.write_html(fig, file=file_path)
        print(f"Figure saved as HTML: {file_path}")
