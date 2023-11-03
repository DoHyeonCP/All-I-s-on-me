package com.example.data.api

import android.content.Context
import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.example.data.model.Congestion
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import javax.inject.Inject

class ApiServiceManager @Inject constructor(
    private val context: Context,
    private val apiService: ApiService


){
    private val _apiResult = MutableLiveData<Congestion>()
    val apiResult: LiveData<Congestion> = _apiResult

    fun callApi(areaName : String) {
        Log.d("ApiServiceManager", "callApi is called with areaName: $areaName")
        val call = apiService.getData()
        call.enqueue(object : Callback<List<ApiResponse>> {
            override fun onResponse(call: Call<List<ApiResponse>>, response: Response<List<ApiResponse>>) {
                Log.d("ApiServiceManager", "API Response: ${response.body()}")
                if (response.isSuccessful) {
                        response.body()?.let{apiResponse ->
                            val area = apiResponse.find { it.areaName == areaName }
                            area?.let {
                                val congestion = Congestion(
                                    areaName = it.areaName,
                                    congestionLevel = it.congestionLevel,
                                    datetime = it.datetime
                                )
                                _apiResult.postValue(congestion)
                            }

                    }
                } else {
                    Log.e("API Error", "Request failed with code: ${response.code()}")
                }
            }

            override fun onFailure(call: Call<List<ApiResponse>>, t: Throwable) {
                // API 요청 실패 처리
                t.printStackTrace()
            }
        })
    }

//    private fun areaparshing(areaName: String, apiResponse: ApiResponse): Congestion{
//        val area = apiResponse.getClassField(areaName) // Reflectively get the field
//        val congestionLevel = area.congestionLevel ?: "요청 불가 시간입니다."
//        val datetime = area.datetime ?: "8~22시까지 서비스합니다."
//
//        return Congestion(
//            areaName = areaName,
//            congestionLevel = congestionLevel,
//            datetime = datetime
//        )
//    }
//
//    // This is a helper function to get the value of the class field using reflection
//    private fun ApiResponse.getClassField(fieldName: String): Hotspot {
//        val field = this::class.java.getDeclaredField(fieldName)
//        field.isAccessible = true
//        return field.get(this) as Hotspot
//    }

}


