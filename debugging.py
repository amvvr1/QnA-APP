from server.app.services.query_engine import QueryEngine

query_engine = QueryEngine()

file_path = "sub 38min 10k.pdf"

index = query_engine.build_index(file_paths=file_path)

engine = query_engine.build_query_engine(index=index)

response = engine.query("tell me about whats inside the file")

print(response.response)

