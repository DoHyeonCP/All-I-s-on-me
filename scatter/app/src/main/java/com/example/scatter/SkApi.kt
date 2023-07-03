package com.example.scatter

import android.content.ContentValues
import android.content.ContentValues.TAG
import android.util.Log
import android.widget.Toast
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import okhttp3.Request
import org.json.JSONException
import org.json.JSONObject
import java.io.IOException
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import okhttp3.*
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.URL

class SkApi{
    private lateinit var  apiService: ApiService

    var area_n = ""
    companion object {
        var update_date = ""
        var congestion_level = ""
    }






    fun jsonPharshing(area: String, jsonObject: JSONObject){
        val areaObject = jsonObject.getJSONObject("$area")
        Log.d(ContentValues.TAG, areaObject.toString())
        val otherObject = areaObject.getJSONObject("$area")

        area_n = area
        update_date = otherObject.getString("update_date")
        congestion_level = otherObject.getString("congestion_level")
        Log.d(TAG, "update_date: $update_date")
        Log.d(TAG, "area: $area")
        Log.d(TAG, "congestion_level: $congestion_level")

    }

}




val retrofit = Retrofit.Builder()
//            .baseUrl("http://127.0.0.1:8000/")
//            .addConverterFactory(GsonConverterFactory.create())
//            .build()
//
//        apiService = retrofit.create(ApiService::class.java)
//
//        val call: Call<JSONObject> = apiService.getData()
//        call.enqueue(object : Callback<JSONObject> {
//            override fun onResponse(call: Call<JSONObject>, response: Response<JSONObject>) {
//                if (response.isSuccessful) {
//                    val jsonObject: JSONObject? = response.body()
//                    try {
//                        if (jsonObject != null) {
//                            jsonPharshing(area_n, jsonObject)
//                        }
//                    } catch (e: JSONException) {
//                        e.printStackTrace()
//                    }
//                }
//            }
//
//            override fun onFailure(call: Call<JSONObject>, t: Throwable) {
//                // API 요청 실패 처리
//                t.printStackTrace()
//            }
//        })


//val jsonString = """
//        {
//            "post1": {
//                "update_date" : "20230627180000",
//                "area" : "롯데월드",
//                "congestion_level": "위험"
//            },
//            "post1": {
//                "update_date" : "20230627180000",
//                "area" : "방이동 먹자골목",
//                "congestion_level": "안전"
//            }
//        }
//    """.trimIndent()