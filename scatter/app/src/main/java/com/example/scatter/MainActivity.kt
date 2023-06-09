package com.example.scatter



import android.content.Context
import android.content.Intent
import android.location.LocationManager
import android.os.Bundle
import android.util.Log
import android.view.Gravity
import android.widget.Button
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.Toolbar
import androidx.drawerlayout.widget.DrawerLayout
import com.example.scatter.databinding.MainActivityBinding
import com.example.scatter.databinding.ToolbarBinding
import com.google.firebase.messaging.FirebaseMessaging
import com.example.scatter.databinding.ToolbarHeadBinding

class MainActivity : AppCompatActivity() {
    private lateinit var mainbinding: MainActivityBinding
    private lateinit var locationManager: LocationManager
    private lateinit var toolbarbinding: ToolbarBinding
    private lateinit var ivMenu: ImageView
    private lateinit var close_menu: ImageView
    private lateinit var drawerLayout: DrawerLayout
    private lateinit var toolbar: Toolbar
    private lateinit var toolbarheadbinding: ToolbarHeadBinding
    private lateinit var button: Button

    companion object {
        private const val TAG = "MainActivity"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        setTheme(R.style.AppTheme)
        super.onCreate(savedInstanceState)
        mainbinding = MainActivityBinding.inflate(layoutInflater)
        toolbarbinding = ToolbarBinding.inflate(layoutInflater)
        toolbarheadbinding = ToolbarHeadBinding.inflate(layoutInflater)

        setContentView(mainbinding.root)

        ivMenu = toolbarbinding.ivMenu
        close_menu = toolbarheadbinding.closeMenu
        drawerLayout = mainbinding.root
        toolbar = toolbarbinding.root
        button = mainbinding.prediction

        setSupportActionBar(toolbar)

        ivMenu.setOnClickListener {
            drawerLayout.openDrawer(Gravity.LEFT)
        }



        close_menu.setOnClickListener{
            drawerLayout.closeDrawer(Gravity.LEFT)

        }
        button.setOnClickListener {
            val intent = Intent(this@MainActivity, CongetionPrediction::class.java)
            startActivity(intent)
        }


        val congetioninfohead = mainbinding.textHead
        congetioninfohead.text = "기준시간: \n\n" +
                "지역 이름: \n\n" +
                "위험도(혼잡도): "

        // 디버깅용 코드 3줄 SkApi에 지역을 넣었을 때 return 되도록 해야한다.


        val skApi = DjnagoApi()
        skApi.jsonPharshing()
        var u = skApi.update_date
        var a = skApi.area
        var c = skApi.congestion_level
        val congetioninfobody = mainbinding.textBody
        congetioninfobody.text = "$u \n\n" +
                "$a \n\n" +
                "$c \n\n"


        locationManager = getSystemService(Context.LOCATION_SERVICE) as LocationManager
        LocationInfo().startLocationService(locationManager)

        FirebaseMessaging.getInstance().token
            .addOnSuccessListener { token ->
                Log.d(TAG, "Token: $token")
            }
    }

    override fun onResume() {
        super.onResume()
        RequestPermissions().requestlocationpermission(this, this, locationManager)

    }
}


