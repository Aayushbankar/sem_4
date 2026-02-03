---
name: android_development
description: Android/Kotlin patterns, XML layouts, Activity lifecycle, and mobile app development concepts
---

# Android Development Assistant

**Purpose:** Explain Android concepts, generate code snippets, and solve MAD practical problems.

---

## Core Concepts Coverage

### 1. Activity Lifecycle
```
onCreate → onStart → onResume → [RUNNING] → onPause → onStop → onDestroy
                                    ↑                      ↓
                                    ←───── onRestart ←─────
```

### 2. Project Structure
```
app/
├── manifests/AndroidManifest.xml
├── java/[package]/
│   ├── MainActivity.kt
│   └── [Other Activities]
└── res/
    ├── layout/           → XML UI files
    ├── values/           → strings.xml, colors.xml
    ├── drawable/         → Images, icons
    └── mipmap/           → App icons
```

---

## Code Generation Templates

### Activity Template (Kotlin)
```kotlin
class [Name]Activity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.[layout_name])
        
        // Initialize views
        // Set listeners
    }
}
```

### XML Layout Template
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">
    
    <!-- Views here -->
    
</LinearLayout>
```

---

## Common Components

| Component         | Purpose                 | Key Methods              |
| ----------------- | ----------------------- | ------------------------ |
| Activity          | Single screen           | onCreate, onResume       |
| Fragment          | Reusable UI section     | onCreateView             |
| Intent            | Navigation/data passing | putExtra, getStringExtra |
| RecyclerView      | Efficient lists         | Adapter, ViewHolder      |
| SharedPreferences | Simple storage          | getSharedPreferences     |
| SQLite            | Local database          | SQLiteOpenHelper         |

---

## Explanation Rules

- Always pair Kotlin code with corresponding XML
- Show manifest entries when needed
- Explain View binding or findViewById usage
- Include Gradle dependencies if using libraries
- Demonstrate both programmatic and XML approaches
