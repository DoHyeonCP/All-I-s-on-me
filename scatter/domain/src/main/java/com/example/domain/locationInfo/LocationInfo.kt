//package com.example.domain.locationInfo
//
//import android.location.Location
//import android.location.LocationListener
//import android.location.LocationManager
//import android.os.Bundle
//import android.util.Log
////import com.google.android.gms.location.LocationResult
////import com.google.android.gms.location.LocationServices
////import com.google.android.gms.location.LocationSettingsRequest
//
//class LocationInfo{
//    private lateinit var gpsListener : GPSListener
//
//
//    fun startLocationService(locationManager : LocationManager){
//        try{
//            var location: Location? = null
//            val minTime: Long = 10000
//            val minDistance = 1f
//
//            gpsListener = GPSListener()
//
//            if(locationManager.isProviderEnabled(LocationManager.GPS_PROVIDER)) {
//                location = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER)
//
//                if(location != null){
//                    val latitude = location.latitude
//                    val longitude = location.longitude
//                    val message = "최근위치1 -> Latitude : $latitude, Longitude : $longitude"
//
//                    Log.i("MyLocTest", message)
//                }
//                locationManager.requestLocationUpdates(
//                    LocationManager.GPS_PROVIDER,
//                    minTime,
//                    minDistance,
//                    gpsListener
//                )
//            }
////            else if (locationManager.isProviderEnabled(LocationManager.NETWORK_PROVIDER)) {
////                location = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER)
////
////                if (location != null) {
////                    val latitude = location.latitude
////                    val longitude = location.longitude
////                    val message = "최근 위치2 -> Latitude : $latitude\n Longitude : $longitude"
////                    Log.i("MyLocTest", message)
////                }
////                locationManager.requestLocationUpdates(
////                    LocationManager.NETWORK_PROVIDER,
////                    minTime,
////                    minDistance,
////                    gpsListener,
////                )
////                Log.i("MyLocTest", "requestLocationUpdates() 내 위치2에서 호출시작 ~~ ")
////            }
//        } catch (e: SecurityException){
//            Log.e("$e", "fail")
//        }
//    }
//
//    inner class GPSListener : LocationListener {
//        override fun onLocationChanged(location: Location) {
//            val latitude = location.latitude
//            val longitude = location.longitude
//            val message = "내 위치는 Latitude : $latitude Longitude : $longitude"
//            Log.i("MyLocTest", message)
//        }
//
//        override fun onStatusChanged(provider: String, status: Int, extras: Bundle) {}
//
//        override fun onProviderEnabled(provider: String) {}
//
//        override fun onProviderDisabled(provider: String) {}
//    }
//}