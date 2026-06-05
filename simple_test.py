"""
RAG Personal Trainer - Basitleştirilmiş Versiyon  
(Dependency sorunlarını bypass eden direkt OpenAI API kullanımı)
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import glob

load_dotenv()

class SimpleRAGTrainer:
    """Basitleştirilmiş RAG - OpenAI API direkt kullanımı"""
    
    def __init__(self, verbose=False):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.knowledge_base = ""
        self.verbose = verbose
        
    def load_knowledge_base(self, path="knowledge_base", verbose=False):
        """Tüm txt dosyalarını yükle"""
        if verbose:
            print(f"📚 Knowledge base yükleniyor: {path}/")
        files = glob.glob(f"{path}/*.txt")
        
        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                self.knowledge_base += f"\n\n=== {os.path.basename(file)} ===\n{content}"
        
        if verbose:
            print(f"✅ {len(files)} dosya yüklendi ({len(self.knowledge_base)} karakter)")
        
    def ask_question(self, question):
        """Soru sor - knowledge base'i context olarak kullan"""
        if self.verbose:
            print(f"\n🤖 Soru işleniyor: {question[:60]}...")
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"""Sen profesyonel bir fitness antrenörüsün.
Aşağıdaki bilgi tabanından yararlanarak soruları yanıtla:

{self.knowledge_base[:4000]}  

Kısa, pratik ve bilimsel yanıtlar ver."""},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content


# HIZLI TEST
if __name__ == "__main__":
    print("="*70)
    print("🏋️  SIMPLIFIED RAG PERSONAL TRAINER - TEST")
    print("="*70)
    
    try:
        trainer = SimpleRAGTrainer()
        trainer.load_knowledge_base()
        
        # Test soruları
        questions = [
            "Bench press nasıl yapılır?",
            "HIIT nedir ve faydaları nelerdir?",
            "Protein nedir ve günde ne kadar almalıyım?"
        ]
        
        for q in questions:
            print("\n" + "="*70)
            print(f"❓ {q}")
            print("="*70)
            answer = trainer.ask_question(q)
            print(f"\n💡 {answer}\n")
            
        print("\n✅ Test başarılı!")
        
    except Exception as e:
        print(f"\n❌ HATA: {e}")
        print("\n.env dosyasında OPENAI_API_KEY var mı kontrol edin.")
