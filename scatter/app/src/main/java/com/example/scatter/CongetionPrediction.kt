package com.example.scatter

import android.net.http.SslError
import android.os.Bundle
import android.os.PersistableBundle
import android.webkit.SslErrorHandler
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.appcompat.app.AppCompatActivity
import com.example.scatter.databinding.CongetionPredictionBinding

class CongetionPrediction : AppCompatActivity() {
    private lateinit var predictionBinding: CongetionPredictionBinding
    private lateinit var webView : WebView

    override fun onCreate(savedInstanceState: Bundle?) {
        setTheme(R.style.AppTheme)
        super.onCreate(savedInstanceState)

        predictionBinding = CongetionPredictionBinding.inflate(layoutInflater)

        webView = predictionBinding.predictionGraph
        webView.settings.javaScriptEnabled = true
        webView.settings.mixedContentMode = WebSettings.MIXED_CONTENT_ALWAYS_ALLOW

        webView.webViewClient = object : WebViewClient(){
            override fun onReceivedSslError(view: WebView?, handler: SslErrorHandler?, error: SslError?){
                handler?.proceed()
            }
        }

        webView.loadUrl("www.naver.com")
    }
}