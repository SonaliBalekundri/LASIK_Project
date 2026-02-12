👁️ Project #2: LASIK Corneal Topography Analyser
🏥 Domain: Medical Image Processing / Computer Vision

⚙️ What it does: Automated analysis of corneal topography images from WaveLight EX500 LASIK surgical planning system. The tool:
	1.	Extracts the ablation profile region from full screenshots
	2.	Detects irregular corneal regions (“Taluses”) using contour detection
	3.	Calculates centroid coordinates for each region
	4.	Computes talus angles using trigonometry (tan⁻¹(y/x))
	5.	Applies zone-based percentage adjustments based on colour intensity

🔧 Technical Pipeline: Full Screenshot → Crop ROI → BGR → LAB conversion → Gaussian Blur → Thresholding → Contour Detection → Moment Calculation → Angle Computation

📌 About the Project: A Python tool to automate corneal topography analysis for LASIK surgery planning — built with a team under the guidance of an ophthalmologist, using real patient scan data from a WaveLight EX500 system.

❓ Problem & Solution: Surgeons manually analyze corneal heat maps to identify irregular regions (“taluses”) and calculate angles for surgical precision. We automated this — detecting taluses, computing centroids, and calculating angles in seconds.

🛠️ What We Built:
→ Image cropping to extract the 6.5mm optical zone from WaveLight EX500 screenshots
→ Contour detection using LAB color space and adaptive thresholding
→ Centroid calculation using image moments
→ Trigonometric angle computation (tan⁻¹(Δy/Δx))
→ Interactive trackbars for real-time threshold adjustment
→ Zone-based percentage system (6 color zones from bright purple to orange)

💻 Tech & Tools: Python | OpenCV | NumPy | Math

📚 What I Learned: This was my first dive into medical imaging and taught me that computer vision isn’t just about detecting objects — it’s about extracting meaningful clinical data. Understanding color spaces (BGR vs LAB) and why certain transformations work better for specific tasks was a game-changer.

🔄 What I’d Do Differently Today:
→ Use deep learning (U-Net or Mask R-CNN) for more robust segmentation
→ Build a web interface with Flask/Streamlit for easier clinical use
→ Add batch processing for multiple patient scans
→ Integrate with DICOM format for hospital system compatibility
→ Add automated report generation with PDF export

#MedicalImaging #ComputerVision #OpenCV #Python #LASIK #HealthTech #StudentProject #BuildingInPublic
