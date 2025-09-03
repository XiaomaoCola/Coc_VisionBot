<p align="center">
  🌐 <strong>Language</strong> | 🇯🇵 <a href="./README.md"><strong>日本語</strong></a> | 🇺🇸 <a href="./README_en.md"><strong>English</strong></a> | 🇨🇳 <a href="./README_ch.md"><strong>中文</strong></a>
</p>

## Live Demo Video

🎥 [Watch Live Demo](https://youtu.be/HaeDby77l3Y)

---

## Background

### Project Runtime Environment

1. This project only works at 1920*1080 resolution.
2. This project only works in Bluestack.
3. This project requires installing tesseractocr on the computer and adding it to environment variables.
4. Tesseract only runs normally on Windows, so this project can only be tested on Windows.

---

### About Ban Mechanisms

(After understanding COC's ban mechanism, it can be applied to other games in the future.)
1. Repeatedly clicking the same coordinates.
	1. Whether deploying troops or various clicks, they must be randomly clicked within the maximum possible range.
2. Total time control.
	1. Online time should not exceed 10 hours per day.
3. Adding rest time.
	1. For example, after 10 to 20 attacks, automatically idle for 10 to 20 minutes.
4. Possible detection of multiple accounts on the same device with the same IP address.
	1. One device with one IP should ideally have only 10 accounts.
	2. If there are more accounts, change VPN address. Express VPN can provide fixed addresses, 10 accounts per address.
	3. Different devices can use virtual machines, whether Android virtual machines or Windows virtual machines can be created. This will be studied later. One IP address with one device should be sufficient.
	4. Script variations: write multiple scripts, for example, one script deploys Lightning Dragons, another deploys Fire Dragons, 5 accounts use Lightning Dragons, 5 accounts use Fire Dragons.
5. Too many clicks in one battle with too short intervals will result in bans.
	1. Can use drag and hold combined with random clicking, with random click count upper limit, such as 30 times.

---

## Core Technology Architecture

### Anti-Detection Technology
- **Advanced Randomization Algorithm**: Adopts multi-layer random number generation strategies, including coordinate random offset, time interval randomization, behavior pattern randomization, etc., effectively evading game anti-cheat system pattern recognition
- **Intelligent Behavior Simulation**: Based on real player behavior data analysis, implements humanized operation rhythm and decision delays, significantly reducing detection risks

### Computer Vision Technology
- **OpenCV Image Processing Engine**: Integrates advanced computer vision libraries to achieve high-precision game interface recognition and target detection
- **Adaptive Template Matching**: Uses multi-scale, multi-angle template matching algorithms to ensure stable recognition accuracy under different game states
- **Real-time Image Analysis**: Based on pixel-level analysis for game state monitoring, achieving millisecond-level response intelligent decisions

### Deep Learning OCR Technology
- **PaddleOCR Text Recognition Engine**: Integrates Baidu PaddlePaddle deep learning framework OCR model to achieve precise recognition of in-game numerical values
- **Resource Intelligent Assessment System**: Real-time recognition of key resource quantities like Elixir and Gold through OCR technology, automatically determining attack profitability based on preset strategy algorithms
- **Multi-language Text Recognition**: Supports game interface text recognition in various language environments, improving script internationalization adaptation capabilities

### System Integration and Optimization
- **Tesseract OCR Integration**: Combines traditional OCR engines as backup recognition solutions, improving text recognition fault tolerance and stability
- **Multi-threaded Asynchronous Processing**: Adopts asynchronous programming mode to achieve parallel processing of image processing, decision calculation, and operation execution
- **Intelligent Resource Management**: Dynamically monitors system resource usage, adaptively adjusting processing precision and speed balance points

---

## Future Expansion Directions

### Diversified Attack Strategy System
- **Tactical Algorithm Library**: Develop machine learning-based diverse attack strategies, including Lightning Dragon flow, Fire Dragon flow, mixed flow and other different tactical combinations
- **Adaptive Strategy Selection**: Automatically select optimal attack plans based on enemy base layouts, achieving intelligent strategy matching
- **Attack Success Rate Optimization**: Continuously optimize execution effects of various strategies through big data analysis of historical battle records

---

## Usage Instructions and Disclaimer

### Usage Instructions
This project is for personal learning and technical exploration purposes, aimed at researching practical applications in related technical fields such as computer vision, image recognition, OCR technology, etc.

### Disclaimer
- This project is **for learning and research purposes only**, with no intention to interfere with any real elections or violate platform rules
- Users should comply with relevant laws, regulations, and platform terms of service
- If citation, testing, or collaboration is needed, please declare the purpose of use in advance and respect legal and moral boundaries
- The project author assumes no legal responsibility arising from the use of this project
- Please use this project under legal and compliant premises, and do not use it for any illegal or non-compliant activities

**Important Reminder: Please ensure your usage behavior complies with local laws and regulations as well as relevant platform terms of use.**
