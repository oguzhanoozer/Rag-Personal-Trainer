"""
ULTRA BASIT TEST - Manuel Deneme
"""
import streamlit as st
from simple_test import SimpleRAGTrainer

st.title("🧪 Minimal Test")

# Test buton
if st.button("TEST: API Çalışıyor mu?"):
    try:
        st.write("1. SimpleRAGTrainer oluşturuluyor...")
        trainer = SimpleRAGTrainer()
        
        st.write("2. Knowledge base yükleniyor...")
        trainer.load_knowledge_base()
        
        st.write("3. Basit soru soruluyor...")
        answer = trainer.ask_question("Merhaba, test")
        
        st.success("✅ BAŞARILI!")
        st.write(f"Cevap: {answer}")
        
    except Exception as e:
        st.error(f"❌ HATA: {e}")
        import traceback
        st.code(traceback.format_exc())
