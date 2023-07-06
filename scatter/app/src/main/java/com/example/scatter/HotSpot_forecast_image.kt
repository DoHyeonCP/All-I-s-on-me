package com.example.scatter

import android.media.Image
import com.google.gson.annotations.SerializedName

data class HotSpot_forecast_image(
    @SerializedName("name") val name : String? = null,
    @SerializedName("path") val path : Image
)
