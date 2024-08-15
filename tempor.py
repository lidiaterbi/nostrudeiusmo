batch_size = 1000
for i in range(0, len(data), batch_size):
    documents = data["text_column"].iloc[i:i+batch_size].tolist()
    model.fit(documents)
