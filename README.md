## Overview 

A Python tool that analyszes URL's and determines whether they are legitimate, suspicious , or potentially malicious. It uses URL feature extraction and heuristic rules to identify common phising patterns such as deceptive domains, excessive sudomains, obfuscation, and known attack indicators. The purpose of this python tool is to help assist students, security beginners, and anyone who needs a simple offline phishing detection tool. Phishing attacks prove to consistently be throned as the most common manner of attack. Many phishing attempts rely on malicious URLs designed to trick users into entering credentials or downloading malware and this tool aims to resolve such.

## Features 

This detector is a multi-tool of several capabilities that make it both a learning tool and a practical security aid. The tool utilizes structural analysis of URL's by inspecting domain depth, subdomain usage, and overall length, which helps identify malicious intent behind the structures more efficiently. Additionally, the tool can detect the use of IP addresses in place of domain names and it can flag URLs that contain unusual or uncommon characters. Furthermore, the tool searches for deceptive or high-risk keywords that frequently present themselves in phishing links, including terms related to account verification, security updates, and login prompts. The combination of the analysis of the link, the tool will utilize heuristic rules to produce a rating of classification from safe, suspicious, or high-risk. 

## Installation

To use this Phishing Link Detector you'll need a working Python environment that is on the version 3.10 or above. Additionally, there is a requirements.txt file to ensure all the necessary Python dependencies can be installed easily and consistently. Once inside the project directory, the required libraries can be installed by running a pip command that be referenced in the requirements.txt file. This gurantees that all required modules needed for URL parsing, feature extraction, and otional machine-lerarning functionally are avaliable before the program is executed. After these steps have been followed, the tool is fully ready to run on any compatiable system!

Additionally, if you may want to convert this tool into a .exe instead, you can utilize the PyInstaller to package it.
## How Does it Work?

The detector operates by extracting meaningful features from a URL and applying a set of heuristic rules that reflect well-documented phishing behaviors. It evaluates the depth of the domain, checks for excessive subdomain, identifies the presence of IP-based URLs, and looks for unusual or obfuscated characters that attackers often use to disguise malicious links. The program also searches for deceptive keywords that mimic legitimate services, such as misspelled brand names or terms like "verify,", "secure," or "update," which frequently appear in phishing attempts. A probability score is then produced by  and given to the user depending on the individual factors of probabilty given from such details. 

## Directory

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
