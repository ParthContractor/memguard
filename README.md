# Readme.Md
## 🧭 Project Snapshot: `memguard` (Work in Progress)

✅ What I’ve Done So Far

1. Defined the problem  
   Memory leaks in iOS apps are hard to detect early — existing tools are manual, slow, and reactive.
2. Created structured solution vision  
   A lightweight CLI tool that scans Swift files, identifies leak-prone patterns, and gives friendly explanations.
3. Finalized 10 MVP leak patterns  
   Stored in patterns.yaml with prompt + code examples — e.g., missing `weak` delegates, retain cycles, etc.
4. Deferred prompt testing  
   GPT prompt-based fix suggestions are parked for future testing and iteration.
5. Created project folder structure  
   Includes /cli, /engine, /tests, and placeholder files to maintain clean architecture.
6. Implemented core matcher logic  
   matcher.py loads YAML rules, scans each Swift file line by line, and returns relevant matches.
7. Built and tested working scanner  
   scan.py CLI reads all Swift files recursively from any project directory and prints clear results.
8. Confirmed output with real Swift project  
   Successfully detected both clean and leaky code using the provided memguard-sample test project.



