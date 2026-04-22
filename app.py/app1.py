from model import detect_threat

if __name__ == "__main__":
    print("🔐 AI SOC Log Analyzer")
    
    query = input("Enter a security log: ")
    
    threat, explanation = detect_threat(query)
    
    print("\n🚨 Threat Type:", threat)
    print("\n🧠 Explanation:\n", explanation)
