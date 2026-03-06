A Python tool that analyszes URL's and determines whether they are legitimate, suspicious , or potentially malicious. It uses URL feature extraction and heuristic rules to identify common phising patterns such as deceptive domains, excessive sudomains, obfuscation, and known attack indicators. The purpose of this python tool is to help assist students, security beginners, and anyone who needs a simple offline phishing detection tool.

---Features---

Analyzes URLs using rule-based detection

Extractts structural features

Flags high-risk patterns such as deceptive keywords or obfuscated domains

Detects shortened links and embedded redirects

Provides clear output

Works Fully Offline

Optional .exe structural distribution for Windows




---Directory---

phishing-detector/

│

├── main.py                 # Entry point


├── detector/


│   ├── analyzer.py         # Core detection logic


│   ├── features.py         # URL feature extraction


│   └── rules.py            # Heuristic rules


├── model/


│   └── trained_model.pkl   # Optional ML model


├── utils/


│   └── helpers.py          # Utility functions


├── tests/                  # Test cases


├── requirements.txt        # Dependencies


└── README.md               # Documentation
