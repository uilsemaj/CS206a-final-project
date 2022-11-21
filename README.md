## for offline execution (only my local)
conda activate roboticsfinalproject

# Signal Processing
## File
- bpm-detection taken from: https://github.com/scaperot/the-BPM-detector-python
- works decently enough.

## calibration
- 80 bpm: shows up as 160 bpm on bpm_detection
- 140bpm.wav: shows up as 207.85219399538104 on bpm_detection
- starwars is about "Completed!  Estimated Beats Per Minute: 159.24642544499562" and based on 
- to run: ```python bpm_detection.py --filename calibration/104bpm.wav```

