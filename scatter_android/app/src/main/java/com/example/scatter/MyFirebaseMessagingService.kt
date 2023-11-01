package com.example.scatter

import android.util.Log
import android.widget.Toast
import com.google.android.gms.tasks.OnCompleteListener
import com.google.firebase.messaging.FirebaseMessaging
import com.google.firebase.messaging.FirebaseMessagingService


// 배포전까지의 디버깅용
// firebase는 배포하기전까진 여기서 Log에 나온 토근을 server에 직접입력하여
// push알림을 받도록 해야함
class MyFirebaseMessagingService : FirebaseMessagingService() {

    companion object {
        private const val TAG = "MyFirebaseMessagingService"
    }

    override fun onNewToken(token: String) {
        super.onNewToken(token)
        Log.d(TAG, "Refreshed token: $token")

        // 서버로 토큰을 전송하는 로직을 구현하세요.
//        sendRegistrationToServer(token)
    }



//    private fun sendRegistrationToServer(token: String) {
//        // 서버로 토큰을 전송하는 로직을 구현하세요.
//    }
}