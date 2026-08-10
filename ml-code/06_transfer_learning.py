"""
06 — Pretrained models (transfer learning): use a trained model instead of building one.
Part A (colab-friendly, no big downloads): HuggingFace pipeline for text (sentiment).
Part B: image transfer-learning with torchvision (fine-tune ResNet head) — stub w/ notes.

Run Part A:  pip install transformers  (or use Google Colab)
            python ml-code/06_transfer_learning.py
"""
try:
    from transformers import pipeline
except ImportError:
    print("Install first:  pip install transformers  (or run in Colab)")
    raise SystemExit

# A) Zero-shot/sentiment in one line — no training by us!
clf = pipeline("sentiment-analysis")
for t in ["I love this product, it is amazing!",
           "This is the worst app I have ever used.",
           "Okay, it works fine, nothing special."]:
    print(t, "->", clf(t))

# B) Text generation
gen = pipeline("text-generation", model="distilgpt2")  # tiny model ~ 313M params
out = gen("Machine learning is", max_length=20, num_return_sequences=1)
print("\ngenerated:", out[0]["generated_text"])

print("\nKEY IDEAS")
print("- We never trained these. We loaded weights trained by others and used them.")
print("- Fine-tuning = retrain the LAST few layers on your own small dataset.")
print("- For images: torchvision.models.resnet18(pretrained=True) then swap the head:",
      "model.fc = nn.Linear(512, num_classes)")
print("- This is how you ship an 'AI feature' in a hackathon in < 1 hour.")