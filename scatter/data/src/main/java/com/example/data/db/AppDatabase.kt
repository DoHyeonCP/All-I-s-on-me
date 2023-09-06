package com.example.data.db

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import com.example.data.model.Congestion

@Database(entities = [Congestion::class],version = 1, exportSchema = false)
abstract class AppDatabase: RoomDatabase(){
    abstract fun areaDataDao(): AreaDataDao

    companion object{
        private var INSTANCE: AppDatabase? = null

        @Synchronized
        fun getDatabase(context: Context): AppDatabase? {
            if (INSTANCE == null){
                INSTANCE = Room.databaseBuilder(
                    context.applicationContext,
                    AppDatabase::class.java,
                    "congestion"
                ).build()
            }
            return INSTANCE
        }
    }
}