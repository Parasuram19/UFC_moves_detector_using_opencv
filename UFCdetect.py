from ultralytics import YOLO 
# val = YOLO('args.yaml')
val = YOLO('best.pt')
# val = YOLO('args.yaml').load('best.pt') 

img="Sample.mp4"
res = val.track(img,save=True,tracker='bytetrack.yaml')