from ultralytics import YOLO

model = YOLO('/Users/pradyumnakombethotaramgopal/Desktop/Dataset/best.pt')

metrics = model.val(
    data='/Users/pradyumnakombethotaramgopal/Desktop/Dataset/config.yaml',
    split='test'
)

print(metrics)
