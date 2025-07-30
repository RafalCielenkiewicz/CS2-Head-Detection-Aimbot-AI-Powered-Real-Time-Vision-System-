# CS2 Head Detection Aimbot (AI-Powered, Real-Time Vision System)

** FOR EDUCATIONAL PURPOSES ONLY – THIS PROJECT IS NOT INTENDED FOR CHEATING**

This project demonstrates a fully working, AI-based head detection system integrated with real-time aiming in Counter-Strike 2 (CS2). The system uses a custom-trained YOLOv8 model and live screen analysis to detect enemy heads and assist in aiming – similar to how a real-time vision module would work in robotics or autonomous targeting.

---

## Highlights

- **Real-time head detection** in a live 3D game (CS2)  
- **Trained YOLOv8 model** on thousands of labeled head images  
- **Efficient screen capture** with `MSS` – optimized for real-time detection  
- **Target-locking system** – avoids jitter and locks on the nearest visible head  
- **Mouse automation** – moves the crosshair toward detected heads    

---

## How It Works

1. **Training**  
   - Public head-detection dataset with thousands of labeled samples  
   - Trained on Google Colab with GPU using YOLOv8  
   - Tested different configurations to optimize accuracy vs speed

2. **Detection**  
   - The model scans a limited area (center of screen) to improve performance  
   - Detection is optimized for heads in medium to close range  
   - Output: bounding box coordinates of detected heads

3. **Targeting System**  
   - Locks onto the closest head and follows it smoothly  
   - Uses pyautogui-based mouse control to aim towards the target  
   - Simple logic ensures smooth aiming without flickering between multiple targets

4. **Screen Capture**  
   - Replaced OpenCV with `MSS` for much faster screen capture  
   - System processes only cropped screen area for better performance

---

## Example 

[https://github.com/user-attachments/assets/6cd3be2f-a506-4936-a80f-b94b76c03d0d](https://github.com/user-attachments/assets/bf121271-7e0b-4704-a5e4-f2e0e765cde0)

---

## Technologies Used

- **YOLOv8** – for training and inference  
- **Python** – core language for scripting  
- **Google Colab** – dataset preparation and model training  
- **MSS** – high-performance screen capture  
- **PyAutoGUI** – mouse control for aiming  

---

## Disclaimer

This repository and its content are shared **strictly for educational and demonstrational purposes**.  
Do not use this or similar tools in any form of competitive or online gameplay.


