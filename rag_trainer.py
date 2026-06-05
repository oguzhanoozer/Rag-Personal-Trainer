"""
RAG-based AI Personal Trainer
Kişiselleştirilmiş fitness programları oluşturmak için RAG (Retrieval-Augmented Generation) sistemi
"""

import os
from typing import List, Dict, Optional
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()


class RAGPersonalTrainer:
    """
    RAG tabanlı kişisel antrenör AI sistemi.
    Fitness bilgi tabanından ilgili bilgileri çekerek kişiselleştirilmiş programlar oluşturur.
    """
    
    def __init__(
        self, 
        knowledge_base_path: str = "./knowledge_base",
        persist_directory: str = "./chroma_db",
        model_name: str = "gpt-3.5-turbo",
        temperature: float = 0.7
    ):
        """
        RAG Personal Trainer'ı başlat.
        
        Args:
            knowledge_base_path: Fitness dokümanlarının bulunduğu klasör
            persist_directory: ChromaDB veritabanı kayıt klasörü
            model_name: OpenAI model adı
            temperature: LLM temperature (0-1, yaratıcılık seviyesi)
        """
        self.knowledge_base_path = knowledge_base_path
        self.persist_directory = persist_directory
        self.model_name = model_name
        self.temperature = temperature
        
        # API key kontrolü
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY environment variable not set!")
        
        # Initialize components
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature
        )
        self.vectorstore = None
        self.qa_chain = None
        
    def load_knowledge_base(self) -> None:
        """
        Fitness bilgi tabanını yükle ve vector store'a dönüştür.
        """
        print(f"📚 Loading knowledge base from {self.knowledge_base_path}...")
        
        # Load documents
        loader = DirectoryLoader(
            self.knowledge_base_path,
            glob="**/*.txt",
            loader_cls=TextLoader,
            show_progress=True
        )
        documents = loader.load()
        
        if not documents:
            raise ValueError(f"No documents found in {self.knowledge_base_path}")
        
        print(f"✅ Loaded {len(documents)} documents")
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        splits = text_splitter.split_documents(documents)
        print(f"📄 Split into {len(splits)} chunks")
        
        # Create vector store
        print("🔨 Creating vector store...")
        self.vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        print("✅ Vector store created successfully!")
        
    def load_existing_vectorstore(self) -> bool:
        """
        Var olan vector store'u yükle (varsa).
        
        Returns:
            True if loaded successfully, False otherwise
        """
        if os.path.exists(self.persist_directory):
            print(f"📂 Loading existing vector store from {self.persist_directory}...")
            try:
                self.vectorstore = Chroma(
                    persist_directory=self.persist_directory,
                    embedding_function=self.embeddings
                )
                print("✅ Vector store loaded successfully!")
                return True
            except Exception as e:
                print(f"❌ Error loading vector store: {e}")
                return False
        return False
        
    def setup_qa_chain(self, custom_prompt: Optional[str] = None) -> None:
        """
        QA chain'i kur.
        
        Args:
            custom_prompt: Özel prompt template (opsiyonel)
        """
        if not self.vectorstore:
            raise ValueError("Vector store not initialized! Call load_knowledge_base() first.")
        
        # Default prompt template
        if custom_prompt is None:
            template = """Sen profesyonel bir kişisel antrenör ve fitness uzmanısın.
Aşağıdaki bilgi tabanı verilerini kullanarak kullanıcının sorusuna detaylı ve kişiselleştirilmiş yanıt ver.

Bilgi Tabanı:
{context}

Kullanıcı Sorusu: {question}

Yanıtın:
- Bilimsel ve kanıta dayalı olmalı
- Kullanıcının seviyesine uygun olmalı
- Güvenli ve uygulanabilir olmalı
- Spesifik egzersizler, set/tekrar sayıları ve form açıklamaları içermeli
- Motivasyonel ve destekleyici bir dil kullanmalı

Yanıt:"""
        else:
            template = custom_prompt
        
        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )
        
        # Create QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(
                search_kwargs={"k": 4}  # Top 4 most relevant chunks
            ),
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )
        print("✅ QA chain setup complete!")
        
    def generate_workout_plan(
        self,
        user_profile: Dict[str, str],
        goal: str
    ) -> Dict[str, any]:
        """
        Kullanıcı profili ve hedefe göre kişiselleştirilmiş antrenman programı oluştur.
        
        Args:
            user_profile: Kullanıcı bilgileri (yaş, cinsiyet, deneyim seviyesi, vb.)
            goal: Fitness hedefi
            
        Returns:
            Programı ve kaynak dokümanları içeren dict
        """
        if not self.qa_chain:
            raise ValueError("QA chain not setup! Call setup_qa_chain() first.")
        
        # Construct query from user profile
        profile_str = ", ".join([f"{k}: {v}" for k, v in user_profile.items()])
        query = f"""
Kullanıcı Profili: {profile_str}
Hedef: {goal}

Bu kullanıcı için haftalık detaylı bir antrenman programı oluştur. Program şunları içermeli:
1. Haftalık antrenman planı (her gün hangi kas grupları)
2. Her egzersiz için set ve tekrar sayıları
3. Doğru form ve teknik ipuçları
4. İlerleme önerileri
5. Beslenme önerileri (genel)
"""
        
        # Get response from RAG system
        result = self.qa_chain.invoke({"query": query})
        
        return {
            "program": result["result"],
            "source_documents": result["source_documents"],
            "user_profile": user_profile,
            "goal": goal
        }
    
    def ask_question(self, question: str) -> Dict[str, any]:
        """
        Fitness hakkında genel soru sor.
        
        Args:
            question: Kullanıcı sorusu
            
        Returns:
            Yanıtı ve kaynak dokümanları içeren dict
        """
        if not self.qa_chain:
            raise ValueError("QA chain not setup! Call setup_qa_chain() first.")
        
        result = self.qa_chain.invoke({"query": question})
        
        return {
            "answer": result["result"],
            "source_documents": result["source_documents"]
        }
    
    def get_nutrition_advice(
        self,
        user_profile: Dict[str, str],
        dietary_preferences: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Kullanıcı profili ve tercihlere göre beslenme önerileri al.
        
        Args:
            user_profile: Kullanıcı bilgileri
            dietary_preferences: Diyet tercihleri (vegan, vegetarian, vs.)
            
        Returns:
            Beslenme önerileri ve kaynak dokümanları
        """
        if not self.qa_chain:
            raise ValueError("QA chain not setup! Call setup_qa_chain() first.")
        
        profile_str = ", ".join([f"{k}: {v}" for k, v in user_profile.items()])
        preferences_str = ", ".join(dietary_preferences) if dietary_preferences else "Yok"
        
        query = f"""
Kullanıcı Profili: {profile_str}
Diyet Tercihleri: {preferences_str}

Bu kullanıcı için detaylı beslenme önerileri oluştur:
1. Günlük kalori ihtiyacı tahmini
2. Makro besin dağılımı (protein, karbonhidrat, yağ)
3. Önerilen yiyecekler
4. Örnek öğün planı
5. Takviye önerileri (eğer gerekiyorsa)
"""
        
        result = self.qa_chain.invoke({"query": query})
        
        return {
            "nutrition_advice": result["result"],
            "source_documents": result["source_documents"],
            "user_profile": user_profile
        }


def initialize_trainer(force_reload: bool = False) -> RAGPersonalTrainer:
    """
    RAG Personal Trainer'ı başlat ve hazırla.
    
    Args:
        force_reload: Var olan vector store'u sil ve yeniden yükle
        
    Returns:
        Hazır RAGPersonalTrainer instance
    """
    trainer = RAGPersonalTrainer()
    
    # Load or create vector store
    if force_reload or not trainer.load_existing_vectorstore():
        trainer.load_knowledge_base()
    
    # Setup QA chain
    trainer.setup_qa_chain()
    
    return trainer


if __name__ == "__main__":
    print("🏋️ RAG Personal Trainer AI 🏋️")
    print("=" * 50)
    
    # Initialize
    trainer = initialize_trainer()
    
    # Example: Ask a question
    print("\n📋 Example Question:")
    question = "Squat egzersizini nasıl doğru yaparım?"
    result = trainer.ask_question(question)
    print(f"\nSoru: {question}")
    print(f"\nYanıt:\n{result['answer']}")
    
    # Example: Generate workout plan
    print("\n" + "=" * 50)
    print("📋 Example Workout Plan:")
    user_profile = {
        "yaş": "28",
        "cinsiyet": "erkek",
        "deneyim": "başlangıç",
        "boy": "175 cm",
        "kilo": "75 kg"
    }
    goal = "Kas kütlesi artırma ve yağ yakma"
    
    plan = trainer.generate_workout_plan(user_profile, goal)
    print(f"\nKullanıcı: {user_profile}")
    print(f"Hedef: {goal}")
    print(f"\nProgram:\n{plan['program']}")
