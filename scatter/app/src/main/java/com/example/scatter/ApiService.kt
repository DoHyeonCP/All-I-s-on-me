package com.example.scatter



import org.json.JSONObject
import retrofit2.Call
import retrofit2.Response
import retrofit2.http.GET
import retrofit2.http.Header
import retrofit2.http.POST
import retrofit2.http.Query

interface ApiService{
    @GET("api-sk/") // 엔드포인트 경로
    fun getData(): Call<JSONObject>
}