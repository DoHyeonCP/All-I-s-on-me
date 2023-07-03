package com.example.scatter

import android.util.Log
import com.google.firebase.messaging.FirebaseMessaging
import com.google.firebase.firestore.auth.FirebaseAppCheckTokenProvider
import com.google.firebase.iid.FirebaseInstanceIdReceiver
import com.google.firebase.iid.internal.FirebaseInstanceIdInternal
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence
import org.eclipse.paho.client.mqttv3.*
import com.example.scatter.FirebaseMessagingService
import com.google.firebase.ktx.Firebase

class Mqtt {
    private lateinit var mqttClient : MqttClient
    val brokerUrl = "tcp://115.21.135.45:1883"

    fun sendLocationToServer(latitude: Double, longitude: Double) {


        val clientId = "Phone_GPS"
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

        FirebaseMessaging.getInstance().token
            .addOnSuccessListener { token ->
                var firebasetoken = token
                val topic = "location"
                var message = "$latitude" + "," +"$longitude" + "," + "$firebasetoken"
                Log.i("informatio", message)
                var mqttMessage = MqttMessage(message.toByteArray())
                mqttClient.publish(topic, mqttMessage)
            }
    }
<<<<<<< HEAD
}
=======

    fun requestLocationinfo(area: String){
        val clientId = "locationname"

        val topic = "$area"
        var message = "$area"
        val payload = "disconnected".toByteArray(Charsets.UTF_8)
        Log.i("informatio", message)
        var mqttMessage = MqttMessage(message.toByteArray())

        try {
            mqttClient = MqttClient(brokerUrl, clientId, MemoryPersistence())
            val mqttConnectOptions = MqttConnectOptions()
            mqttConnectOptions.connectionTimeout = 1000
            mqttConnectOptions.setWill("$area", payload, 2, false)
            mqttClient.connect(mqttConnectOptions)
        } catch(ex: MqttException){
            ex.printStackTrace()
        }
        mqttClient.publish(topic, mqttMessage)
    }
}
>>>>>>> bc27729b2e81cf02a2b0e400afd3bdb6d6e69a28
