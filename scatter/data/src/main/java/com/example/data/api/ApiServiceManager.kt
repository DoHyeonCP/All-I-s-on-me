package com.example.data.api

//import android.content.Context
//import android.util.Log
//import androidx.lifecycle.LiveData
//import androidx.lifecycle.MutableLiveData
//import com.example.data.model.Congestion
//import retrofit2.Call
//import retrofit2.Callback
//import retrofit2.Response
//import javax.inject.Inject
//
//class ApiServiceManager @Inject constructor(
//    private val context: Context,
//    private val apiService: ApiService
//){
//
//    suspend fun callApi(areaName: String): Congestion? {
//        return try {
//            val apiResponseList = apiService.getData() // Directly gets List<ApiResponse>
//            val area = apiResponseList.find { it.areaName == areaName }
//            area?.let {
//                Congestion(
//                    areaName = it.areaName,
//                    congestionLevel = it.congestionLevel,
//                    datetime = it.datetime
//                )
//            }
//        } catch (e: Exception) {
//            Log.e("API Error", "Request failed", e)
//            null // Handle the error by returning null
//        }
//    }
//}


