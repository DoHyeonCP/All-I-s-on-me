import pandas as pd
import plotly.graph_objects as go
import ImageManage

class Visualization():
    def __init__(self):
        self.image_dto = ImageManage()

    def visualize_future_data(self, total_pred):
        # 날짜시간 타입으로 변경
        total_pred['ds'] = pd.to_datetime(total_pred['ds'])
        total_pred=total_pred.set_index(total_pred['ds'], drop=True)

        ticker_list=list(total_pred.ticker.unique())
        
        #이미지 저장 전에 폴더 비우기
        self.image_dto.clear_image_folder()
        self.image_dto.clear_html_folder()
        
        for ticker in ticker_list:
            pred=total_pred.groupby('ticker').get_group(ticker)
            print(ticker)
            for i in range(24,len(pred),24):
                print(pred.index[i].date().strftime('%m월 %d일'))
                day_pred=pred[i:i+24][['pred_100m2','level','num_level']] #하루치 예측값, index에는 시간
                #print(day_pred)
                time_values=day_pred.index.strftime('%H시')

                fig=go.Figure(go.Scatter(
                    x=time_values,
                    y=day_pred['pred_100m2'],
                    mode='lines+markers',
                    marker={'symbol':'circle', 'size': 8},
                    fill='tozeroy',  # 면적 채우기 설정
                    #name=ticker,
                    hovertemplate='%{x}: %{y}명<br>%{text}단계: %{customdata}',
                    text=day_pred['num_level'],
                    customdata=day_pred['level']
                ))

                fig.update_layout(
                    #title={'text': ticker, 'x': 0.5},
                    xaxis={'title': None, 'tickformat': '%H시',
                        'tickmode': 'array',  # 눈금을 배열 모드로 설정
                        'tickvals': time_values[::3],  # 3시간 간격으로 눈금 값 설정
                        'ticktext': time_values[::3],  # 눈금에 표시될 텍스트 설정
                        'tickangle': 0,  # 눈금 텍스트의 회전 각도 설정
                        },
                    yaxis={'title': '혼잡도(명/100㎡)', 'showgrid':True, 'gridcolor':'lightgray'},
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    showlegend=False,
                )
                #fig.show()
                
                #이미지로 저장
                image_filename = f"{ticker}_{pred.index[i].date().strftime('%m%d')}.png"
                self.image_dto.save_fig_as_png(fig, image_filename)
                print(f"Image saved: {image_filename}")
                
                #HTML로 저장
                html_filename = f"{ticker}_{pred.index[i].date().strftime('%m%d')}.html"
                self.image_dto.save_fig_as_html(fig, html_filename)
                print(f"Image saved: {html_filename}")

