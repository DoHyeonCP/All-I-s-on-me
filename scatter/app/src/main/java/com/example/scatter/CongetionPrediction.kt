package com.example.scatter

import android.net.http.SslError
import android.os.Bundle
import android.os.PersistableBundle
import android.webkit.SslErrorHandler
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.Toolbar
import com.example.scatter.databinding.CongetionPredictionBinding
import com.example.scatter.databinding.ToolbarBinding

class CongetionPrediction : AppCompatActivity() {
    private lateinit var predictionBinding: CongetionPredictionBinding
    private lateinit var webView : WebView
    private lateinit var toolbarbinding: ToolbarBinding
    private lateinit var toolbar: Toolbar

    override fun onCreate(savedInstanceState: Bundle?) {
        setTheme(R.style.AppTheme)
        super.onCreate(savedInstanceState)

        toolbarbinding = ToolbarBinding.inflate(layoutInflater)
        toolbar = toolbarbinding.root
        predictionBinding = CongetionPredictionBinding.inflate(layoutInflater)

        setContentView(predictionBinding.root)
        setSupportActionBar(toolbar)

        webView = predictionBinding.predictionGraph
        webView.settings.javaScriptEnabled = true
        webView.settings.mixedContentMode = WebSettings.MIXED_CONTENT_ALWAYS_ALLOW

        webView.webViewClient = object : WebViewClient(){
            override fun onReceivedSslError(view: WebView?, handler: SslErrorHandler?, error: SslError?){
                handler?.proceed()
            }
        }

        webView.loadUrl("https://www.naver.com")
    }
}