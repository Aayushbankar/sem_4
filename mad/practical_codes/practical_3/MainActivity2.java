package com.practicals.practicla_3;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity2 extends AppCompatActivity {
    Button btnMorning;
    Button btnAfternoon;
    Button btnEvening;
    Button btnNight;
    Button btnback;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main2);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        btnMorning = (Button) findViewById(R.id.btnMorning);
        btnAfternoon = (Button) findViewById(R.id.btnAfternoon);
        btnEvening = (Button) findViewById(R.id.btnEvening);
        btnNight = (Button) findViewById(R.id.btnNight);
        btnback = (Button) findViewById(R.id.btnBack) ;

        PrintToast(btnMorning,"Good morning");
        PrintToast(btnAfternoon,"Good afternoon");
        PrintToast(btnEvening,"Good evening");
        PrintToast(btnNight,"Good night");


        Intent back = new Intent(getApplicationContext(),MainActivity.class);
        btnback.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(back);
            }
        });

    }

    void PrintToast(Button btn ,String message){
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), message, Toast.LENGTH_SHORT).show();
            }
        });
    }


}