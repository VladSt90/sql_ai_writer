import chromadb
import os
from .llm_requests import llm_generate_embedding
from .logger import logger


class EmbeddingsManager:
    def __init__(self) -> None:
        chromadb_path = os.getcwd() + "/.chromadb"
        self.client = chromadb.PersistentClient(path=chromadb_path)
        self.collection = self.client.get_or_create_collection(
            name="test", metadata={"hnsw:space": "cosine"}
        )

    def contain_embeddings(self):
        return self.collection.count() != 0

    def add_documents(self, documents):
        logger.info("Generate embeddings...")
        for i, document in enumerate(documents):
            embedding = llm_generate_embedding(document)
            self.collection.add(ids=str(i), embeddings=embedding, documents=document)

        logger.info("Table descriptions embeddings generated!")

    def vector_search(self, document):
        logger.info(
            "Generate an embedding for the prompt and retrieve the most relevant doc..."
        )

        user_input_embedding = llm_generate_embedding(document)
        results = self.collection.query(
            query_embeddings=user_input_embedding, n_results=3
        )
        associated_documents = results["documents"]

        logger.info(f"\nAssociated documents:\n{associated_documents}\n")

        return associated_documents
