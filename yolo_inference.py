from ultralytics import YOLO

model = YOLO('models/best.pt')

results = model.predict('Data/08fd33_4.mp4', save=True, save_dir = 'C:/Study/Projects/AI-ML Football Analysis System')
print(results[0]) # First Frame
print('==============================================')
for box in results[0].boxes:
    print(box)
