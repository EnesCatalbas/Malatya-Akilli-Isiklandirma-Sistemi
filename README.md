# Malatya-Akilli-Isiklandirma-Sistemi

Bu proje, **TÜBİTAK 2209-A Üniversite Öğrencileri Araştırma Projeleri Destekleme Programı** kapsamında geliştirilmektedir. Malatya ilindeki trafik yoğunluğunu azaltmak amacıyla, simülasyon tabanlı ve yapay zeka (Pekiştirmeli Öğrenme) destekli bir akıllı kavşak yönetim sistemi hedeflenmektedir.

## Proje Özeti
Malatya'nın kritik kavşakları **SUMO (Simulation of Urban Mobility)** üzerinde modellenerek, **E3 dedektörleri** aracılığıyla anlık kuyruk uzunluğu ve bekleme süresi verileri toplanmaktadır. Bu veriler **Python** ortamında işlenerek, **Reinforcement Learning (DQN vb.)** algoritmaları ile trafik ışıklarının süreleri dinamik olarak optimize edilmektedir.

## Kullanılan Teknolojiler
*   **Simülasyon:** [SUMO (Simulation of Urban Mobility)](https://sumo.dlr.de/docs/index.html)
*   **Programlama:** Python 3.x
*   **Yapay Zeka:** OpenAI Gym / Stable Baselines3 (Pekiştirmeli Öğrenme. Fakat henüz entegre edilmedi)
*   **Harita Düzenleme:** NetEdit & OSM Web Wizard

## Dosya Yapısı
*   `src/`: Optimizasyon ve veri işleme kodları.
*   `networks/`: Malatya harita ve kavşak tasarımları (.net.xml).
*   `scenarios/`: Trafik akış senaryoları (.rou.xml).
*   `results/`: Simülasyon çıktıları ve performans analizleri.

Not: Bu çalışma TÜBİTAK 2209-A programı tarafından desteklenme aşamasındadır ve henüz taslak + basit uygulama seviyesindedir. 2026 TÜBİTAK programına kadar geliştirilmeye devam edecektir.
