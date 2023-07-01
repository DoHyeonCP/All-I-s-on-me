package com.example.scatter

import android.content.ContentValues.TAG
import android.util.Log
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import org.json.JSONObject
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class SkApi{
    private lateinit var  apiService: UpdateApiService

    fun calljson(BASE_URL : String){
        val retrofit = Retrofit.Builder()
            .baseUrl("$BASE_URL")
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        apiService = retrofit.create(UpdateApiService::class.java)

        CoroutineScope(Dispatchers.IO).launch{
            try{
                val data = apiService.getData(update_date, area, congestion_level)
                // 데이터 파싱처리
//                jsonPharshing(data)
            } catch (e: Exception){
                e.printStackTrace()
            }
        }
    }


    var update_date = ""
    var area = ""
    var congestion_level = ""
    fun jsonPharshing(){
        val testarea = "post1"
        val jsonString = """
        {
            "post1": {
                "update_date" : "20230627180000",
                "area" : "롯데월드",
                "congestion_level": "위험"
            },
            "post1": {
                "update_date" : "20230627180000",
                "area" : "방이동 먹자골목",
                "congestion_level": "안전"
            }
        }
    """.trimIndent()

        val jObject = JSONObject(jsonString)
        val post1Object = jObject.getJSONObject(testarea)
        Log.d(TAG, post1Object.toString())

        update_date = post1Object.getString("update_date")
        area = post1Object.getString("area")
        congestion_level = post1Object.getString("congestion_level")
        update_date = update_date
        area = area
        congestion_level = congestion_level
        Log.d(TAG, "update_date: $update_date")
        Log.d(TAG, "area: $area")
        Log.d(TAG, "congestion_level: $congestion_level")

    }

}