package com.example.scatter

import android.content.Context
import android.content.pm.PackageManager
import android.location.LocationManager
import android.util.Log
import androidx.core.app.ActivityCompat.requestPermissions
import androidx.core.app.ActivityCompat.shouldShowRequestPermissionRationale
import androidx.core.content.ContextCompat
import com.example.scatter.LocationInfo


public class RequestPermissions {
    private val LOCATION_PERMISSION_REQUEST_CODE = 1


    fun requestlocationpermission(context: Context, activity : MainActivity, locationmanager : LocationManager) {
        if (ContextCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED
            && ContextCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED
            && ContextCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_BACKGROUND_LOCATION) != PackageManager.PERMISSION_GRANTED
        ) {
            // 권한이 허용되지 않은경우
            if (shouldShowRequestPermissionRationale(activity , android.Manifest.permission.ACCESS_FINE_LOCATION)
                && shouldShowRequestPermissionRationale(activity, android.Manifest.permission.ACCESS_COARSE_LOCATION)
                && shouldShowRequestPermissionRationale(activity, android.Manifest.permission.ACCESS_BACKGROUND_LOCATION)

            ) {
            } else {
                // 권한에 대한 설명이 필요하지 않은 경우(이미 이전에 권한 요청을 했고 거부당함)
                // 바로 권한 요청
                requestPermissions(
                    activity,
                    arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION),
                    LOCATION_PERMISSION_REQUEST_CODE
                )
                requestPermissions(
                    activity,
                    arrayOf(android.Manifest.permission.ACCESS_COARSE_LOCATION),
                    LOCATION_PERMISSION_REQUEST_CODE
                )
                requestPermissions(
                    activity,
                    arrayOf(android.Manifest.permission.ACCESS_BACKGROUND_LOCATION),
                    LOCATION_PERMISSION_REQUEST_CODE
                )
            }
        } else {

        }
    }
    fun requestnotificationpermission(context: Context, activity : MainActivity){
        if (ContextCompat.checkSelfPermission(context, android.Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED
        ) {
            // 권한이 허용되지 않은경우
            if (shouldShowRequestPermissionRationale(activity, android.Manifest.permission.POST_NOTIFICATIONS)
            ) {
            } else {
                // 권한에 대한 설명이 필요하지 않은 경우(이미 이전에 권한 요청을 했고 거부당함)
                // 바로 권한 요청
                requestPermissions(
                    activity,
                    arrayOf(android.Manifest.permission.POST_NOTIFICATIONS),
                    LOCATION_PERMISSION_REQUEST_CODE
                )
            }
        } else {

        }
    }
}