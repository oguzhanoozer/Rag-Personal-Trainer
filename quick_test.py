"""
Hızlı Test - RAG Personal Trainer
Sadece 1 soru sorup yanıt alacağız
"""

from rag_trainer import RAGPersonalTrainer
import os
from dotenv import load_dotenv

load_dotenv()

print("="*70)
print("🏋️  RAG PERSONAL TRAINER - HIZLI TEST")
print("="*70)

try:
    # RAG trainer oluştur
    print("\n1️⃣ RAG Trainer başlatılıyor...")
    trainer = RAGPersonalTrainer()
    
    # Knowledge base yükle
    print("2️⃣ Knowledge base yükleniyor...")
    trainer.load_knowledge_base()
    
    # QA chain kur
    print("3️⃣ QA chain kuruluyor...")
    trainer.setup_qa_chain()
    
    # Basit bir soru sor
    print("\n" + "="*70)
    question = "Bench press nasıl yapılır? Teknikleri nelerdir?"
    print(f"❓ SORU: {question}")
    print("="*70)
    
    print("\n🤖 AI yanıt hazırlıyor...\n")
    response = trainer.ask_question(question)
    
    print("💡 YANIT:")
    print("-" * 70)
    print(response)
    print("-" * 70)
    
    print("\n✅ Test başarılı! RAG sistemi çalışıyor.")
    
except Exception as e:
    print(f"\n❌ HATA: {e}")
    print("\nLütfen kontrol edin:")
    print("  • OPENAI_API_KEY .env dosyasında mı?")
    print("  • knowledge_base/ klasörü mevcut mu?")
    print("  • Tüm bağımlılıklar yüklü mü?")
