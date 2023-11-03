package com.example.data.api

import com.google.gson.annotations.SerializedName

data class Hotspot(
    @SerializedName("congestion_level") val congestionLevel: String? = null,
    @SerializedName("datetime") val datetime: String? =null
)
