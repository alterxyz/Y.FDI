import chromadb
import chromadb.utils.embedding_functions as embedding_functions
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="OpenAI_API_KEY",
    model_name="text-embedding-3-small"
)

client = chromadb.PersistentClient(path="v_db")

collection = client.get_or_create_collection(name="test", embedding_function=openai_ef)

collection.add(
    documents=[
        "This is a document about pineapple ",
        "This is a document about oranges ",
        "This is a document about apple",
        "This is a document about earth",
        "This is a document about health",
    ],
    ids=["id1", "id2", "id3", "id4", "id5"]
)



# print(collection.peek(1)) # returns a list of the first 10 items in the collection
print(collection.count()) # returns the number of items in the collection

results = collection.query(
    query_texts=["health"], # Chroma will embed this for you
    n_results=3 # how many results to return
)
print(results)
