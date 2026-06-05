# 🎨 AI Personal Trainer - UI Tasarım TODO Listesi

## 📦 Tasarım Araçları

Bu tasarımı şu araçlarla oluşturabilirsiniz:

- **Figma** (Önerilen - Web tabanlı, ücretsiz)
- **Adobe XD**
- **Sketch** (Mac only)
- **Canva** (Hızlı mockup için)

---

## ✅ TODO: Tasarım Aşamaları

### 🎯 Faz 1: Temel Kurulum (30 dk)

- [ ] **Yeni proje oluştur**
  - İsim: "Kinetic AI - RAG Personal Trainer"
  - Canvas boyutu: 1920x1080 (Desktop)
  - Framework: Tailwind CSS + Custom Theme
  
- [ ] **Renk paleti tanımla (Kinetic AI Theme)**

  ```
  Primary Colors:
  #006666 - Teal (Ana marka, butonlar, işaretleyici)
  #005959 - Primary Dim (Hover states)
  #73f0ef - Primary Fixed (Açık vurgu)
  #bbfffe - On Primary (Primary üzerinde metin)
  
  Secondary Colors:
  #b61321 - Kırmızı (Vurgu, logo gradient)
  #a40018 - Secondary Dim
  #b31b25 - Error
  
  Surface & Background:
  #f4f6fa - Background/Surface (Ana arka plan)
  #eef1f5 - Surface Container Low (Sidebar)
  #ffffff - Surface Container Lowest (Kartlar)
  #e5e8ed - Surface Container
  #dfe3e8 - Surface Container High
  #d9dde3 - Surface Container Highest
  
  Text Colors:
  #2c2f32 - On Surface (Ana metin)
  #595c5f - On Surface Variant (İkincil metin)
  #74777b - Outline (Kenarlıklar)
  #abadb1 - Outline Variant
  
  Gradients:
  linear-gradient(to right, #b61321, #006666) - Kinetic gradient (logo)
  ```

- [ ] **Tipografi ayarları (Lexend + Inter)**

  ```
  Font Families:
  - Headline: 'Lexend' (Başlıklar, logo, butonlar, nav)
  - Body: 'Inter' (Paragraflar, inputs)
  - Label: 'Inter' (Küçük etiketler, caption)
  
  Boyutlar:
  - Hero Title: 6xl (60px) veya 7xl (72px), font-black
  - Logo Text: 2xl (24px), font-black
  - Section Heading: lg (18px), font-semibold
  - Nav Items: sm (14px), font-medium, tracking-tight
  - Sidebar Items: xs (12px), font-bold, uppercase, tracking-widest
  - Body: xl (20px), font-light
  - Caption: 10px, uppercase, tracking-widest
  - Button: sm (14px), font-bold
  
  Line Height:
  - Hero: leading-none (1.0)
  - Body: leading-normal (1.5)
  - Sidebar items: leading-tight (1.25)
  
  Special:
  - Gradient text: bg-gradient-to-r from-[#b61321] to-[#006666]
    bg-clip-text text-transparent
  ```

- [ ] **Grid sistem kurulum**
  - 12 sütun grid
  - Gutter: 24px
  - Margin: 48px (yan boşluklar)

---

### 🖼️ Faz 2: Ana Ekran Tasarımı (1 saat)

#### A. Header (Üst Kısım)

- [ ] **Gradient başlık oluştur**
  - Metin: "🏋️ AI Personal Trainer"
  - Font: 48px, Bold
  - Gradient: #FF6B6B → #4ECDC4 (120deg)
  - Text fill: Gradient
  
- [ ] **Alt başlık ekle**
  - Metin: "RAG Powered Fitness Assistant - Kişisel AI Antrenörünüz"
  - Font: 18px, Regular
  - Renk: #666
  - Hizalama: Center

#### B. Sidebar (Sol Panel)

- [ ] **Sidebar container**
  - Genişlik: 320px
  - Arka plan: #f8f9fa
  - Yükseklik: Full screen
  - Padding: 24px
  
- [ ] **"⚙️ Ayarlar" başlığı**
  - Font: 24px, Bold
  - Margin bottom: 16px

