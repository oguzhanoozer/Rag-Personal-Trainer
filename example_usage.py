"""
RAG Personal Trainer - Kullanım Örnekleri
Bu dosya sistemin farklı kullanım senaryolarını gösterir.
"""

from rag_trainer import RAGPersonalTrainer, initialize_trainer


def example_1_simple_question():
    """
    Örnek 1: Basit fitness sorusu sor
    """
    print("\n" + "="*70)
    print("📋 ÖRNEK 1: Basit Fitness Sorusu")
    print("="*70)
    
    trainer = initialize_trainer()
    
    questions = [
        "Deadlift yaparken sırtımı nasıl koruyabilirim?",
        "Protein ne zaman almalıyım?",
        "HIIT nedir ve nasıl yapılır?"
    ]
    
    for question in questions:
        print(f"\n❓ Soru: {question}")
        result = trainer.ask_question(question)
        print(f"\n💡 Yanıt:\n{result['answer']}")
        print(f"\n📚 Kaynak doküman sayısı: {len(result['source_documents'])}")
        print("-" * 70)


def example_2_workout_plan_beginner():
    """
    Örnek 2: Başlangıç seviyesi kullanıcı için antrenman planı
    """
    print("\n" + "="*70)
    print("📋 ÖRNEK 2: Başlangıç Seviyesi Antrenman Programı")
    print("="*70)
    
    trainer = initialize_trainer()
    
    user_profile = {
        "yaş": "25",
        "cinsiyet": "kadın",
        "deneyim": "hiç yok (yeni başlayan)",
        "boy": "165 cm",
        "kilo": "68 kg",
        "aktivite_seviyesi": "sedanter (ofis işi)",
        "sakatlik": "yok"
    }
    
    goal = "Sağlıklı kilo vermek (10 kg) ve genel fitness seviyesini artırmak"
    
    print("\n👤 Kullanıcı Profili:")
    for key, value in user_profile.items():
        print(f"   • {key}: {value}")
    
    print(f"\n🎯 Hedef: {goal}")
    print("\n⏳ Program hazırlanıyor...")
    
    plan = trainer.generate_workout_plan(user_profile, goal)
    
    print("\n" + "="*70)
    print("🏋️ KİŞİSELLEŞTİRİLMİŞ ANTRENMAN PROGRAMI")
    print("="*70)
    print(plan['program'])
    print("\n📚 Bilgi kaynakları: {} doküman kullanıldı".format(len(plan['source_documents'])))


def example_3_workout_plan_intermediate():
    """
    Örnek 3: Orta seviye kullanıcı için kas yapım programı
    """
    print("\n" + "="*70)
    print("📋 ÖRNEK 3: Orta Seviye Kas Yapım Programı")
    print("="*70)
    
    trainer = initialize_trainer()
    
    user_profile = {
        "yaş": "28",
        "cinsiyet": "erkek",
        "deneyim": "1 yıl (düzenli antrenman yapıyor)",
        "boy": "178 cm",
        "kilo": "75 kg",
        "aktivite_seviyesi": "haftada 4-5 gün antrenman",
        "sakatlik": "hafif diz ağrısı (squat'ta dikkat gerekli)"
    }
    
    goal = "Kas kütlesi artırma (lean bulking), özellikle göğüs ve kollar"
    
    print("\n👤 Kullanıcı Profili:")
    for key, value in user_profile.items():
        print(f"   • {key}: {value}")
    
    print(f"\n🎯 Hedef: {goal}")
    print("\n⏳ Program hazırlanıyor...")
    
    plan = trainer.generate_workout_plan(user_profile, goal)
    
    print("\n" + "="*70)
    print("🏋️ KİŞİSELLEŞTİRİLMİŞ KAS YAPIM PROGRAMI")
    print("="*70)
    print(plan['program'])


def example_4_nutrition_advice():
    """
    Örnek 4: Beslenme önerileri al
    """
    print("\n" + "="*70)
    print("📋 ÖRNEK 4: Beslenme Önerileri")
    print("="*70)
    
    trainer = initialize_trainer()
    
    user_profile = {
        "yaş": "32",
        "cinsiyet": "kadın",
        "boy": "170 cm",
        "kilo": "65 kg",
        "aktivite_seviyesi": "haftada 4 gün antrenman",
        "hedef": "yağ kaybı ve kas koruma"
    }
    
    dietary_preferences = ["vejeteryan", "laktozsuz"]
    
    print("\n👤 Kullanıcı Profili:")
    for key, value in user_profile.items():
        print(f"   • {key}: {value}")
    
    print(f"\n🥗 Diyet Tercihleri: {', '.join(dietary_preferences)}")
    print("\n⏳ Beslenme planı hazırlanıyor...")
    
    nutrition = trainer.get_nutrition_advice(user_profile, dietary_preferences)
    
    print("\n" + "="*70)
    print("🥗 KİŞİSELLEŞTİRİLMİŞ BESLENME ÖNERİLERİ")
    print("="*70)
    print(nutrition['nutrition_advice'])


