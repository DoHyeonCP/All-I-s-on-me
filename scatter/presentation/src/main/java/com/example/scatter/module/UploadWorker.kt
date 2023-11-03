package com.example.scatter.module

import android.content.Context
import androidx.work.ExistingPeriodicWorkPolicy
import androidx.work.PeriodicWorkRequestBuilder
import androidx.work.WorkManager

import androidx.work.Worker
import androidx.work.WorkerParameters
import com.example.data.api.ApiServiceManager
import java.util.concurrent.TimeUnit
import javax.inject.Inject

//class UploadWorker(appContext: Context,  workerParams: WorkerParameters):
//    Worker(appContext, workerParams) {
//
//    @Inject
//    lateinit var apiServiceManager: ApiServiceManager
//
//    override fun doWork(): Result {
//        apiServiceManager.callApi()
//
//        // Indicate whether the work finished successfully with the Result
//        return Result.success()
//    }
//
//
//
//
//}