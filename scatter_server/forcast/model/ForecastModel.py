import pandas as pd
from time import time
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

from data.DataProcessor import train_dataset, create_features
from weather_df import train_weather, test_weather
from holiday_df import make_holiday_df

class ForecastModel():
    def __init__(self):
        self.con=train_dataset()
        self.train_wea=train_weather()
        self.test_wea=test_weather()
        self.holiday_df=make_holiday_df()
        self.support = SupportModel()


    def three_days_model(self):
        def add_regressors(m):
            #변수 추가
            m.add_regressor('TMP', standardize=False)
            m.add_regressor('PCP', standardize=False)
            m.add_regressor('weekday', standardize=False)
            m.add_regressor('season_Winter', standardize=False)
            m.add_regressor('season_Spring', standardize=False)
            m.add_regressor('season_Summer', standardize=False)
            m.add_regressor('season_Fall', standardize=False)
            m.add_regressor('tbin_0', standardize=False)
            m.add_regressor('tbin_1', standardize=False)
            m.add_regressor('tbin_2', standardize=False)
            m.add_regressor('tbin_3', standardize=False)

        return self.support.run_model(add_regressors, 3*24, 'h')


    def eight_days_model(self):
        def add_regressors(m):
            m.add_regressor('weekday', standardize=False)
            m.add_regressor('season_Winter', standardize=False)
            m.add_regressor('season_Spring', standardize=False)
            m.add_regressor('season_Summer', standardize=False)
            m.add_regressor('season_Fall', standardize=False)
            m.add_regressor('tbin_0', standardize=False)
            m.add_regressor('tbin_1', standardize=False)
            m.add_regressor('tbin_2', standardize=False)
            m.add_regressor('tbin_3', standardize=False)
        return self.support.run_model(add_regressors, 8*24, 'h')
    
    def total_predictions(self):
        #예측값 병합(모델1, 2)
        pred=self.three_days_model()
        pred2=self.eight_days_model()
        total_pred=pd.concat([pred, pred2])
        #예측값 저장
        total_pred.to_csv('total_pred.csv', index=False)

        return total_pred

class SupportModel():
    def run_model(self, add_regressor_callback, periods, freq):
        mul = pd.merge(self.con, self.train_wea, on = 'ds')
        mul = create_features(mul)
        groups_by_ticker = mul.groupby('ticker')
        
        for_loop_forecast = pd.DataFrame()

        for ticker in groups_by_ticker.groups.keys():
            group = groups_by_ticker.get_group(ticker)
            m = Prophet(interval_width = 0.8,
                            seasonality_mode='multiplicative',
                            holidays_prior_scale=15,
                            holidays=self.holiday_df)
            
            add_regressor_callback(m)

            m.add_seasonality(name='weekly', period=7, fourier_order=10)

            m.fit(group)

            future = m.make_future_dataframe(periods=periods, freq=freq)
            future = create_features(future)
            forecast = m.predict(future)

            # 시각화
            fig = m.plot(forecast)
            ax = fig.gca()
            ax.plot(group['ds'], group['y'], 'b.')
            comp_plot = m.plot_components(forecast)
            plt.show()

            forecast['ticker'] = ticker
            for_loop_forecast = pd.concat([for_loop_forecast, forecast[['ds', 'ticker', 'yhat', 'yhat_upper', 'yhat_lower']]])
        return self.postprocessing(for_loop_forecast, mul)

    def postprocessing(self, for_loop_forecast, mul):
        #예측 음수 값 -> 0으로 대체
        for_loop_forecast['yhat']=for_loop_forecast.apply(lambda x: 1e-6 if x['yhat']<0 else x['yhat'], axis=1)
        for_loop_forecast['yhat_upper']=for_loop_forecast.apply(lambda x: 1e-6 if x['yhat_upper']<0 else x['yhat_upper'], axis=1)
        for_loop_forecast['yhat_lower']=for_loop_forecast.apply(lambda x: 1e-6 if x['yhat_lower']<0 else x['yhat_lower'], axis=1)
        for_loop_forecast.sort_values(by=['ds','ticker'], inplace=True)
        total_forecast=for_loop_forecast.copy()

        
        #실제값('y')열과 합치기
        predictions=pd.merge(mul,total_forecast, on=['ds','ticker'], how='outer')
        predictions=predictions[['ds','ticker','y','yhat','yhat_upper','yhat_lower']]
        predictions.sort_values(by=['ds','ticker'], inplace=True)

        return predictions

    
    

if __name__=='__main__':
    start_time=time()
    model=ForecastModel()
    total_pred=model.total_predictions()
    print('Time:', time()-start_time)