- [ ] **API Key status indicator**
  - ✅ İkon + "API Key bulundu" metni
  - Renk: Yeşil (#10b981)
  - veya
  - ❌ İkon + "API Key eksik" metni
  - Renk: Kırmızı (#ef4444)

- [ ] **"🚀 Sistemi Başlat" butonu**
  - Genişlik: 100%
  - Yükseklik: 48px
  - Arka plan: #4ECDC4
  - Metin: Beyaz, Bold
  - Border radius: 10px
  - Hover efekti: #3da89f

- [ ] **İstatistik kartları (3 adet)**

  ```
  Kart 1: Toplam Soru
  Kart 2: Knowledge Base (4 Döküman)
  Kart 3: Model (GPT-3.5-turbo)
  
  Her kart:
  - Arka plan: Beyaz
  - Border: 1px solid #e5e7eb
  - Border radius: 8px
  - Padding: 16px
  - Shadow: 0 2px 4px rgba(0,0,0,0.05)
  ```

- [ ] **"🗑️ Geçmişi Temizle" butonu**
  - Stil: Outline (çerçeveli)
  - Renk: Kırmızı (#ef4444)
  - Genişlik: 100%

#### C. Main Content (Ana Alan)

**Durum 1: Hoşgeldiniz Ekranı (Sistem başlatılmadı)**

- [ ] **Hoşgeldiniz mesajı kartı**
  - Arka plan: Gradient (#667eea → #764ba2)
  - Metin: Beyaz
  - Padding: 32px
  - Border radius: 12px
  - Shadow: 0 4px 6px rgba(0,0,0,0.1)
  
- [ ] **Özellik listesi (4 madde)**
  - ✅ İkonlu bullet points
  - Font: 16px
  - Line height: 1.8

- [ ] **Örnek sorular listesi**
  - 5 madde
  - Italik stil
  - Gri renk (#999)

**Durum 2: Aktif Ekran (Sistem çalışıyor)**

- [ ] **"💡 Hızlı Sorular" bölümü**
  - Başlık: 24px, Bold
  
- [ ] **6 soru butonu (3x2 grid)**

  ```
  Her buton:
  - Genişlik: 100% (sütun genişliği)
  - Yükseklik: 56px
  - Arka plan: #4ECDC4
  - Metin: Beyaz, 14px
  - Border radius: 10px
  - Padding: 12px
  - Hover: #3da89f + scale(1.02)
  - Disabled: #ccc + opacity 0.6
  
  Sütun yapısı:
  [ Buton 1 ] [ Buton 2 ] [ Buton 3 ]
  [ Buton 4 ] [ Buton 5 ] [ Buton 6 ]
  ```

- [ ] **Divider çizgisi**
  - Renk: #e5e7eb
  - Margin: 24px 0

- [ ] **"❓ Kendi Sorunuzu Sorun" bölümü**
  - Başlık: 24px, Bold

- [ ] **Text area (soru input)**
  - Genişlik: 100%
  - Yükseklik: 100px
  - Border: 2px solid #e5e7eb
  - Border radius: 8px
  - Padding: 16px
  - Placeholder: Açık gri
  - Focus: Border #4ECDC4

- [ ] **"🚀 Sor" butonu (ortalanmış)**
  - Genişlik: 200px
  - Yükseklik: 48px
  - Arka plan: #4ECDC4
  - Metin: Beyaz, Bold
  - Border radius: 10px

- [ ] **Progress bar (4 aşamalı)**

  ```
  Aşama 1: 25%  - 📝 Soru işleniyor...
  Aşama 2: 50%  - 🤖 AI ile iletişim kuruluyor...
  Aşama 3: 75%  - ✅ Yanıt hazırlanıyor...
  Aşama 4: 100% - ✨ Tamamlandı!
  
  Tasarım:
  - Genişlik: 100%
  - Yükseklik: 8px
  - Arka plan: #e5e7eb
  - Dolu kısım: #4ECDC4
  - Border radius: 4px
  - Animasyon: Smooth transition
  ```

---

### 🎁 Faz 3: Soru-Cevap Kutuları (45 dk)

#### Soru Kutusu (Question Box)

- [ ] **Container oluştur**

  ```
  Boyut: 100% genişlik
  Arka plan: Linear gradient
    - Başlangıç: #667eea (sol üst)
    - Bitiş: #764ba2 (sağ alt)
    - Açı: 135deg
  Border radius: 12px
  Padding: 20px
  Shadow: 0 4px 6px rgba(0,0,0,0.1)
  Margin: 16px 0
  ```

- [ ] **İkon ve başlık**
  - "❓ Soru:" metni
  - Font: 18px, Bold
  - Renk: #FFD93D (sarı vurgu)
  - Margin bottom: 8px

- [ ] **Soru metni**
  - Font: 16px, Regular
  - Renk: Beyaz
  - Line height: 1.6
  - Text wrapping: Pre-wrap

#### Cevap Kutusu (Answer Box)

- [ ] **Container oluştur**

  ```
  Boyut: 100% genişlik
  Minimum yükseklik: 200px
  Arka plan: Beyaz
  Border: None
  Border-left: 5px solid #10b981 (yeşil)
  Border radius: 12px
  Padding: 24px
  Shadow: 0 4px 6px rgba(0,0,0,0.1)
  Margin: 16px 0
  ```

- [ ] **İkon ve başlık**
  - "💡 AI Yanıtı:" metni
  - Font: 18px, Bold
  - Renk: #059669 (koyu yeşil)
  - Margin bottom: 12px

- [ ] **Yanıt metni**
  - Font: 16px, Regular
  - Renk: #2d3748 (koyu gri)
  - Line height: 1.8 (rahat okuma)
  - Text wrapping: Pre-wrap
  - Word break: Normal

---

### 📜 Faz 4: Chat Geçmişi (30 dk)

- [ ] **"📜 Soru-Cevap Geçmişi" başlığı**
  - Font: 24px, Bold
  - Margin top: 32px

- [ ] **Expandable item tasarımı**

  ```
  Kapalı hali:
  - Genişlik: 100%
  - Yükseklik: 48px
  - Arka plan: #f8f9fa
  - Border: 1px solid #e5e7eb
  - Border radius: 8px
  - Padding: 12px 16px
  - Cursor: Pointer
  - Hover: #f0f2f6
  
  İçerik:
  - 💬 İkon + Soru preview (60 karakter)
  - Sağda chevron down/up ikon
  
  Açık hali:
  - İçinde soru ve cevap kutuları gösterilir
  - Border: 2px solid #4ECDC4 (aktif vurgu)
  ```

- [ ] **3 örnek expandable item oluştur** (mockup için)
  - En yeni üstte
  - Biri açık, ikisi kapalı gösterilsin

---

### 🎬 Faz 5: Animasyonlar & Mikrointeraksiyonlar (30 dk)

- [ ] **Buton hover efektleri**

  ```
  Hover:
  - Background color değişimi (0.2s ease)
  - Slight scale: transform: scale(1.02)
  - Cursor: pointer
  
  Active (tıklama):
  - Scale: transform: scale(0.98)
  - Darker background
  ```

- [ ] **Progress bar animasyonu**
  - Width değişimi: transition 0.5s ease
  - Smooth fill animasyonu

- [ ] **Spinner loading animasyonu**
  - Dönen halka (circle)
  - Renk: #4ECDC4
  - Boyut: 32x32px

- [ ] **Success message animasyonu**
  - Fade in: opacity 0 → 1 (0.3s)
  - Slide down: translateY(-10px → 0)

- [ ] **Expandable item animasyonu**
  - Height değişimi: max-height 0 → auto
  - Opacity: 0 → 1
  - Süre: 0.3s ease

---

### 📱 Faz 6: Responsive Tasarım (45 dk)

#### Desktop (1920x1080) - BİTTİ ✅

- [ ] Yukarıdaki tüm tasarımlar bu boyut için

#### Tablet (768x1024)

- [ ] **Layout değişiklikleri**
  - Sidebar genişlik: 280px
  - Font boyutları: 90% ölçeğinde
  - Hızlı sorular: 2 sütun yerine 2x3

- [ ] **Buton boyutları**
  - Yükseklik: 48px (touch-friendly)

#### Mobile (375x812 - iPhone X)

- [ ] **Layout değişiklikleri**
  - Sidebar: Hamburger menu'ye taşınır
  - Main content: Full width
  - Hızlı sorular: 1 sütun (stack)
  
- [ ] **Typography ölçeklendirme**
  - H1: 32px
  - H2: 24px
  - Body: 14px

- [ ] **Padding/Margin azaltma**
  - Ana padding: 16px (48px yerine)
  - Gutter: 16px (24px yerine)

---

### 🎨 Faz 7: High-Fidelity Mockup (1 saat)

- [ ] **3 ekran durumu oluştur**
  1. Başlangıç (Sistem başlatılmadı)
  2. Boş ekran (Sistem hazır, soru sorulmadı)
  3. Aktif kullanım (Soru-cevap gösteriliyor)

- [ ] **Her durum için detaylı mockup**
  - Gerçek metin kullan (Lorem ipsum değil)
  - İkonlar ekle
  - Renkleri doğru uygula
  - Gölgeleri ekle

- [ ] **Etkileşim akışı göster**
  - Ok işaretleri ile kullanıcı yolculuğu
  - State değişimleri göster
  - Hover durumları belirt

---

### ✨ Faz 8: Son Rötuşlar (30 dk)

- [ ] **Accessibility kontrolleri**
  - Renk kontrastı > 4.5:1 (WCAG AA)
  - Focus indicators görünür
  - Button'lar en az 44x44px (touch target)

- [ ] **Görsel iyileştirmeler**
  - Tüm köşeleri yuvarla (consistency)
  - Gölgeleri ayarla (derinlik hissi)
  - Spacing kontrolü (8px grid system)

- [ ] **Export hazırlığı**
  - Tüm component'leri grupla
  - İsimlendirmeyi düzenle
  - Reusable component'ler oluştur

---

## 📤 Export & Paylaşım

- [ ] **Figma/XD export**
  - PNG export: 2x resolution (Retina)
  - PDF export: Tüm sayfalar
  - Component library oluştur

- [ ] **Developer handoff**
  - CSS değerlerini not olarak ekle
  - Spacing değerlerini belirt
  - Font fallback'lerini yaz
  - Renk HEX kodlarını dokümante et

- [ ] **Prototip oluştur (opsiyonel)**
  - Clickable prototype
  - Buton tıklamaları
  - State değişimleri
  - Animasyon önizlemeleri

---

## 🎯 Checklist Özeti

### Temel Gereksinimler ✅

- [ ] Renk paleti tanımlı
- [ ] Tipografi kuralları açık
- [ ] Grid sistem kurulu
- [ ] 3 ana ekran durumu tasarlandı

### Bileşenler ✅

- [ ] Header (gradient başlık)
- [ ] Sidebar (kontrol paneli)
- [ ] Hızlı soru butonları (6 adet)
- [ ] Soru input formu
- [ ] Progress bar
- [ ] Soru kutusu (mor gradient)
- [ ] Cevap kutusu (beyaz + yeşil border)
- [ ] Chat geçmişi (expandable)

### İnteraktif Öğeler ✅

- [ ] Buton hover efektleri
- [ ] Loading spinners
- [ ] Progress animasyonu
- [ ] Expandable items

### Responsive ✅

- [ ] Desktop (1920x1080)
- [ ] Tablet (768x1024)
- [ ] Mobile (375x812)

---

## 🛠️ Önerilen Figma Eklentileri

1. **Iconify** - Ücretsiz ikonlar (emoji alternatifi)
2. **Unsplash** - Placeholder görseller
3. **Stark** - Accessibility kontrol
4. **Arc** - Border radius ayarlama
5. **Content Reel** - Gerçek içerik üretimi

---

## 💡 Tasarım İpuçları

### Renk Kullanımı

- Mor gradient sadece soru kutularında
- Yeşil border/vurgu sadece cevap kutularında
- Turkuaz butonlarda ve progress'te
- Beyaz arka planlar temiz görünüm için

### Espacios (Boşluklar)

- 8px grid kullan: 8, 16, 24, 32, 48, 64
- Tutarlı padding: Kartlarda hep 16 veya 24
- Margin consistency: Bölümler arası 32-48px

### Typography Hiyerarşisi

- Her sayfada 1 H1 (Ana başlık)
- H2 bölüm ayırıcı
- H3 alt başlıklar
- Body büyük metinlerde
- Caption küçük notlar

### Görsel Denge

- Sidebar 1/4, Main content 3/4
- Simetrik buton dizilimi
- Center alignment başlıklarda
- Left alignment body metinlerde

---

**Tahmini Toplam Süre:** 5-6 saat  
**Zorluk Seviyesi:** Orta  
**Önerilen Araç:** Figma (ücretsiz)  
**Sonuç:** Production-ready UI tasarımı  

---

💪 **İyi tasarımlar!** Bu checklist'i takip ederek profesyonel bir UI tasarımı oluşturabilirsiniz.