def example_5_advanced_questions():
    """
    Örnek 5: İleri seviye fitness soruları
    """
    print("\n" + "="*70)
    print("📋 ÖRNEK 5: İleri Seviye Sorular")
    print("="*70)
    
    trainer = initialize_trainer()
    
    advanced_questions = [
        "Progressive overload prensibini nasıl uygularım?",
        "HIIT ve LISS kardiyo arasındaki farklar nelerdir?",
        "Antrenman sonrası beslenme penceresi gerçekten önemli mi?"
    ]
    
    for i, question in enumerate(advanced_questions, 1):
        print(f"\n❓ Soru {i}: {question}")
        result = trainer.ask_question(question)
        print(f"\n💡 Yanıt:\n{result['answer']}")
        print("\n" + "-"*70)


def example_6_form_check():
    """
    Örnek 6: Egzersiz formu kontrolü
    """
    print("\n" + "="*70)
    print("📋 ÖRNEK 6: Egzersiz Formu Kontrolü")
    print("="*70)
    
    trainer = initialize_trainer()
    
    form_questions = [
        "Squat yaparken dizlerim ağrıyor, ne yapmalıyım?",
        "Bench press'te doğru form nedir?",
        "Deadlift'te hangi kaslar çalışmalı?"
    ]
    
    for question in form_questions:
        print(f"\n❓ {question}")
        result = trainer.ask_question(question)
        print(f"\n💡 Yanıt:\n{result['answer']}")
        print("\n" + "-"*70)


def example_7_custom_scenario():
    """
    Örnek 7: Özel senaryo - Evde antrenman
    """
    print("\n" + "="*70)
    print("📋 ÖRNEK 7: Evde Antrenman Programı (Minimal Ekipman)")
    print("="*70)
    
    trainer = initialize_trainer()
    
    user_profile = {
        "yaş": "35",
        "cinsiyet": "erkek",
        "deneyim": "orta",
        "ekipman": "sadece dumbbell (10kg ve 15kg), resistance band",
        "antrenman_yeri": "ev",
        "zaman": "günde 30-40 dakika"
    }
    
    goal = "Kas koruma ve fit kalma (evde minimal ekipmanla)"
    
    print("\n👤 Kullanıcı Profili:")
    for key, value in user_profile.items():
        print(f"   • {key}: {value}")
    
    print(f"\n🎯 Hedef: {goal}")
    print("\n⏳ Program hazırlanıyor...")
    
    plan = trainer.generate_workout_plan(user_profile, goal)
    
    print("\n" + "="*70)
    print("🏋️ EVDE ANTRENMAN PROGRAMI")
    print("="*70)
    print(plan['program'])


def interactive_mode():
    """
    İnteraktif Mod: Kullanıcı ile sohbet tarzı iletişim
    """
    print("\n" + "="*70)
    print("💬 İNTERAKTİF MOD - RAG Personal Trainer")
    print("="*70)
    print("\nFitness hakkında sorularınızı sorun!")
    print("Çıkmak için 'q' yazın.\n")
    
    trainer = initialize_trainer()
    
    while True:
        question = input("❓ Sorunuz: ").strip()
        
        if question.lower() in ['q', 'quit', 'exit', 'çık']:
            print("\n👋 Görüşmek üzere! Sağlıklı günler!")
            break
        
        if not question:
            continue
        
        print("\n⏳ Yanıt hazırlanıyor...")
        result = trainer.ask_question(question)
        print(f"\n💡 Yanıt:\n{result['answer']}\n")
        print("-" * 70 + "\n")


def main():
    """
    Ana fonksiyon - Tüm örnekleri sırayla çalıştır
    """
    print("\n" + "="*70)
    print("🏋️  RAG PERSONAL TRAINER - KULLANIM ÖRNEKLERİ  🏋️")
    print("="*70)
    
    examples = [
        ("1", "Basit Sorular", example_1_simple_question),
        ("2", "Başlangıç Programı", example_2_workout_plan_beginner),
        ("3", "Orta Seviye Kas Yapım", example_3_workout_plan_intermediate),
        ("4", "Beslenme Önerileri", example_4_nutrition_advice),
        ("5", "İleri Seviye Sorular", example_5_advanced_questions),
        ("6", "Form Kontrolü", example_6_form_check),
        ("7", "Evde Antrenman", example_7_custom_scenario),
        ("8", "İnteraktif Mod", interactive_mode)
    ]
    
    print("\nHangi örneği çalıştırmak istersiniz?")
    for num, title, _ in examples:
        print(f"  {num}. {title}")
    print("  0. Tümünü çalıştır (1-7)")
    
    choice = input("\nSeçiminiz (0-8): ").strip()
    
    if choice == "0":
        # Run all examples except interactive mode
        for num, title, func in examples[:-1]:
            try:
                func()
                input("\n⏸️  Devam etmek için Enter'a basın...")
            except Exception as e:
                print(f"\n❌ Hata: {e}")
    elif choice == "8":
        interactive_mode()
    elif choice in [str(i) for i in range(1, 8)]:
        idx = int(choice) - 1
        examples[idx][2]()
    else:
        print("❌ Geçersiz seçim!")


if __name__ == "__main__":
    main()
