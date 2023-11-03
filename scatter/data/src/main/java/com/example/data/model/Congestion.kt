package com.example.data.model

import androidx.room.Entity
import androidx.room.PrimaryKey

data class Congestion(
    val areaName: String,
    val congestionLevel: String,
    val datetime: String

)
