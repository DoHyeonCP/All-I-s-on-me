package com.example.scatter.activity

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.data.api.ApiResponse
import com.example.data.api.ApiServiceManager
import com.example.data.model.Congestion
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class MainViewModel @Inject constructor(
    private val apiServiceManager: ApiServiceManager
) : ViewModel() {

    private val _congestionData = MutableLiveData<Congestion>()
    val congestionData: LiveData<Congestion> = _congestionData

    init {
        apiServiceManager.apiResult.observeForever {
            _congestionData.value = it
        }
    }
    fun onMenuItemSelected(areaName: String) {
        apiServiceManager.callApi(areaName)
    }
}