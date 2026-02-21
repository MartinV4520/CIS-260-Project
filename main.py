from classify_url import classify

def main():
    print("=== Phishing Detector ===")
    url = input("Enter a URL to classify: ")
    label, confidence, model_name = classify(url)

    print(f"\nModel: {model_name}")
    print(f"Prediction: {label}")
    if confidence is not None:
        print(f"Confidence: {confidence:.4f}")

if __name__ == "__main__":
    main()
