package com.example.scatter.activity

import android.location.LocationManager
import com.example.scatter.R
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.livedata.observeAsState
import androidx.compose.runtime.setValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.lifecycleScope
import androidx.work.ExistingPeriodicWorkPolicy
import androidx.work.PeriodicWorkRequestBuilder
import androidx.work.WorkManager
import com.example.data.api.ApiService
import com.example.data.model.Congestion
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.util.Calendar
import java.util.concurrent.TimeUnit
import javax.inject.Inject


@AndroidEntryPoint
class MainActivity: ComponentActivity(){
    private val mainViewModel: MainViewModel by viewModels()


    override fun onCreate(savedInstanceState: Bundle?){
        super.onCreate(savedInstanceState)
        setContent{
            Column{
                Surface(
                    modifier = Modifier.fillMaxSize(),

                    ) {
                    MainView().Main(mainViewModel = mainViewModel)
                }
            }
        }
    }
}


//    private fun scheduleAPiCall(){
////        apiServiceManager.callApi()
//        val repeatingRequest = PeriodicWorkRequestBuilder<UploadWorker>(1, TimeUnit.HOURS)
//            // 정각에 실행되도록 지연 설정
//            .setInitialDelay(getInitialDelayToHour(), TimeUnit.MILLISECONDS)
//            .build()
//
//        WorkManager.getInstance(this).enqueueUniquePeriodicWork(
//            "ApiCall",
//            ExistingPeriodicWorkPolicy.KEEP,
//            repeatingRequest
//        )
//    }

//    fun getInitialDelayToHour(): Long {
//        val currentCalendar = Calendar.getInstance()
//        val targetCalendar = Calendar.getInstance().apply {
//            add(Calendar.HOUR_OF_DAY, 1)
//            set(Calendar.MINUTE, 0)
//            set(Calendar.SECOND, 0)
//            set(Calendar.MILLISECOND, 0)
//        }
//        return targetCalendar.timeInMillis - currentCalendar.timeInMillis
//    }

//        locationManager = getSystemService(Context.LOCATION_SERVICE) as LocationManager
//        com.example.data.mqtt.LocationInfo().startLocationService(locationManager)
//
//
//        FirebaseMessaging.getInstance().token
//            .addOnSuccessListener { token ->
//                Log.d("token", "$token")
//            }

//@Preview
//@Composable
//fun ToolbarSamplePreview() {
//    apise
//    Surface(
//            modifier = Modifier.fillMaxSize(),
//        ) {
//       Main()
//    }
//}