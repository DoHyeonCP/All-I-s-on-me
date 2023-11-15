package com.example.scatter.viewmodel

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.data.api.ApiResponse
import com.example.data.api.ApiService
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class MainViewModel @Inject constructor(
    private val apiService: ApiService
) : ViewModel() {

    private val _congestionData = MutableLiveData<ApiResponse>()
    val congestionData: LiveData<ApiResponse> = _congestionData

    fun getCongestionData(areaName: String) {
        viewModelScope.launch {
            try {
                val dataList = apiService.getData()
                val areaData = dataList.find { it.areaName == areaName }
                _congestionData.value = areaData
            } catch (e: Exception) {
                // Handle errors
            }
        }
    }
}