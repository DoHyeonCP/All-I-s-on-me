package com.example.scatter

import android.content.Intent
import android.net.http.SslError
import android.os.Bundle
import android.os.PersistableBundle
import android.view.View
import android.webkit.SslErrorHandler
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.ImageButton
import android.widget.ImageView
import android.widget.Spinner
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.Toolbar
import androidx.compose.ui.graphics.Color
import com.example.scatter.databinding.CongetionPredictionBinding
import com.example.scatter.databinding.ToolbarBinding

class CongetionPrediction : AppCompatActivity() {
    private lateinit var predictionBinding: CongetionPredictionBinding
    private lateinit var spinner1 : Spinner
    private lateinit var spinner2 : Spinner
    private lateinit var graphview1 : ImageView
    private lateinit var graphview2 : ImageView
    private lateinit var backButton : ImageButton
    override fun onCreate(savedInstanceState: Bundle?) {
        setTheme(R.style.Theme_Scatter)
        super.onCreate(savedInstanceState)

        predictionBinding = CongetionPredictionBinding.inflate(layoutInflater)

        setContentView(predictionBinding.root)

        backButton = predictionBinding.backButton


        spinner1 = predictionBinding.spinner1
        graphview1 = predictionBinding.graph1
        val itemArray = arrayOf("지역을 선택해주세요", "롯데월드", "방이동먹자골목", "에비뉴엘월드타워점", "롯데월드몰", "올림픽공원")
        val spinnerAdapter1 = ArrayAdapter(
            this,
            R.layout.spinner_dropdown_item,
            itemArray
        )
        spinner1.adapter = spinnerAdapter1

        spinner2 = predictionBinding.spinner2
        graphview2 = predictionBinding.graph2
        val spinnerAdapter2 = ArrayAdapter(
            this,
            R.layout.spinner_dropdown_item,
            itemArray
        )
        spinner2.adapter = spinnerAdapter2


        spinner1.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
                override fun onItemSelected(
                    parent: AdapterView<*>,
                    view: View,
                    position: Int,
                    id: Long
                ) {
                    val seletedRegion = itemArray[position]
                    val imageResurceID = getImageResourceId(seletedRegion)
                    graphview1.setImageResource(imageResurceID)

                }

                override fun onNothingSelected(parent: AdapterView<*>) {}
            }

        spinner2.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(
                parent: AdapterView<*>,
                view: View,
                position: Int,
                id: Long
            ) {
                val seletedRegion = itemArray[position]
                val imageResurceID = getImageResourceId(seletedRegion)
                graphview2.setImageResource(imageResurceID)

            }

            override fun onNothingSelected(parent: AdapterView<*>) {}
        }

        backButton.setOnClickListener{
            val intent = Intent(this@CongetionPrediction, MainActivity::class.java)
            startActivity(intent)
        }
    }


    private fun getImageResourceId(region: String): Int {
        return when (region) {
            "롯데월드" -> R.drawable.jamsillotteworld
            "방이동먹자골목" -> R.drawable.bangi
            "에비뉴엘월드타워점" -> R.drawable.avinual
            "롯데월드몰" -> R.drawable.lotteworldmall
            "올림픽공원" -> R.drawable.oplimpicpark
            else -> R.drawable.whitescreen // 기본 이미지 리소스 ID
        }
    }


}