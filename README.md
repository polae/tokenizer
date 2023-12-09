# Tokenizer
This api gives a token count for a particular string and OpenAI model. 

### JSON Schema
```
{
  "text": "Example text ...",
  "model_name": "gpt-4"
}
```

### Docker Reference 

To run this locally (with Docker installed):

Build the container:
 ```
docker build -t tokenizer .
```

Run the container:

```
docker run -p 127.0.0.1:8085:8085 tokenizer
```

ENDPOINT:
```
http://localhost:8085/count_tokens
```

API Reference: 
```
http://localhost:8085/docs
```





