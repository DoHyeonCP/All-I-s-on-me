package com.example.data.api

import com.google.gson.annotations.SerializedName

data class ApiResponse(
    @SerializedName("id") val id: Int,
    @SerializedName("area_name") val areaName: String,
    @SerializedName("datetime") val datetime: String,
    @SerializedName("congestion_level") val congestionLevel: String
)
