package com.example.scatter


import retrofit2.Call
import retrofit2.http.GET

interface ImageApiService {
    @GET("forecastimages/")
    fun getImage() : Call<HotSpot_forecast_image>
}