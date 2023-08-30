package com.example.data.db

import androidx.room.Database
import androidx.room.RoomDatabase
import com.example.data.model.Hotspot

@Database(entities = [Hotspot::class], version = 1, exportSchema = false)
abstract class AppDatabase: RoomDatabase(){
    abstract fun areaDataDao(): AreaDataDao
}