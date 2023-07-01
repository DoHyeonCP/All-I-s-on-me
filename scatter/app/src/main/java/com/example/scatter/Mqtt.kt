package com.example.scatter

import android.util.Log
import com.google.firebase.firestore.auth.FirebaseAppCheckTokenProvider
import com.google.firebase.iid.FirebaseInstanceIdReceiver
import com.google.firebase.iid.internal.FirebaseInstanceIdInternal
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence
import org.eclipse.paho.client.mqttv3.*
import com.example.scatter.FirebaseMessagingService
import com.google.firebase.ktx.Firebase


class Mqtt  {
    private lateinit var mqttClient : MqttClient
    private lateinit var firebasemessagingservice : FirebaseMessagingService



    fun sendLocationToServer(latitude: Double, longitude: Double) {
        val brokerUrl = "tcp://192.168.143.180:1883"
        val clientId = "Phone_GPS"

        firebasemessagingservice = FirebaseMessagingService()
        firebasemessagingservice
        val firebaseToken = firebasemessagingservice.firebasetoken

//        val payload = "disconnected".toByteArray(Charsets.UTF_8)
        try {
            mqttClient = MqttClient(brokerUrl, clientId, MemoryPersistence())
            val mqttConnectOptions = MqttConnectOptions()
            mqttConnectOptions.connectionTimeout = 1000
//            mqttConnectOptions.setWill("location", payload, 1, false)
            mqttClient.connect(mqttConnectOptions)
        } catch(ex: MqttException){
            ex.printStackTrace()
        }
        val topic = "location"
        val message = "$latitude" + "," +"$longitude"
        val mqttMessage = MqttMessage(message.toByteArray())
        Log.i("firebasetoken", "$firebaseToken")
        mqttClient.publish(topic, mqttMessage)
    }
}
